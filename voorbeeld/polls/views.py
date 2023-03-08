from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Question


def index(req):
    print(req)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Deze vraag bestaat niet")
    return render(req, 'polls/detail.html', { 'question': question})


def results(req, question_id):
    return HttpResponse("Dit zijn de resultaten van vraag %s" % question_id)


def vote(req, question_id):
    return HttpResponse("Je stemt op vraag %s" % question_id)
