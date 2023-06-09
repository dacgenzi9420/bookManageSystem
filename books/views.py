import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.contrib.auth import login,logout,authenticate

from books.models import Books,Record


# Create your views here.
class LoginView(View):
    def post(self,request):
        # 表单传参 可以用以下方式获取参数
        # user = request.POST.get('user')
        # pwd = request.POST.get('pwd')
        # json传参如下：（三目运算）
        parmas = request.POST if len(request.POST) else json.loads(request.body.decode())
        username = parmas.get('user')
        password = parmas.get('pwd')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return JsonResponse({'code':200,'msg':'登录成功'})
        else:
            return JsonResponse({'code': 100, 'msg': '登录失败'})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return JsonResponse({'code': 200, 'msg': '退出成功'})

class BookView(View):
    """获取图书信息"""
    def get(self,request):
        if not request.user.is_authenticated:
            return JsonResponse({'code': 200, 'msg': '未登录'})
        b = Books.objects.all()
        res = [{'id':bs.id,'name':bs.name,'status':bs.status} for bs in b]
        return JsonResponse({'code':200,'msg':'success','data':res})
    """添加图书"""
    def post(self,request):
        if not request.user.is_authenticated:
            return JsonResponse({'code': 200, 'msg': '未登录'})
        params = request.POST if len(request.POST) > 0 else json.loads(request.POST.decode())
        id = params.get('id')
        name = params.get('name')
        status = params.get('status')
        """对传入参数校验"""
        if not id and name:
            return JsonResponse({'code':8006,'msg':'图书编号或图书名称不能为空'})
        if not isinstance(id,str):
            return JsonResponse({'code': 8006, 'msg': '图书编号不能是字符串'})
        if not isinstance(name,str):
            return JsonResponse({'code': 8006, 'msg': '图书名称只能是字符串'})
        try:
            Books.objects.create(id=id, name=name, status=status)
        except Exception as e:
            return JsonResponse({'code':8005,'msg':'图书已经存在，不能重复创建'})
        else:
            return JsonResponse({'code':200,'msg':'add success'})
    """删除图书"""
    def delete(self,request):
        """先判断是否登录"""
        if not request.user.is_authenticated:
            return JsonResponse({'code': 200, 'msg': '未登录'})
        book_id = request.GET.get('id')
        if not id:
            return JsonResponse({'code':8002,'msg':'id not is null'})
        try:
            book = Books.objects.get(id=book_id)
        except Exception as e:
            return JsonResponse({'code':8002,'msg':'图书不存在'})
        else:
            book.delete()
            return JsonResponse({'code':200,'msg':'success'})

    """修改图书信息"""
def update11(request):
    if not request.user.is_authenticated:
        return JsonResponse({'code': 8006, 'msg': '未登录'})
    if request.method == 'POST':
        params = request.POST if len(request.POST) > 0 else json.loads(request.POST.decode())
        id = params.get('id')
        name = params.get('name')
        status = params.get('status')
        bookInfo = Books.objects.get(id=id)
        print(bookInfo)
        bookInfo.name = name
        bookInfo.status = status
        bookInfo.save()
        return JsonResponse({'code':200,'msg':'success'})

class RecordView(View):
    def post(self,request):
        if not request.user.is_authenticated:
            return JsonResponse({'code':8006,'msg':'未登录'})
        params = request.POST if len(request.POST) > 0 else json.loads(request.POST.decode())
        book_name = params.get('book')
        book_info = Books.objects.get(name=book_name)
        if book_info.status == 1:
            return JsonResponse({'code':200,'msg':'可借'})
        else:
            return JsonResponse('error')
