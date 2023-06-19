from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api-schema/', get_schema_view(title='Avto shahobcha api', description='Guide for the REST API',
                                        public=True, permission_classes=(AllowAny,)), name="api_schema"),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),

]

