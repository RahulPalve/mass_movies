from django.shortcuts import render , HttpResponse
from main import link_proc as lp
from django.db import models
from main.models import Movie
 
def index(request):
    for no in range(100,1000):
        try:
            ID, TITLE, POSTER, PLOT, DL_LINK=lp.process(no)
            m=Movie(id=ID, title=TITLE, poster=POSTER, plot=PLOT, dl_link=DL_LINK)
            m.save()
        except:
            pass
    return HttpResponse("Done!")
# Create your views here.