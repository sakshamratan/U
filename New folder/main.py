#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    dataset = Dataset(annotation_file)
    download = Download()

#Print image names and their captions from annotation file using dataset object
    data = dataset.get_data()
    for i, item in enumerate(data):
        print(f'{i + 1}. Image name: {item["image_name"]} Caption: {item["caption"]}')

#Download images to ./data/imgs/ folder using download object
    download.download(data)

#Transform the required image (roll number mod 10) and save it seperately
    for i, item in enumerate(data):
        if (i+1) % 10 == 0:
            img = Image.open(f'./data/imgs/{item["image_name"]}')
            for transform in transforms:
                img = transform(img)
                img.save(f'./data/imgs/{item["image_name"]}_transformed.jpg')
        
#Get the predictions from the captioner for the above saved transformed image
    for i, item in enumerate(data):
        if (i+1) % 10 == 0:
            img_path = f'./data/imgs/{item["image_name"]}_transformed.jpg'
            pred = captioner.predict(img_path)
            print(f'Caption for transformed image: {pred}')
        
def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage(), BlurImage(1)], None) # Sample arguments to call experiment()
if name == 'main':
main()




