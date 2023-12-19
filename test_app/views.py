from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
from .models import Redirect, redirect_post_save
from .forms import CreateNewUser

# Create your views here.

def index(request):
    if request.method=="GET":
        title = "Test Redirect"
        #user = Redirect.objects.create()

        data = Redirect.objects.all()
        return render(request, "index.html", {"title":title, "data":data, "form":CreateNewUser})
    else:
        user = Redirect.objects.create()
        print(user)
        title = "Test Redirect"

        data = Redirect.objects.all()
        return render(request, "index.html", {"title":title, "data":data, "form":CreateNewUser})

class GetUrlView(View):
    def get(self, request, *args, **kwargs):
        key = request.GET.get('key')
        data = cache.get(key)
        if data:
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "Key not found"}, status=404)