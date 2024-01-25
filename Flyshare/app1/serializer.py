from app1.models import PostModel
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class PostModelSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'

# class ChatMessageSerializer(ModelSerializer):
#     class Meta:
#         model = ChatMessage
#         fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'