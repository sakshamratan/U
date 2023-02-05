#Imports
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
      self.radius = radius
    def __call__(self, image):
      if type(image) == np.ndarray:
        image = Image.fromarray(image)
        image = image.filter(ImageFilter.GaussianBlur(radius=self.radius))
    if type(image) == Image:
        image = np.array(image)
    return image
