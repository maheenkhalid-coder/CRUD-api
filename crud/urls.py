from django.contrib import admin
from django.urls import path
from api import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Student API",
      default_version='v1',
      description="Student Register",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@abc.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>', views.StudentAPI.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
    name='schema-swagger-ui'),

]
