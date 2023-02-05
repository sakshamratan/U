import numpy as np
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        if isinstance(image, np.ndarray):
            if self.flip_type == 'horizontal':
                return np.fliplr(image)
            elif self.flip_type == 'vertical':
                return np.flipud(image)
        elif isinstance(image, Image.Image):
            if self.flip_type == 'horizontal':
                return image.transpose(Image.FLIP_LEFT_RIGHT)
            elif self.flip_type == 'vertical':
                return image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Input must be a numpy array or a PIL image.")

