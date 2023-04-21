from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Question, Answer

from django.http import HttpResponse


# Create your views here.
# def index(request: str):
#     return HttpResponse("나의 첫번째 장고 프로젝트!")

def index(request: str):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'djangopractice/question_list.html', context)


def detail(request: str, question_id: int):
    # question = Question.objects.get(id=question_id) # 정상 출력
    question = get_object_or_404(Question, pk=question_id)  # 없을 경우 404 에러 리턴
    context: Question = {'question': question}
    return render(request, 'djangopractice/question_detail.html', context)


def answer_create(request: str, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now()) # 연결된 키를 사용 하여 접근
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now()) # 모델에 접근해 생성
    answer.save()

    return redirect('djangopractice:detail', question_id=question_id)
