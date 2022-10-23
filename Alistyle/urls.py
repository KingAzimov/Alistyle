from django.conf.urls.static import static
from asosiyapp.views import Home2View
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home2View.as_view(), name='home2'),
    path('', include('userapp1.urls')),
    path('buyurtma/', include('buyurtmaapp.urls')),
    path('asosiy/', include('asosiyapp.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
