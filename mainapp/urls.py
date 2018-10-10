from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .models import Question
from rest_framework import routers
from mainapp import views

app_name = 'mainapp'

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('questionform', views.question_form, name='questionform'),
    path('questionreceiver', views.question_receiver, name='questionreceiver'),
    path('questionmanager', views.question_manager, name='questionmanager'),
    path('question/<int:id>', views.question, name='question'),
    path('login', auth_views.LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]