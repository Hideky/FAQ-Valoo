from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.paginator import Paginator
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from .permissions import IsPostOrIsAdminUser


def index(request):
    """Return Index View"""
    if request.method == 'GET' and 'search' in request.GET:
        questions = Question.objects.filter(answer__isnull=False, question__contains=request.GET['search'], hidden=False).order_by('date')
    else:
        questions = Question.objects.filter(answer__isnull=False, hidden=False).order_by('date')

    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    context = {
        'questions': paginator.get_page(page)
    }

    return render(request, 'mainapp/faq.html', context)


def question_form(request):
    """Return Question Form View - Send question using Rest Framework with Ajax"""
    return render(request, 'mainapp/questionform.html')


def question(request, id):
    """Return Question individual View"""
    question = get_object_or_404(Question, id=id)
    return render(request, 'mainapp/question.html', {'question':question})


def question_manager(request):
    """Return QuestionManager View - Admin only"""
    if not request.user.is_authenticated:
        return render(request, 'mainapp/notlogged.html', status=401)

    if not request.user.is_staff:
        return redirect(reverse('mainapp:index'), status=403)

    questions = Question.objects.filter().order_by('date')
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    context = {
        'questions': paginator.get_page(page)
    }
    return render(request, 'mainapp/questionmanager.html', context)


class QuestionViewSet(viewsets.ModelViewSet):
    """Question view used by Rest Framework"""
    permission_classes = (IsPostOrIsAdminUser,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer