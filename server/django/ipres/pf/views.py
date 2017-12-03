from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    fc = "Cannot open the info file."
    try:
        file_ob = open('/root/files/ip')
        fc = file_ob.read()
        file_ob.close()
    except:
        pass

    return render(request, 'pf/index.html', {'file_content': fc})
    #return HttpResponse("Hello, world. You're at the polls index.")
