from django.urls import path
from retrieval.views import RetrievalView

urlpatterns = [
    path('retrieval/', RetrievalView.as_view()),
]