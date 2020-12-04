import imageio
import os
from PIL import Image, ImageSequence
from IPython import embed
from webptools import gifwebp


def compose_gif(image_dir, save_dir, range_=None):
    img_paths = list(os.listdir(image_dir))
    img_paths.sort(key=lambda x: x.split('.')[0].split('_')[1])
    img_paths = [os.path.join(image_dir, img_name) for img_name in img_paths]
    img_paths = img_paths[range_]
    gif_images = []
    for path in img_paths:
        # gif_images.append(imageio.imread(path))
        image = Image.open(path)
        image = image.resize((640, 360))
        gif_images.append(image)
        # embed()
        # exit(0)
    
    name = os.path.basename(image_dir)
    gif_images[0].save(os.path.join(save_dir, name+".webp"), save_all=True, append_images=gif_images[1:])
    # imageio.mimsave(os.path.join(save_dir, name+".gif"), gif_images, fps=5)
    # print(gifwebp(os.path.join(save_dir, name+".gif"), os.path.join(save_dir, name+".webp"), "-q 80"))


if __name__ == "__main__":
    image_dir = '/mnt/d/data/annotatation/annotations_before/annotations_coco_1112_v4/VisualizeMask/'
    save_dir = './assets/css/webp'
    os.makedirs(save_dir, exist_ok=True)
    ann_ids = {'2592056': slice(0, 30),
               '2930398': slice(10, 60),
               '2932104': slice(40, 85),
               '3021160': slice(15, 33),
               }
    for ann_id in ann_ids:
        compose_gif(os.path.join(image_dir, ann_id), save_dir, range_=ann_ids[ann_id])