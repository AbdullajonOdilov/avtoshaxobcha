from django.urls import path
from .views import MahsulotFilterAPIView, MahsulotAPIView, OluvchiAPIView, SavdoAPIView, ChiqimAPIView

urlpatterns = [
    path('mahsulot_filter/', MahsulotFilterAPIView.as_view(), name='mahsulot_filter'),
    path('mahsulot/', MahsulotAPIView.as_view(), name='mahsulot'),
    path('oluvchi/', OluvchiAPIView.as_view(), name='oluvchi'),
    path('savdo/', SavdoAPIView.as_view(), name='savdo'),
    path('chiqim/', ChiqimAPIView.as_view(), name='chiqim'),
]
