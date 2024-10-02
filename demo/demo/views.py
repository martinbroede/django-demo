from time import sleep

from django.conf import settings
from django.http import HttpResponse


def intensive_task():
    sum = 0
    for i in range(10_000_000):
        if(i % 500_000 == 0):
            sleep(0.05)
        sum += i

def example (request):
    intensive_task()
    return HttpResponse(f"Version: {settings.VERSION} / Ref: {settings.REF} / DB: {settings.DATABASES['default']['ENGINE']}")