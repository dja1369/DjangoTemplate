from django.urls import path
from retrieval.views import RetrievalView, admin_view, RetrievalTestView

urlpatterns = [
    path('retrieval/', RetrievalView.as_view()),
    path('retrieval/test/', RetrievalTestView.as_view()),
    path('admin/', admin_view),
]