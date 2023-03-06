from django.urls import re_path
from . import views

urlpatterns = [

	re_path(r'^login/$', views.LoginFormView.as_view()),
	re_path(r'^logout/$', views.LogoutView.as_view()),
	re_path(r'^$', views.MainView.as_view()),
]