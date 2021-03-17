from django.shortcuts import render,redirect
from django.views import View
from .models import *


class Index(View):
    def get(self, request):
        return render(request, 'bike/index.html', {})

    def post(self, request):
        pass


class Login(View):
    def get(self, request):
        if 'user' in request.session:
            return redirect('/dashboard/',{'loggedin':True})

        return render(request, 'bike/login.html', {'error': ''})

    def post(self, request):
        email_or_mobile = request.POST.get('username',None)
        password = request.POST.get('password',None)
        data = BikeUser.objects.filter(email=email_or_mobile,password=password).get()
        if data:
            request.session['user'] ={ 'id':data.id,'email':data.email,'name':data.name,'mobile':data.mobile}
            return redirect('/dashboard/',{'loggedin':True})
        return render(request,'bike/login.html',{'error':'user id or password is incorrect'})


class Sign(View):
    def get(self, request):
        return render(request, 'bike/sign.html', {})

    def post(self, request):
        name=request.POST.get('name',None)
        email = request.POST.get('email', None)
        mobile = request.POST.get('mobile', None)
        password= request.POST.get('password', None)
        data_model= BikeUser(name=name,email=email,mobile=mobile,password=password)
        data_model.save()
        return render(request,'bike/sign.html')


class Dashboard(View):


    def get(self, request):
       # import pdb
        #pdb.set_trace()
        if 'user' in request.session:
            return render(request,'bike/dashboard.html',{'user':request.session['user'],'loggedin':True})
        return redirect('/login/',{'error':'please login first','loggedin':True})

    def post(self, request):
        email_or_mobile = request.POST.get('username',None)
        password =request.POST.get('password',None)
        data = BikeUser.object.filter(email=email_or_mobile,password=password).get()
        if data:
            request.session['user']={'id':data.id , 'name': data.name,'email':data.email,'mobile':data.mobile}
            return render(request,'bike/dashboard.html',{'user':data})
        return render(request,'bike/login.html',{'error': 'user id or password is incorrect '})


class Logout(View):
    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        return redirect('/', {'error': 'Logout successful'})