from django.core.mail import send_mail


def send_email(subject, address):
    send_mail('Продукти для перевірки', subject,
              'kuptsovsasha@gmail.com', [address], fail_silently=False)




