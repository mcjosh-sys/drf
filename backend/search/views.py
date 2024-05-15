from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from . import client

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        params = {}
        if request.user.is_authenticated:
            user = request.user.username
            params['user'] = user
        query = request.GET.get('q')
        tags = (request.GET.get('tags') if request.GET.get('tags') else '').split(',')
        if tags: 
            params['tags'] = tags
        public = request.GET.get('public')
        if public and public.lower() in ['true','false']:
            params['public'] = public.lower() == 'true'
        if not query:
            return Response('', status=400)
        print(params)
        results = client.perform_search(query, **params)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
