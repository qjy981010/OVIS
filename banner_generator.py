import PIL.Image as Image
from PIL import ImageEnhance
import os
from IPython import embed


IMAGES_PATH = '/mnt/d/data/annotatation/annotations_before/annotations_coco_1112_v4/VisualizeMask'  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = [90, 160]  # 每张小图片的大小
IMAGE_ROW = 5  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 12  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = './assets/css/banner_new.jpg'  # 图片转换后的地址


# 获取图片集地址下的所有图片名称
image_names = [os.path.join(annid, 'img_0000001.jpg') for annid in os.listdir(IMAGES_PATH) if '_' not in annid]

# # 简单的对于参数的设定和实际图片集的大小进行数量判断
# if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
#     raise ValueError("合成图片的参数和要求的数量不能匹配！")

# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE[1], IMAGE_ROW * IMAGE_SIZE[0])) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(IMAGE_ROW):
        for x in range(IMAGE_COLUMN):
            from_image = Image.open(os.path.join(IMAGES_PATH, image_names[IMAGE_COLUMN * y + x])).resize(
                (IMAGE_SIZE[1], IMAGE_SIZE[0]), Image.ANTIALIAS)
            from_image = ImageEnhance.Brightness(from_image).enhance(0.5)
            to_image.paste(from_image, (x * IMAGE_SIZE[1], y * IMAGE_SIZE[0]))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图
image_compose() #调用函数