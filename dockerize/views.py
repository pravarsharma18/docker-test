from django.http import HttpResponse


def home(request):
    return HttpResponse(f"<h1>Running on {request.META['SERVER_PORT']}</h1>")
