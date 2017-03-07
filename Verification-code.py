# coding = utf-8
import Image,ImageFont,ImageDraw
import random

# 随机字母:
def ranChar():
    return chr(random.randint(65,90))

# 随机艳色１:
def ranColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

# 随机艳色2:
def ranColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

# 240 *60
width = 60*4
heigh = 60
image = Image.new('RGB', (width,heigh), (255,255,255))
# 创建 Font对象：
font = ImageFont.truetype('/home/chen/my_blog/public/lib/font-awesome/fonts/fontawesome-webfont.ttf', 36)
# 创建Draw对象：
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(heigh):
        draw.point((x,y), fill=ranColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('/home/chen/code.jpg', 'jpeg');
