from PIL import Image, ImageFont, ImageDraw

FONT_FILE = ImageFont.truetype(r'Poppins-SemiBold.ttf', 175)
FONT_COLOR = "#000000"
WIDTH, HEIGHT = 1739,732

def make_cert(name):
    image_source = Image.open(r'template_Sertfikat.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text((WIDTH-name_width/2, HEIGHT-name_height/2), name, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + name+".jpg")
    print('printing certificate of: '+name)

names = ['coba1','coba2']
def make_no(no,names):
    WIDTH, HEIGHT = 1408,415
    FONT_FILE = ImageFont.truetype(r'Poppins-SemiBold.ttf', 80)
    image_source = Image.open(r'./out/'+names+'.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(no, font=FONT_FILE)
    draw.text((WIDTH-name_width/2, HEIGHT-name_height/2), no, fill=FONT_COLOR, font=FONT_FILE)
    image_source.save("./out/" + no+".jpg")
    print('printing certificate of: '+no)
no = ['001','002']
for x in names:
    make_cert(x)
for x in range(len(no)):
    for y in range(len(names)):
        if x==y:
            make_no(no[x],names[y])