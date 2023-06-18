from django.contrib.auth import authenticate, login

from rest_framework import status, generics

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
        # Get the user's token
        token = request.auth

        # Delete the user's token
        if token:
            Token.objects.filter(key=token).delete()

        # Perform the logout
        logout(request)

        return Response("Logged out successfully", status=status.HTTP_200_OK)

# mahsulot filter
class MahsulotFilterlarAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot_filter.objects.all()
    serializer_class = MahsulotFilterSerializer


class MahsulotFilterAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot_filter.objects.all()
    serializer_class = MahsulotFilterSerializer




#mahsulot
class MahsulotlarAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer



class MahsulotAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer



#oluvchi uchun ipis
class OluvchilarAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer


class OluvchiAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer



#for savdo
class SavdolarAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer


class SavdoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer


# for chiqim
class ChiqimlarAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer


class ChiqimAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer


