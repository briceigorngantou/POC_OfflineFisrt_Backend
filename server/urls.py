from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('all/', views.view_products, name='view_products'),
    path('sync/', views.synch_data, name='synch_data'),
    path('create/', views.add_items, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]
