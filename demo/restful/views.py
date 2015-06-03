from django.contrib.auth.models import User, Group
from restful.models import Order
from rest_framework import viewsets
from restful.serializers import UserSerializer, GroupSerializer, OrderSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑order的 API endpoint
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



