import numpy as np
from PIL import Image, ImageFilter

class BlurImage(object):
    def __init__(self, radius):
        self.radius = radius
       
  

    def __call__(self, image):
         if type(image) == np.ndarray:
                image = Image.fromarray(image)
                image = image.filter(ImageFilter.GaussianBlur(radius=self.radius))
        if type(image) == Image:
            image = np.array(image)
        return image
    