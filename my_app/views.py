from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Hello, Alex"
    )

def home_page(request):
    return HttpResponse(
        "HOME PAGE"
    )