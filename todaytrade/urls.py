"""todaytrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todaytrade import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact-us', views.contact),
    path('about-us', views.about),
    path('course_register', views.course_registration),
    path('courses', views.courses),
    path('dii', views.dii),
    path('explore', views.explore),
    path('investor', views.investor),
    path('IPO', views.IPO),
    path('live_course', views.live_course),
    path('signin', views.login),
    path('logout', views.logout),
    path('MCX', views.MCX),
    path('news', views.news),
    path('service', views.service),
    path('premium_registration', views.premium_registration),
    path('premium-services', views.premium_services),
    path('sectors', views.sectors),
    path('signup', views.signup),
    path('stocks', views.stocks),
    path('trendingstock', views.trendingstock),
    path('ii', views.intraday),
    path('Dashboard',views.Secret),
    path('traders/<id>',views.traders),
    path('traders1_13/<id>',views.traders1_13),
    path('traders1_16/<id>',views.traders1_16),
    path('traders1_17/<id>',views.traders1_17),
    path('traders1_18/<id>',views.traders1_18),
    path('traders1_19/<id>',views.traders1_19),
    path('traders1_20/<id>',views.traders1_20),
    path('traders1_21/<id>',views.traders1_21),
    path('traders1_22/<id>',views.traders1_22),
    path('traders1_23/<id>',views.traders1_23),
    path('traders1_24/<id>',views.traders1_24),
    path('traders1_25/<id>',views.traders1_25),
    path('traders1_26/<id>',views.traders1_26),
    path('traders1_27/<id>',views.traders1_27),
    path('traders1_28/<id>',views.traders1_28),
    path('traders1_29/<id>',views.traders1_29),
    path('traders1_30/<id>',views.traders1_30),
    path('traders1_31/<id>',views.traders1_31),
    path('traders1_32/<id>',views.traders1_32),
    path('traders1_33/<id>',views.traders1_33),
    path('traders1_34/<id>',views.traders1_34),
    path('traders1_35/<id>',views.traders1_35),
    path('traders1_36/<id>',views.traders1_36),
    path('traders1_37/<id>',views.traders1_37),
    path('traders1_38/<id>',views.traders1_38),
    path('traders1_39/<id>',views.traders1_39),
]
