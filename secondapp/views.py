
from django.db.models.expressions import OrderBy
from django.shortcuts import render
from secondapp.models import Hospital

def index(request) :
    Hospital_list=Hospital.objects.all().order_by('id')
    for i in Hospital_list :
        print(i.id,end=' ')
        print(i.sido)
    
    return render(request,'../templates/Hospital_main.html',{'Hospital_list' : Hospital_list})
    
# Create your views here.
