import twilio
from twilio.rest import Client

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

'''from skimage import io
from keras.models import load_model'''

from PyPDF2 import PdfFileWriter, PdfFileReader 

import secrets
"""
def predict_ct(link):
  img = image.load_img(link, grayscale=False, target_size=(64, 64))
  disease_class = ['p','n']
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis = 0)
  x /= 255

  custom = model.predict(x)

  a=custom[0]
  ind=np.argmax(a)
    
  return disease_class[ind]
"""
def send_sms(target_contact,message_content,hospital):
  account_sid = 'AC086b805caf8c43de3e755d6543502d9c'
  auth_token = '6c9cda7dba1b0a539f233b372e2b086c'
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                      body=f'\n\nFrom {hospital} via Iris:\n\n{message_content}',
                      from_='+14243476632',
                      to=target_contact
                  )  
  return True

def send_email(target_email,message_content):
  message = Mail(
  from_email=('iris.contactonline@gmail.com','Iris'),
  to_emails=target_email,
  subject='Your results are ready!',
  html_content=message_content)
  try:
    sg = SendGridAPIClient('SG.0btdzfBXQqq4LcdaYxYQxQ.XL2YqBA0SHW-NTlQ4qTv4C9GLdVGLocaUdOzQaUT2Ik')
    response = sg.send(message)
    status = response.status_code
    if status = 202:
      return True
    else:
      return False
  except Exception as e:
    return False

def generate_pdf_password():
  return secrets.token_hex(2).upper()

def encrypt_pdf(password,filename):
  out = PdfFileWriter() 
    
  file = PdfFileReader("myfile.pdf") 
    
  num = file.numPages 
    
  for idx in range(num): 
      
      page = file.getPage(idx) 
      out.addPage(page) 
    
  out.encrypt(password) 
    
  with open(f"{filename}.pdf", "wb") as f: 
      out.write(f)

  


