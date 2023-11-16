from rest_framework import serializers
from .models import Whiteboard

class WhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiteboard
        fields = '__all__'


class InvitationSerializer(serializers.Serializer):
    email = serializers.EmailField()