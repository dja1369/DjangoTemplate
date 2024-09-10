from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from mongoengine import QuerySetManager
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from retrieval.models import TestModel


# Create your views here.
class RetrievalView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Retrieval!"}, status=status.HTTP_200_OK)

class RetrievalTestView(APIView):
    def get(self, request):
        query_set: QuerySetManager = TestModel.objects.all()
        return Response({"message": "Hello, Retrieval Test!", "data List": query_set.to_json()}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        test = TestModel(**data).save()
        return Response({"message": "Hello, Retrieval Test!", "data": test.to_json()}, status=status.HTTP_200_OK)


def admin_view(request):
    model = {"name": "test", "age": 10}
    return render(request, "admin/test_model_change_list.html" , model)