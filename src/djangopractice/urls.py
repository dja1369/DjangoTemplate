from django.urls import path

from . import views

app_name = 'djangopractice'

urlpatterns = [
    # path('', views.index), # 오리지날 방법
    path('', views.index, name='index'), # alias 활용
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create')
]
