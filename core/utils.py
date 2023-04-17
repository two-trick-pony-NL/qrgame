from django.core.signing import Signer
import qrcode
from .settings import HOST_URL
from questions.models import Question

# Importing the PIL library
from PIL import ImageDraw, ImageFont, Image
LOGO = Image.open('logo.png').resize((150,150))

signer = Signer()
font = ImageFont.truetype('Roboto-Black.ttf', 40)
question_list = Question.objects.all()
total = question_list.count()




def generate_qr(url, name, qrcode_number):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(str(url))
    qr.make()
    img_qr_big = qr.make_image().convert('RGB')
    pos = ((img_qr_big.size[0] - LOGO.size[0]) // 2, (img_qr_big.size[1] - LOGO.size[1]) // 2)
    img = qr.make_image()
    img_qr_big.paste(LOGO, pos)
    I1 = ImageDraw.Draw(img)
    # Add Text to an image
    I1.text((150, -3), 'QR: ' +str(qrcode_number)+ ' of '+str(total), font=font, fill=000)
    img_qr_big.save("./qrcodes/"+name+".png")



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
    generate_qr(url_live, filename, i.id)
    print(str(round(i.id/total*100))+"%")
    print(url_live)
    print(url_dev)
    print('\n')
print("#### All done, starting server ####\n\n")