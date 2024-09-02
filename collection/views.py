from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CollectionView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Collection!"}, status=status.HTTP_200_OK)