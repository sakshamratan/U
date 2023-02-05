import numpy as np
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if isinstance(image, Image.Image):
            w, h = image.size
            if isinstance(self.output_size, int):
                if h > w:
                    new_h, new_w = self.output_size * h / w, self.output_size
                else:
                    new_h, new_w = self.output_size, self.output_size * w / h
            else:
                new_h, new_w = self.output_size

            image = image.resize((int(new_w), int(new_h)))
            return image
        else:
            raise ValueError("Input must be a PIL image.")
