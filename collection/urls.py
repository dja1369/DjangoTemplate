from django.urls import path
from collection.views import CollectionView

urlpatterns = [
    path('collection/', CollectionView.as_view()),
]