from django.http import HttpResponse

def Index(request):
    return HttpResponse("Welcome to the Homepage")
