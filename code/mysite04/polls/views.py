from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    var = 'electioary'
    template=loader.get_template('polls/index.html')
    context = {
        'various':var,
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    return HttpResponse("user %s" % question_id)
 
def result(request, question_id):
    return HttpResponse("result %s" % question_id)
  
def message(request, message_str):
    return HttpResponse("message: %s" % message_str)
