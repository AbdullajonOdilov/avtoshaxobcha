from django.urls import path, include
from rest_framework import routers
from .views import MahsulotFilterAPIView, MahsulotAPIView, OluvchiAPIView, SavdoAPIView, ChiqimAPIView, LoginAPIView, LogoutAPIView

router = routers.DefaultRouter()
router.register(r'mahsulot-filter', MahsulotFilterAPIView)
router.register(r'mahsulot', MahsulotAPIView)
router.register(r'oluvchi', OluvchiAPIView)
router.register(r'savdo', SavdoAPIView)
router.register(r'chiqim', ChiqimAPIView)

urlpatterns = [
    # Login URL
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls)),
]
