from django.urls import path, include
from rest_framework import routers
from .views import LoginAPIView, ChangeUsernamePasswordAPIView, LogoutAPIView, MahsulotFilterAPIView, MahsulotAPIView, OluvchiAPIView, SavdoAPIView, ChiqimAPIView

router = routers.DefaultRouter()
router.register(r'chiqim', ChiqimAPIView)
router.register(r'mahsulot', MahsulotAPIView)
router.register(r'mahsulot-filter', MahsulotFilterAPIView)
router.register(r'oluvchi', OluvchiAPIView)
router.register(r'savdo', SavdoAPIView)

urlpatterns = [
    # Login URL
    path('login/', LoginAPIView.as_view(), name='login'),
    path('change-user/', ChangeUsernamePasswordAPIView.as_view(), name='change'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls)),
]
