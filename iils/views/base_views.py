from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'iils/question_list.html', context)
    #return HttpResponse("통합정보연계시스템 Test Site #1")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'iils/question_detail.html', context)



