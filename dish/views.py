from .models import Dish
from .serializers import DishSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class DishAPIView(APIView):

    def get(self, request):
        try:
            paginator = PageNumberPagination()

            dishes = Dish.objects.all()
            result_page = paginator.paginate_queryset(dishes, request)
            serializer = DishSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = DishSerializer(data=request.data)
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
        
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)

            if not pk:
                return Response({
                    'success': False,
                    'message': 'method put not allowed'
                }, status=status.HTTP_404_NOT_FOUND)
            
        
            try:
                instance = Dish.objects.get(pk=pk)
            except:
                return Response({
                    'success': False,
                    'message': 'object not found'
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = DishSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'success': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)

            if not pk:
                return Response({
                    'success': False,
                    'message': 'method put not allowed'
                }, status=status.HTTP_404_NOT_FOUND)
            
        
            try:
                instance = Dish.objects.get(pk=pk)
                serializer = DishSerializer(instance)
                
                instance.delete()
            except:
                return Response({
                    'success': False,
                    'message': 'object not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            return Response({
                'success': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)