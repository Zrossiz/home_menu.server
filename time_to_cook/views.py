from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import TimeToCookSerializer

class CreateTimeToCookAPIView(APIView):

    def post(self, request):
        try:
            serializer = TimeToCookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'success': True,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)