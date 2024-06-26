from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name ='products:detail',
        lookup_field = 'pk',
        read_only = True
        )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='products:detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # name= serializers.CharField(source='title', read_only=True)
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
        ]
        
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value) #iexact -> case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists.")
    #     return value
        
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
    
    def get_my_user_data(self, obj):
        return {'username':obj.user.username}
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("products:edit",kwargs={"pk":obj.pk}, request=request)
    def get_my_discount(self, obj):
        if not (hasattr(obj, 'id') or isinstance(obj, Product)):
            return None
        
        return obj.get_discount()