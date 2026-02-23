from django.urls import path
from .views import register

app_name = 'registration'

urlpatterns = [
    path('', include('registration.urls')),   
    path('admin/', admin.site.urls),
]