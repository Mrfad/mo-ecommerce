from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    # query_set = Product.objects.filter(unit_price__range=(20, 30))
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.filter(collection__id=1).order_by('-title')
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

    TaggedItem.objects.get_tags_for(product, 1)

    context = {'name': 'Fady', 'tags': list(queryset)}
    return render(request, 'playground/hello.html', context)

 