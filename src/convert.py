# https://www.kaggle.com/datasets/mihaelaborta/cots-detection

import os, csv, ast
import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext, get_file_name
from dotenv import load_dotenv

import supervisely as sly
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_size
import shutil

from tqdm import tqdm


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "cots detection"
    images_path = "/home/grokhi/rawdata/cots-detection/train_images"
    ann_path = "/home/grokhi/rawdata/cots-detection/train.csv"
    batch_size = 30
    ds_name = "train"

    def create_ann(image_path):
        labels = []
        tags = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 720  # image_np.shape[0]
        img_wight = 1280  # image_np.shape[1]

        video_name = image_path.split("/")[-2]

        image_name = video_name + "/" + get_file_name_with_ext(image_path)

        tags += [sly.Tag(meta) for meta in video_meta if meta.name == video_name]

        tags += [
            sly.Tag(sequence_tag, value=name_to_sequence[image_name]),
            sly.Tag(video_frame_tag, value=name_to_frame[image_name]),
            sly.Tag(sequence_frame_tag, value=name_to_sequenceframe[image_name]),
        ]

        ann_data = name_to_data[image_name]
        for curr_ann_data in ann_data:
            left = int(curr_ann_data["x"])
            top = int(curr_ann_data["y"])
            right = left + int(curr_ann_data["width"])
            bottom = top + int(curr_ann_data["height"])
            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class)
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    obj_class = sly.ObjClass("starfish", sly.Rectangle)
    tag_names = ["video_0", "video_1", "video_2"]
    video_meta = [sly.TagMeta(elem, sly.TagValueType.NONE) for elem in tag_names]

    sequence_tag = sly.TagMeta("sequence", sly.TagValueType.ANY_NUMBER)
    video_frame_tag = sly.TagMeta("video_frame", sly.TagValueType.ANY_NUMBER)
    sequence_frame_tag = sly.TagMeta("sequence_frame", sly.TagValueType.ANY_NUMBER)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=video_meta + [sequence_tag, video_frame_tag, sequence_frame_tag],
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    name_to_data = {}
    name_to_sequence, name_to_frame, name_to_sequenceframe = {}, {}, {}

    if ann_path is not None:
        with open(ann_path, "r") as file:
            csvreader = csv.reader(file)
            for idx, row in enumerate(csvreader):
                if idx == 0:
                    continue
                image_subpath = "video_{}/{}.jpg".format(row[4].split("-")[0], row[4].split("-")[1])
                name_to_data[image_subpath] = ast.literal_eval(str(row[-1]))
                name_to_sequence[image_subpath] = ast.literal_eval(str(row[1]))
                name_to_frame[image_subpath] = ast.literal_eval(str(row[2]))
                name_to_sequenceframe[image_subpath] = ast.literal_eval(str(row[3]))

    images_names = list(name_to_data.keys())

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        real_images_names = [im_name.replace("/", "_") for im_name in images_names_batch]

        img_infos = api.image.upload_paths(dataset.id, real_images_names, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))
    return project
