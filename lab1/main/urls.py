from django.urls import path, include, re_path
from django.contrib import admin
from . import views
from .views import List
from .views import *
urlpatterns = [

	re_path(r'^$', List.as_view(), name = 'list-view'),
	re_path(r'^register/$', views.RegisterFormView.as_view()),
]