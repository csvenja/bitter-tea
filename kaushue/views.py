from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
    return render(request, 'detail.html', {
        'question': question,
        'references': references
    })


def partial(request, question_id):
    question, references = get_detail(question_id)
    return render(request, 'partial.html', {
        'question': question,
        'references': references
    })


@require_http_methods(['POST'])
@csrf_exempt
def edit(request, question_id):
    question_id = int(question_id)
    content = request.POST.get('content', None)
    question = get_object_or_404(Question, pk=question_id)
    print question
    question.content = content
    question.save()
    return HttpResponse()
