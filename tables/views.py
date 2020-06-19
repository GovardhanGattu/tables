from django.shortcuts import render
from django.http import HttpResponse
from tables.models import Table
from tables.forms import Mytable


# Create your views here.

def tables(request):
	if request.method == "POST":
		num=request.POST.get("number")
		data = { 'res': num , 'range':range(1,11) }

	return render(request,'tables/tables.html',{'info':data})

def select(request):
	form=Mytable()
	return render(request,'tables/select.html',{'form':form})