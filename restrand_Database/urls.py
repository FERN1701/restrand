
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from restrand import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',include('restrand.urls')),
    path('reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('home')), name='password_reset_confirm'),
    path('accounts/',include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
