from django.shortcuts import get_object_or_404, render
from kaushue.models import Page


def index(request):
    page_list = Page.objects.all()
    context = {'page_list': page_list}
    return render(request, 'index.html', context)


def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'detail.html', {'page': page})
