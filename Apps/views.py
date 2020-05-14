from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def test(request):
	return render(request,'main.html')

def login(request):
	if request.method == 'GET':
		name=request.GET.get('username')
		pwd=request.GET.get('password')
		print('Get:')
	else:
		name=request.POST.get('username')
		pwd=request.POST.get('password')
		print('Post:')
		if checkuser(name,pwd) == True:
			return HttpResponseRedirect('../main')
		else:
			messages.success(request,"用户名或密码有误")

	print(name,pwd)
	return render(request,'login.html')

#检查用户名和密码
def checkuser(name,pwd):
	if name[:4] == '2017' and pwd != '':
		return True
	return False
