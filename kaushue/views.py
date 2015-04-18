from django.shortcuts import get_object_or_404, render
from kaushue.models import Question


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})
