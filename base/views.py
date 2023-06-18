from rest_framework import generics
from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim
from .serializers import MahsulotFilterSerializer, MahsulotSerializer, OluvchiSerializer, SavdoSerializer, ChiqimSerializer


class MahsulotFilterlarAPIView(generics.ListCreateAPIView):
    queryset = Mahsulot_filter.objects.all()
    serializer_class = MahsulotFilterSerializer

class MahsulotFilterAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot_filter.objects.all()
    serializer_class = MahsulotFilterSerializer


class MahsulotlarAPIView(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer

class MahsulotAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer

#oluvchi uchun ipis
class OluvchilarAPIView(generics.ListCreateAPIView):
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer

class OluvchiAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer


class SavdolarAPIView(generics.ListCreateAPIView):
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer

class SavdoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer


class ChiqimlarAPIView(generics.ListCreateAPIView):
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer

class ChiqimAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer

