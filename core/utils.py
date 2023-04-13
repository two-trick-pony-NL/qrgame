from django.core.signing import Signer
import qrcode
from .settings import HOST_URL

signer = Signer()


from questions.models import Question

def generate_qr(url, name):
    img = qrcode.make(str(url))
    img.save("./qrcodes/"+name+".png")


question_list = Question.objects.all()
total = question_list.count()
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
    generate_qr(url_live, filename)
    print(str(round(i.id/total*100))+"%")
    print(url_live)
    print(url_dev)
    print('\n')
print("#### All done, starting server ####\n\n")