from django.db import models

# Create your models here.

#新闻信息表
class News(models.Model):
	abstract = models.CharField('摘要',max_length=100,blank=False)
	date = models.DateField('发布时间',blank=False)
	link = models.CharField('网页链接',max_length=100,blank=False)
	content = models.TextField('新闻内容')
	pic_link = models.TextField('图片链接')
	category = models.CharField('所属类别',max_length=200)
	viewtimes = models.IntegerField('浏览次数',default=0)

	class Meta:
		verbose_name = '学校新闻'
		verbose_name_plural = '学校新闻'
		db_table = '学校新闻表'

	def __str__(self):
		return self.abstract

#通知公告表
class Inform(models.Model):
	abstract = models.CharField('标题',max_length=100,blank=False)
	date = models.DateField('发布时间',blank=False)
	link = models.CharField('网页链接',max_length=100,blank=False)
	content = models.TextField('通告内容')
	category = models.CharField('所属类别',max_length=200)
	viewtimes = models.IntegerField('浏览次数',default=0)

	class Meta:
		verbose_name = '通知公告'
		verbose_name_plural = '通知公告'
		db_table = '通知公告表'

	def __str__(self):
		return self.abstract

#学院新闻表
class Collegial_News(models.Model):
	abstract = models.CharField('摘要',max_length=100,blank=False)
	date = models.DateField('发布时间',blank=False)
	link = models.CharField('网页链接',max_length=100,blank=False)
	content = models.TextField('新闻内容')
	pic_link = models.TextField('图片链接')
	category = models.CharField('所属类别',max_length=200)
	viewtimes = models.IntegerField('浏览次数',default=0)
	collegial = models.CharField('所属学院',max_length=30,blank=False)

	class Meta:
		verbose_name = '学院新闻'
		verbose_name_plural = '学院新闻'
		db_table = '学院新闻表'

	def __str__(self):
		return self.abstract

#用户信息表
class User(models.Model):
	username = models.CharField('登录名',max_length=20,blank=False)
	password = models.CharField('密码',max_length=50,blank=False)
	grade = models.CharField('年级',max_length=10,blank=False)
	collegail = models.CharField('学院',max_length=30,blank=False)
	sex = models.CharField('性别',max_length=2,blank=False)
	major = models.CharField('专业',max_length=30)

	class Meta:
		verbose_name = '用户信息'
		verbose_name_plural = '用户信息'
		db_table = '用户信息表'

	def __str__(self):
		return self.username

#浏览信息表
class Browse_Record(models.Model):
	userID = models.ForeignKey(User,on_delete=models.CASCADE)
	infoID = models.CharField('信息ID',max_length=20,blank=False)
	infoCategory = models.CharField('信息类别',max_length=20,blank=False)
	viewtime = models.DateTimeField('浏览时间')
	viewduration = models.IntegerField('浏览时长')
	viewtimes = models.IntegerField('浏览次数')

	class Meta:
		verbose_name = '浏览信息'
		verbose_name_plural = '浏览信息'
		db_table = '浏览信息表'

	def __str__(self):
		return self.username