from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim
from .serializers import MahsulotFilterSerializer, MahsulotSerializer, OluvchiSerializer, SavdoSerializer, ChiqimSerializer

class MahsulotFilterAPIView(APIView):
    def get(self, request):
        filters = Mahsulot_filter.objects.all()
        serializer = MahsulotFilterSerializer(filters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotFilterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MahsulotAPIView(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OluvchiAPIView(APIView):
    def get(self, request):
        oluvchilar = Oluvchi.objects.all()
        serializer = OluvchiSerializer(oluvchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OluvchiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavdoAPIView(APIView):
    def get(self, request):
        savdolar = Savdo.objects.all()
        serializer = SavdoSerializer(savdolar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavdoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChiqimAPIView(APIView):
    def get(self, request):
        chiqimlar = Chiqim.objects.all()
        serializer = ChiqimSerializer(chiqimlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChiqimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
