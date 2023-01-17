from PIL import Image
from glob import glob
from os import path

raw_path = '_img/posts/'
data_path = 'assets/img/posts/'

size_array = [
    {
        'width': 230,
        'suffix': '_placehold'
    },
    {
        'width': 535,
        'suffix': '_thumb'
    },
    {
        'width': 535 * 2,
        'suffix': '_thumb@2x'
    },
    {
        'width': 575,
        'suffix': '_xs'
    },
    {
        'width': 767,
        'suffix': '_sm'
    },
    {
        'width': 991,
        'suffix': '_md'
    },
    {
        'width': 1999,
        'suffix': '_lg'
    },
    {
        'width': 1920,
        'suffix': ''
    }
]

ext_array = ['jpg', 'png']

for ext in ext_array:
    images = [Image.open(img) for img in glob(path.join(raw_path, '*.' + ext))]
    image_name_array = [img.split('\\')[-1].split('.')[0] for img in glob(path.join(raw_path, '*.' + ext))]
    print(image_name_array)

    for idx, im in enumerate(images):
        # print(image.size)
        for size in size_array:

            w = size['width']
            h = int(size['width'] * im.size[1] / im.size[0])
            im2 = im.resize((w,h))

            im2 = im2.convert('RGB')
            im2.save(data_path + image_name_array[idx] + size['suffix'] + '.jpg', 'JPEG')
