from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def tables(request):
	if request.method == "POST":
		num=request.POST.get("number")
		data = { 'res': num , 'range':range(1,11) }

	return render(request,'tables/tables.html',{'info':data})

def select(request):
	return render(request,'tables/select.html')