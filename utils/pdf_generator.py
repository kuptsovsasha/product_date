import pdfkit
import requests
from django.http import cookie

from django.utils import timezone
options = {
    'shop': 1333,
    'department': 'Молочка'
}


r = requests.get('http://127.0.0.1:8000/product/' )


print(r.content)