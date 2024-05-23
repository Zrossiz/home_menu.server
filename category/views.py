from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer

class CreateCategoryAPIView(CreateAPIView):
    def post(self, request):
        try:
            data = request.data

            serializer = CategorySerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            
            return Response({
                'success': True,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)