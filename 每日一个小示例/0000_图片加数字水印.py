
#--------------------------

#图片右上角加数字水印

#--------------------------

from PIL import Image, ImageDraw, ImageFont

def add_number_flag(img):
    draw=ImageDraw.Draw(img)
    #设置字体，大小为40
    myfont=ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
    #设置颜色为红色
    fillcolor='#ff0000'
    #获取原始图片大小
    width,height=img.size
    #为图片右上角添加数字0001，位置为：width-字体大小
    draw.text((width-40, 0),'0001',font=myfont,fill=fillcolor)
    #图片保存
    img.save(r"D:/result.jpg","jpeg")


if __name__=="__main__":
    image=Image.open(r'D:/a.jpg')
    add_number_flag(image)
