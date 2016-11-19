from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from qa.models import *
from django.views.decorators.http import require_GET

# Create your views here.
def test(request, *args, **kwords):
    return HttpResponse('OK',status=200, content_type='text/plain')

def paginate(request,qs):
    try:
        limitnum = int(request.GET.get('limit', 10))
    except ValueError:
        limitnum = 10
    if limitnum > 100:
        limitnum = 10
    try:
        pagenum = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limitnum)
    try:
        page = paginator.page(pagenum)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

#/?page=n
@require_GET
def newquestion(request):
    try:
        pagenum = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    qs = Question.objects.new()
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(pagenum)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/templates/allquestions.html', {'page': page, 'next': pagenum + 1, 'prev': pagenum - 1, 'nav': '/?page='})

#/popular/?page=n
@require_GET
def popular(request):
    try:
        pagenum = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    qs = Question.objects.popular()
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(pagenum)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/templates/popular.html', {'page': page, 'next': pagenum + 1, 'prev': pagenum - 1, 'nav': '/?page='})

#/question/n/
@require_GET
def question(request, pk):
    q = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=q)
    return render(request, 'qa/templates/question_details.html', {'question': q, 'answers': answers})
