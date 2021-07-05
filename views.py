from django.shortcuts import render
from django.http import HttpResponse
from.models import Register

# Create your views here.

def home(request):
	return HttpResponse("gud evening to all..")

def htmltag(a):
	return HttpResponse("<h2>hi welcome to apssdc programs</h2>")


def usernameprint(request,uname):
	return HttpResponse("<h2>hi welcome <span style='color:green'>{}</span></h2>".format(uname))


def usernameage(i,un,age):
	return HttpResponse("<h2 style='text-align:center;background-color:green'> hi user <span style='color:yellow'>{}</span>and your age is: <span style='color:red'>{}</span></h2>".format(un,age))


def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('hi user{}')</script><h2 style='text-align:center;background-color:green'> hi user <span style='color:yellow'>{}</span>and your age is: <span style='color:red'>{}</span>and your id is {}</h2>".format(ename,ename,eage,eid))


def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k={'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')


def internaljs(request):
	return render(request,'html/internaljs.html',)


def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname=req.POST['uname']
		urollno=req.POST['urollno']
		uemail=req.POST.get('uemail')
		#print(uname,urollno,uemail)
		data={'username':uname,'rollno':urollno,'emailid':uemail}
		return render(req,'html/display.html',data)
		
	return render(req,'html/myform.html')


def bootstarpfun(request):
	return render(request,'html/bootstrap1.html')


def btregi(request):
	return render(request,'html/btregst.html')

def register1(request):
	name="siva"
	email="siva@gmail.com"
	reg=Register(name="siva",email="siva@gmail.com")
	reg.save()
	return HttpResponse("row insertedd successfully")