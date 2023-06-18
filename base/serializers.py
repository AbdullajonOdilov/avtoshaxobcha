from rest_framework import serializers
from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim

class MahsulotFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot_filter
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class OluvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oluvchi
        fields = '__all__'

class SavdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savdo
        fields = '__all__'

class ChiqimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chiqim
        fields = '__all__'
