from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.http import HttpResponse
from django.views import View

from Apps.models import News
from Apps.models import User

# Create your views here.
def mainpage(request):

	#通过url得到当前登录的用户
	url = request.get_full_path()
	username = url.split('=')[-1]
	print(username)

	#得到所有新闻信息
	newslist = News.objects.all()

	return render(request,'main.html',{'newslist':newslist})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		# password = request.POST.get('password')
		return HttpResponseRedirect('../main/?'+'username='+username)

	return render(request,'login.html')
#
# #检查用户名和密码
# def checkuser(name,pwd):
#
# 	userlist = User.objects.filter(username=name,password=pwd)
#
# 	if userlist:
# 		return True
# 	return False


#得到用户注册的数据
def register(request):
	return HttpResponseRedirect('../login')

	# reg_name = request.POST.get ( 'reg_name' )
	# reg_pwd = request.POST.get ( 'reg_pwd' )
	# reg_inst = request.POST.get ( 'reg_inst' )
	# reg_major = request.POST.get ( 'reg_major' )
	# reg_grade = request.POST.get ( 'reg_grade' )
	# reg_sex = request.POST.get ( 'reg_sex' )
	#
	# print(reg_name)
	# print(reg_pwd)
	# print(reg_inst)
	# print(reg_major)
	# print(reg_grade)
	# print(reg_sex)
	#
	# if reg_name == '' or reg_pwd == '' or reg_inst == '' or reg_major == '':
	# 	messages.success(request,"输入信息有误")
	#
	# else:
	# 	user = User.objects.create(username = reg_name,password = reg_pwd,grade = reg_grade,sex = reg_sex,
	# 	                    collegail = reg_inst,major = reg_major)
	# 	if user:
	# 		messages.success(request,"注册成功")
	# 	else:
	# 		messages.success(request,"注册失败，用户已存在")


#
# class UserLogin(View):
# 	def get(self,request):
# 		return render(request,'login.html')
# 	def post(self,request):
# 		uname = request.POST.get('username','')
# 		pwd = request.POST.get('password','')
#
# 		userlist = User.objects.filter(username=uname,password=pwd)
#
# 		if userlist:
# 			return True
# 		return False

#登录连接数据库检查用户
class Checkuser( View ):
	def get(self,request):
		uname = request.GET.get('uname','')
		pwd = request.GET.get('pwd','')

		userlist = User.objects.filter(username=uname,password=pwd)

		flag = False
		if userlist:
			flag = True

		return JsonResponse({'flag':flag})

#注册调用
class Register( View ):
	def get(self,request):
		reg_name = request.GET.get('name','')
		reg_pwd = request.GET.get('pwd','')
		reg_inst = request.GET.get('inst','')
		reg_major = request.GET.get('major','')
		reg_grade = request.GET.get('grade','')
		reg_sex = request.GET.get('sex','')

		user = User.objects.create(username = reg_name,password = reg_pwd,grade = reg_grade,sex = reg_sex,
		                    collegail = reg_inst,major = reg_major)
		if user:
			messages.success(request,"注册成功")
			return JsonResponse({'flag':True})
		else:
			messages.success(request,"注册失败，用户已存在")
			return JsonResponse({'flag':False})