from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from . models import place
from . models import team


def operations(request):
    obj=place.objects.all()
    team_obj=team.objects.all()
    #name = "friends"
    #return render(request, "index1.html",{'obj' :name,})
    #return render(request, "formpage.html")
    return render(request,"index1.html",{'result':obj,
                                         'result1':team_obj
                                         })

#def result(request):
   # x=int(request.GET["num1"])
   # y=int(request.GET["num2"])
    #add=x+y
   # sub=x-y
   # mul=x*y
   # div=x/y

    #return render(request,"result.html",{'addition':add,
                                        # 'substraction':sub,
                                        # 'multiplication':mul,
                                         #'division':div})

#def Home(request):
   # return HttpResponse("Home page")


#def About(request):
   #return render(request, "About1.html")


#def Details(request):
    #return HttpResponse("Details")


#def contact(request):
   # return render(request, "contact1.html")



