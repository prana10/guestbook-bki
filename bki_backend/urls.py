from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from tamu.views import PageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageView.index, name="index"),
    path('upload', PageView.upload, name="upload"),
    path('success/', PageView.success, name="success"),
]

admin.site.title = "PT.Biro Klasifikasi Indonesia | Dashboard Admin Guestbook"
admin.site.site_header = "BKI Administration"
admin.site.index_title = "Dashboard Admin PT.Biro Klasifikasi Indonesia"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)