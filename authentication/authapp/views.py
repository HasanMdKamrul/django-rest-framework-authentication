from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductSerializer

# Create your views here.


@api_view(['GET'])

def server_check(request):
    time = datetime.now().strftime("%y %m %d %H %M %S")
    message = "Server is running"
    return Response(data=message + time)

class get_products_list(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# class get_server_check(APIView):
#     def get(self,request):
#         time = datetime.now().strftime("%y %m %d %H %M %S")
#         message = "Server is running"
#         return Response(data=message + time)
    
# @csrf_exempt

# def get_data(request):
    
#     if request.method == "GET": 
#         time = datetime.now().strftime("%y %m %d %H %M %S")
#         message = "Server is running"
#         return JsonResponse(data= message + time, safe=False)