from rest_framework import serializers 
from .models import fr

class frSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = fr 
        fields = '__all__' 
