The authors of the **CSIRO COTS: The CSIRO Crown-of-Thorn Starfish Detection Dataset** (a.k.a. **TensorFlow - Help Protect the Great Barrier Reef Competition**) present a comprehensive initiative to address the significant coral loss caused by Crown-of-Thorn Starfish (COTS) outbreaks on the Great Barrier Reef (GBR). The objective is to encourage research in Machine Learning and AI-driven technologies to enhance the detection, monitoring, and management of COTS populations at a reef scale.

Australia's Great Barrier Reef, a national icon and World Heritage Site, faces threats, including Crown-of-Thorns Starfish (COTS). The authors emphasize that COTS are a key factor responsible for coral loss on the GBR. The unique characteristics of COTS, such as their size and poisonous spines, contribute to their impact on coral reef ecosystems.

The World Wide Fund for Nature (WWF) identifies key threats to the GBR, with COTS outbreaks and their correlation to increased farm pollution ranking prominently. Australian agencies are actively engaged in monitoring and managing COTS populations to ensure ecological sustainability.

The authors detail the Manta Tow method, a significant technique for monitoring COTS and coral cover. While effective, the method has limitations related to scalability, data resolution, reliability, and traceability. To address these issues, the authors propose leveraging underwater imaging devices and deep learning algorithms for more efficient and scalable environmental surveys.

## **Data Acquisition**

The data was collected using GoPro Hero9 cameras adapted for the Manta Tow method. The cameras are attached to the manta tow board, providing an oblique field of view of the reef below. The dataset is collected in October 2021 in the Swain Reefs region of the GBR, exhibiting variations in lighting, visibility, coral habitat, depth, distance from the bottom, and viewpoint.

## **Dataset Characteristics**

The authors provide details about the released dataset. It comprises sequences of underwater images collected at five different areas on a GBR reef, totaling over 35,000 images. The dataset is split into *train* and test data, with a focus on COTS as the only class in this object detection dataset. <i>Note, that the test dataset is not provided.</i>

The dataset's unique features include sequence-based annotations, the potential for multiple COTS in the same image, and COTS overlapping each other. The evaluation criteria prioritize recall, reflecting the key objective of finding all visible COTS along defined transect paths.
