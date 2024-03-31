from rest_framework import serializers
from .models import Todo 

#serializers convert our django model into json format we can easly send it from the web
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        fields = ["id", "task", "completed"]