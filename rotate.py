import numpy as np
from PIL import Image, ImageOps, ImageEnhance

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self.degrees = degrees

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        if isinstance(image, Image.Image):
            image = image.rotate(self.degrees)
            return image
        else:
            raise ValueError("Input must be a PIL image.")
