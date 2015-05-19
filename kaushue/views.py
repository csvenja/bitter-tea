# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from kaushue.models import Question, Connection


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def get_detail(question_id):
    question = get_object_or_404(Question, pk=question_id)
    references = []
    for reference in question.reference.all():
        r = {
            'id': reference.id,
            'title': reference.title,
            'logic': Connection.objects.get(
                from_question=question_id,
                to_question=reference.id
            ).logic
        }
        references.append(r)
    return question, references


def detail(request, question_id):
    question, references = get_detail(question_id)
    question_list = Question.objects.all()
    return render(request, 'detail.html', {
        'question': question,
        'references': references,
        'question_list': question_list,
    })


def partial(request, question_id):
    question, references = get_detail(question_id)
    question_list = Question.objects.all()
    return render(request, 'partial.html', {
        'question': question,
        'references': references,
        'question_list': question_list,
    })


@require_http_methods(['GET'])
@csrf_exempt
def get_questions(request):
    question_list = Question.objects.all()
    resp = {}
    for question in question_list:
        resp[question.id] = question.title
    return JsonResponse(resp)


@require_http_methods(['POST'])
@csrf_exempt
def edit(request, question_id):
    question_id = int(question_id)
    content = request.POST.get('content', None)
    question = get_object_or_404(Question, pk=question_id)
    question.content = content
    question.save()
    return HttpResponse()


@require_http_methods(['POST'])
@csrf_exempt
def add_link(request):
    from_id = int(request.POST.get('from_id'))
    to_id = int(request.POST.get('to_id'))
    logic = request.POST.get('logic', None)
    Connection.objects.create(
        from_question=Question.objects.get(pk=from_id),
        to_question=Question.objects.get(pk=to_id),
        logic=logic)
    return HttpResponse()


@require_http_methods(['POST'])
@csrf_exempt
def remove_link(request):
    from_id = int(request.POST.get('from_id'))
    to_id = int(request.POST.get('to_id'))
    Connection.objects.get(
        from_question=Question.objects.get(pk=from_id),
        to_question=Question.objects.get(pk=to_id)
    ).delete()
    return HttpResponse()


def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Question.objects.create(title=title, content=content)
            return redirect('/')
        else:
            return render(request, 'new.html', {
                'title': title,
                'content': content,
                'error': '请填写标题和内容'
            })
