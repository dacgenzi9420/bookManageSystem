from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class LoginView(View):
    def post(self,request):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print()
        return HttpResponse('user:{},pwd:{}'.format(user,pwd))

