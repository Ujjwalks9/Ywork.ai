from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

class Ordercreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):  
        title = self.request.query_params.get('title')
        queryset = Order.objects.filter(user=self.request.user)
        if title:
            queryset = queryset.filter(title__icontains=title)  
        return queryset
