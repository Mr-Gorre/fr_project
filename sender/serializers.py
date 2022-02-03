from sender.models import Deliver, Client, Message
from rest_framework import serializers


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
