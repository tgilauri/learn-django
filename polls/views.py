from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


# Create your views here.

def index(request):
    questions = Question.objects.order_by("-pub_date")[:5]
    output = "<br/>".join([q.question_text for q in questions])
    return HttpResponse(output)


def detail(request, question_id):
    print(type(question_id))
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're vote for question %s" % question_id)
