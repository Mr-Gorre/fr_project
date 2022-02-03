# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from sender.models import Client, Message, Deliver
from sender.serializers import ClientSerializer, MessageSerializer, DeliverSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    permission_classes = [permissions.IsAuthenticated]
