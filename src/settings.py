from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "CSIRO COTS Detection"
PROJECT_NAME_FULL: str = "CSIRO COTS: The CSIRO Crown-of-Thorn Starfish Detection Dataset (a.k.a. TensorFlow - Help Protect the Great Barrier Reef Competition)"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    source_url="https://www.kaggle.com/competitions/tensorflow-great-barrier-reef/rules",
    redistributable=False,
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Ecological()]
CATEGORY: Category = Category.Environmental()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2021

HOMEPAGE_URL: str = "https://www.kaggle.com/competitions/tensorflow-great-barrier-reef"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 9492717
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/cots-detection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/competitions/tensorflow-great-barrier-reef/data"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/abs/2111.14311"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[
    str
] = "https://www.kaggle.com/competitions/tensorflow-great-barrier-reef/overview"
AUTHORS: Optional[List[str]] = [
    "Jiajun Liu",
    "Brano Kusy",
    "Ross Marchant",
    "Brendan Do",
    "Torsten Merz",
    "Joey Crosswell",
    "Andy Steven",
    "Nic Heaney",
    "Karl von Richter",
    "Lachlan Tychsen-Smith",
    "David Ahmedt-Aristizabal",
    "Mohammad Ali Armin",
    "Geoffrey Carlin",
    "Russ Babcock",
    "Peyman Moghadam",
    "Daniel Smith",
    "Tim Davis",
    "Kemal El Moujahid",
    "Martin Wicke",
    "Megha Malpani",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "jiajun.liu@csiro.au",
    "brano.kusy@csiro.au",
    "ross.marchant@csiro.au",
    "brendan.do@csiro.au",
    "torsten.merz@csiro.au",
    "joey.crosswell@csiro.au",
    "andy.steven@csiro.au",
    "nic.heaney@csiro.au",
    "karl.vonrichter@csiro.au",
    "laclan.tychsen-smith@csiro.au",
    "david.ahmedtaristizabal@csiro.au",
    "ali.armin@csiro.au",
    "geoffrey.carlin@csiro.au",
    "russ.babcock@csiro.au",
    "peyman.moghadam@csiro.au",
    "daniel.v.smith@csiro.au",
    "timdavis@google.com",
    "kelmoujahid@google.com",
    "wicke@google.com",
    "mmalpani@google.com",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "CSIRO, Australia",
    "Queensland University of Technology, Australia",
    "Google, USA",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.csiro.au/en/",
    "https://www.qut.edu.au/",
    "https://www.google.com",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "image sets": ["video_0", "video_1", "video_2"],
    "__POSTTEXT__": "Additionally, every image contains information about its ***sequence***, ***video_frame***, and ***sequence_frame***",
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
