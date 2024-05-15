from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
import json
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # model_data = Product.objects.all().order_by("title").first()
    # data = {}
    # if model_data:
    #     # data = model_to_dict(model_data, fields=['id','title','content','price'])
    #     data = ProductSerializer(instance=model_data).data
    """
    DRF API View
    """
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)