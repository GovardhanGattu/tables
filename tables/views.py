from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def tables(request , num):
	data = { 'res': num , 'range':range(1,11) }

	return render(request,'tables/tables.html',{'info':data})

def add(request):
	return render(request,'tables/add.hmtl')