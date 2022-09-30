from rest_framework.generics import ListAPIView
from .serializers import UtilisationSerializer
from .models import Utilisation
import psutil
from django.core.mail import send_mail
# Create your views here.

def check_usage(ram_usage):
    print("usage is over 50")
    import time
    t=time.time()
    prev=ram_usage
    print(t)
    while time.time()-t <= float(10):
        print(t-time.time())
        if prev > float(50):
            prev=dict(psutil.virtual_memory()._asdict())['percent']
            print("in if part")
        else:
            print("Usage is stable now")
            return False
    try:
        send_mail('Ram over utilisation', 'RAM stayed for 50% for over 10 seconds.', 'noreply@takvaviya.com', ['krishnakumar31096@gmail.com'], fail_silently=False)
        return True
    except Exception as e:
        print("Exception occured in sending ,mail ",e)
        return False

def store_tasks_todb():
    cpu_usage=psutil.cpu_percent()
    ram_usage=dict(psutil.virtual_memory()._asdict())['percent']
    if ram_usage >float(50):
        if check_usage(ram_usage):
            print("Successfully sent email")
        else:
            print("failed to send email")

    from datetime import datetime
    current_datetime=datetime.now()
    try:
        utilisation=Utilisation()
        utilisation.cpu_usage=cpu_usage
        utilisation.ram_usage=ram_usage
        utilisation.save()
    except Exception as e:
        print("Exception occured in saving ",e)




class ListUtilisation(ListAPIView):
    serializer_class = UtilisationSerializer
    queryset = Utilisation.objects.all()



