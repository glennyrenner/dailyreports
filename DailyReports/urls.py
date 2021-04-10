"""DailyReports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('cdd/', cdd, name="cdd"),
    path('medic/', medic, name="medic"),
    path('prev/', prev, name="prev"),
    path('adv/', adv, name="adv"),
    path('env/', env, name="env"),
    path('interv/', interv, name="interv"),

    path('adv/submit', submit_adv, name='submit-adv-report'),
    path('prev/submit', submit_prev, name='submit-prev-report'),
    path('medic/submit', submit_medic, name='submit-medic-report'),
    path('interv/submit', submit_interv, name='submit-interv-report'),
    path('env/submit', submit_env, name='submit-env-report'),
]
