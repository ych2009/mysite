from django.shortcuts import render,get_object_or_404, render_to_response
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.template import RequestContext
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect,csrf_exempt,ensure_csrf_cookie

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name ='polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
       #  return render_to_response('polls/detail.html',
       #                            {
       #  'question': question,
       #  'error_message': "You didn't select a choice.",
       #  },
       # context_instance=RequestContext(request)
       #                            )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

