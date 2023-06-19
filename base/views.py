from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from rest_framework import status, generics, viewsets, filters
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim
from .serializers import MahsulotFilterSerializer, MahsulotSerializer, \
    OluvchiSerializer, SavdoSerializer,ChiqimSerializer


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

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


    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']



#mahsulot
class MahsulotAPIView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = MahsulotSerializer
    queryset = Mahsulot.objects.all()


    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['product_name', 'time']
    search_fields = ['product_name']

    pagination_class = PageNumberPagination
    # Set the desired page size
    page_size = 10





#oluvchi uchun ipis
class OluvchiAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Oluvchi.objects.all()
    serializer_class = OluvchiSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'time']
    search_fields = ['name']

#for savdo
class SavdoAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Savdo.objects.all()
    serializer_class = SavdoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['product__product_name', 'cost', 'oluvchi__name']
    search_fields = ['product__product_name', 'oluvchi__name']
    pagination_class = PageNumberPagination
    # Set the desired page size
    page_size = 20


# for chiqim
class ChiqimAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['time', 'money']
    search_fields = ['comment', 'person']
    pagination_class = PageNumberPagination
    # Set the desired page size
    page_size = 25

