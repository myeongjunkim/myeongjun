"""Django_project_team4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


#모든 앱에 있는 뷰스 다 임포트 해오기
# from . import views

import Django_project_team4.views
import myeongjun.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Django_project_team4.views.home, name='home'),
    path('myeongjun/', include('myeongjun.urls')),
    # 각자 만든거 추가하기

]
