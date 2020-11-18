from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, Choice

def index(request):
    question_list = Question.objects.order_by('published')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, id):
    try: question = Question.objects.get(pk=id)
    except Question.DoesNotExit: raise Http404("Question not found")
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try: selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Select a choice'})
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'polls/results.html', {'question': question})