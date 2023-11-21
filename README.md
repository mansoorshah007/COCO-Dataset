# COCO Dataset Downloader

This script allows you to download and extract the COCO (Common Objects in Context) dataset and annotations. The COCO dataset is widely used for object detection and segmentation tasks.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install package_name`):
  - requests
  - numpy
  - tqdm
  - pycocotools

## Usage

1. Clone or download this repository to your local machine.

2. Run the `coco-dataset-downloader.py` script. This script will:

   - Download the COCO dataset if it's not already downloaded.
   - Extract the dataset to a specified directory.
   - Download the COCO annotations if they're not already downloaded.
   - Extract the annotations to the same directory.

   ```bash
   python3 coco-dataset-downloader.py
