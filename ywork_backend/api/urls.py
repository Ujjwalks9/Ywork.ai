from django.urls import path
from .views import Ordercreate, OrderList

urlpatterns = [
    path('orders/create/', Ordercreate.as_view()),
    path('orders/', OrderList.as_view()),
]
