from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Products
from .serlializers import ProductSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_products': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/delete/pk'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    item = ProductSerializer(data=request.data)

    # validating for already existing data
    if Products.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_products(request):

    # checking for the parameters from the URL
    if request.query_params:
        prod = Products.objects.filter(**request.query_params.dict())
    else:
        prod = Products.objects.all()

    # if there is something in products else raise error
    if prod:
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_product(request, pk):
    product = Products.objects.get(pk=pk)
    data = ProductSerializer(instance=product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
