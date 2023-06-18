from django.urls import path
from .views import MahsulotFilterAPIView, MahsulotAPIView, OluvchiAPIView, SavdoAPIView, ChiqimAPIView, \
    MahsulotFilterlarAPIView, ChiqimlarAPIView, SavdolarAPIView, OluvchilarAPIView, MahsulotlarAPIView, \
    LoginAPIView, LogoutAPIView

urlpatterns = [
    # Login URL
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('mahsulot_filterlar/', MahsulotFilterlarAPIView.as_view(), name='mahsulot_filterlar'),
    path('mahsulot_filter/<int:pk>/', MahsulotFilterAPIView.as_view(), name='mahsulot_filter'),
    path('mahsulotlar/', MahsulotlarAPIView.as_view(), name='mahsulotlar'),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view(), name='mahsulot'),
    path('oluvchilar/', OluvchilarAPIView.as_view(), name='oluvchilar'),
    path('oluvchi/<int:pk>/', OluvchiAPIView.as_view(), name='oluvchi'),
    path('savdolar/', SavdolarAPIView.as_view(), name='savdolar'),
    path('savdo/<int:pk>/', SavdoAPIView.as_view(), name='savdo'),
    path('chiqimlar/', ChiqimlarAPIView.as_view(), name='chiqimlar'),
    path('chiqim/', ChiqimAPIView.as_view(), name='chiqim'),
]
