from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    posts = models.post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    modes = models.Mood.objects.all()


    years = range(1960, 2021)
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        uryear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
        print(urfcolor)
    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False


    return render(request,'index.html',locals())