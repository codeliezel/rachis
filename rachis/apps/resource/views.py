from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resource
from .serializers import ResourceSerializer

class ResourceView(APIView):

    """
    Create a single link resource
    """
    
    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Get all link resources
    """

    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)