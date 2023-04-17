from django.core.signing import Signer
import qrcode
from .settings import HOST_URL
from questions.models import Question

# Importing the PIL library
from PIL import ImageDraw, ImageFont, Image
LOGO = Image.open('logo.png').resize((150,150))

signer = Signer()
font = ImageFont.truetype('Roboto-Black.ttf', 80)
font_small = ImageFont.truetype('Roboto-Black.ttf', 40)
question_list = Question.objects.all()
total = question_list.count()




def generate_qr(url, name, qrcode_number, riddle):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=8,
        version=12, )
    qr.add_data(str(url))
    qr.make()
    img_qr_big = qr.make_image().convert('RGB')
    pos = ((img_qr_big.size[0] - LOGO.size[0]) // 2, (img_qr_big.size[1] - LOGO.size[1]) // 2)
    img = qr.make_image()
    img_qr_big.paste(LOGO, pos)
    I1 = ImageDraw.Draw(img_qr_big)
    I2 = ImageDraw.Draw(img_qr_big)

    # Add Text to an image
    I1.text((220, -3), 'Riddle #' +str(qrcode_number), font=font, fill=000)
    I2.text((0, 730), riddle, font=font_small, fill=000)
    img_qr_big.save("./qrcodes/"+name+".png")


"""
print("\n\n #### Creating QR CODES ####")
print('0%')
for i in question_list:
    secret = signer.sign(str(i.id))
    url_live = HOST_URL +"/qr/"+ secret
    url_dev = 'http://localhost:8000/qr/'+secret
    filename = i.riddle
    filename = filename.replace(",", "_")
    filename = filename.replace("/", "_")
    filename = filename.replace(' ', '-').lower()
    filename = filename[0:20]
    generate_qr(url_live, filename, i.id, i.riddle[0:38]+'...')
    print(str(round(i.id/total*100))+"%")
print(url_live)
print(url_dev)
print("#### All done, starting server ####\n\n")"""