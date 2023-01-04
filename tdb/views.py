from django.http import HttpResponse

def Hello(request):
    return HttpResponse("HI")