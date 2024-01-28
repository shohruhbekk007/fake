from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/logout/', LogoutView.as_view(next_page='admin'), name='admin_logout'),
    path('', include('blog.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)