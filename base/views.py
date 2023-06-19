from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from rest_framework import status, generics, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim
from .serializers import MahsulotFilterSerializer, MahsulotSerializer, \
    OluvchiSerializer, SavdoSerializer,ChiqimSerializer


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.auth
        if token: Token.objects.filter(key=token).delete()
        logout(request)

        return Response("Logged out successfully", status=status.HTTP_200_OK)


# mahsulot filter
class MahsulotFilterAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot_filter.objects.all()
    serializer_class = MahsulotFilterSerializer


#mahsulot
class MahsulotAPIView(viewsets.ModelViewSet):
    serializer_class = MahsulotSerializer
    queryset = Mahsulot.objects.all()
    permission_classes = [IsAuthenticated]



#oluvchi uchun ipis
class OluvchiAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer



#for savdo
class SavdoAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer


# for chiqim
class ChiqimAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer


