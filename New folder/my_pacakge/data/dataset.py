import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms
        with jsonlines.open(self.annotation_file, "r") as f:
            self.anns = list(f.iter())

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.anns)

    def __getitem__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.anns[idx]

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        image = Image.open(path).convert("RGB")
        if self.transforms:
            for transform in self.transforms:
                image = transform(image)
        return image