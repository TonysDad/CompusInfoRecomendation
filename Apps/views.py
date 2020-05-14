from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse

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
		else: #判断是否有注册信息
			messages.success(request,"用户名或密码有误")
	#
	# print(name,pwd)
	return render(request,'login.html')

#检查用户名和密码
def checkuser(name,pwd):
	if name == None or pwd == None:
		return False
	if name[:4] == '2017' and pwd != '':
		return True
	return False

#得到用户注册的数据
def register(request):
	reg_name = request.POST.get ( 'reg_name' )
	reg_pwd = request.POST.get ( 'reg_pwd' )
	reg_inst = request.POST.get ( 'reg_inst' )
	reg_major = request.POST.get ( 'reg_major' )
	reg_grade = request.POST.get ( 'reg_grade' )
	reg_sex = request.POST.get ( 'reg_sex' )

	print(reg_name)
	print(reg_pwd)
	print(reg_inst)
	print(reg_major)
	print(reg_grade)
	print(reg_sex)

	messages.success(request,"注册成功")

	return HttpResponseRedirect('../login')
