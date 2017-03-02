from PIL import Image

# Python 中的图像处理库 Pillow
# PIL在Python3中更名为Pillow
# Python2中安装命令: sudo pip install PIL
# Python3中安装命令: sudo pip install Pillow

img = Image.open('pic.JPG')
print(img.size, img.mode)       # (3264, 2448) RGB

# 缩略图 保持原图长宽比不变
# size = (200, 200)
# img.thumbnail(size)
# img.save('/Users/zhangzhao/PycharmProjects/pillow_demo/thum.JPEG')
# print(img.size, img.mode)     # (200, 150) RGB

# 图片剪切
frame = (1632, 0, 3264, 1224) # 图片四分之一右上角部分
# (left, upper, right, lower)
# right > left; lower > upper
# 剪切后图片:
#      x = left;                 y = upper;
# height = lower - upper;    width = right - left;
crop_img = Image.open('pic.JPG').crop(frame)
crop_img.save('/Users/zhangzhao/PycharmProjects/pillow_demo/crop.jpg')
#crop_img.show()
print(crop_img.size)    # (1632, 1224)

# 几何转换
resize_out = crop_img.resize((200, 200))
#resize_out.show()

rotate_out = crop_img.rotate(45)    # 逆时针 45
#rotate_out.show()

# 模式转换
change_mode = resize_out.convert('L')
print(resize_out.mode)  # RGB
print(change_mode.mode) # L


