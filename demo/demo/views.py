from django.conf import settings
from django.http import HttpResponse


def example (request):
    sum = 0
    for i in range(200_000_000):
        sum += i
    return HttpResponse(f"Version: {settings.VERSION} / {settings.REF} / Sum: {sum}")