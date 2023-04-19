from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reqeust: str):
    return HttpResponse("나의 첫번째 장고 프로젝트!")


