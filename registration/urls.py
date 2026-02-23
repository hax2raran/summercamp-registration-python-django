from django.urls import path
from .views import register

app_name = 'registration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),   # changed
]