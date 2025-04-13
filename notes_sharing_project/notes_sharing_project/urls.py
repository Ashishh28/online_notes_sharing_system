from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notes.views import home  # 👈 Import home view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 👈 Set this as homepage
    path('notes/', include('notes.urls')),  # 👈 Optional: keep all app routes
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
