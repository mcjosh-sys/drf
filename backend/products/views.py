from rest_framework import authentication, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user, content=content)
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     # print(request.user)
    #     return qs.filter(user=request.user)

class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin, 
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            serializer.save(content=instance.title)
    
            
class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ProductMixinView(
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            serializer.save(content=instance.title)
            
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
product_list_create_view = ProductListCreateAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_list_view = ProductListAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_destroy_view = ProductDestroyAPIView.as_view()
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
        method = request.method
        
        if method == 'GET':
            if pk is not None:
                #detail view
                # queryset = Product.objects.filter(pk=pk)
                # if not queryset.exists():
                #     return Http404
                obj = get_object_or_404(Product, pk=pk)
                data = ProductSerializer(obj, many=False).data
                return Response(data)
            #list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
            
            
        if method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                title = serializer.validated_data.get('title')
                content = serializer.validated_data.get('content') or None
                if content is None:
                    content = title
                serializer.save(content=content)
                return Response(serializer.data)
    
