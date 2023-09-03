import json
import os
import zipfile
from os.path import isfile
import requests
import numpy as np
from pathlib import Path

from tqdm.notebook import tqdm
from pycocotools.coco import COCO
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

COCODatasetUrl = "http://images.cocodataset.org/zips/train2014.zip"
COCOAnnotationUrl = "http://images.cocodataset.org/annotations/annotations_trainval2014.zip"
dataDir = "data"

def downloadCOCODataset(datasetUrl, annotationsUrl, dataDir):

    Path(dataDir).mkdir(parents  = True, exist_ok = True)
    datasetZipPath = os.path.join(dataDir, "train2014.zip")

    if not isfile(datasetZipPath):
        print("Downloading COCO dataset...")

        response = requests.get(datasetUrl)
        with open(datasetZipPath, 'wb') as file:
            file.write(response.content)

    datasetExtractedDir = os.path.join(dataDir, "train2014")

    if not os.path.exists(datasetExtractedDir):
        print("Extracting COCO dataset...")

        with zipfile.ZipFile(datasetZipPath, 'r') as zipRef:
            zipRef.extractall(dataDir)

    annotationsZipPath = os.path.join(dataDir, "annotations_trainval2014.zip")

    if not isfile(annotationsZipPath):
        print("Downloading COCO annotations...")
        response = requests.get(annotationsUrl)

        with open(annotationsZipPath, 'wb') as file:
            file.write(response.content)

    annotationsExtractedDir = os.path.join(dataDir, "annotations")

    if not os.path.exists(annotationsExtractedDir):
        print("Extracting COCO annotations...")

        with zipfile.ZipFile(annotationsZipPath, 'r') as zipRef:
            zipRef.extractall(dataDir)

downloadCOCODataset(COCODatasetUrl, COCOAnnotationUrl, dataDir)
dataset = COCO(os.path.join(dataDir, 'annotations', 'instances_train2014.json'))

