from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.product_list_create_view, name='list'),
    path('<int:pk>/', views.product_detail_view, name="detail"),
    path('<int:pk>/update/', views.product_update_view, name='edit'),
    path('<int:pk>/delete/', views.product_destroy_view),
]
