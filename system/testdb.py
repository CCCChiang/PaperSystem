# from django.http import HttpResponse
# from mltdc.models import Test

# def add(request):
#     name = request.POST.get('name')
#     age = request.POST.get('age')
#     sex = request.POST.get('sex')
#     test = Test(name = name, age = age, sex = sex)
#     test.save()

#     return HttpResponse("<p> You have uploaded data to MLTDC_TDB successfully. </p>")

# def getALL(request):
#     list = Test.objects.all()
#     response=''
#     for var in list:
#         response += var.name + " "

#     return HttpResponse(response)

# def update(request):
#     id = request.GET.get('id')
#     test = Test.objects.get(id=id)
#     test.name = "oooo"
#     test.save()

#     return HttpResponse("<p> You have moditied data to MLTDC_TDB successfully. </p>")

# def delete(request):
#     id = request.GET.get('id')
#     test = Test.objects.get(id=id)
#     test.delete()

#     return HttpResponse("<p> You have deleted data to MLTDC_TDB successfully. </p>")