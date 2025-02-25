
from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing

urlpatterns = [
    path('',views.home,name = 'home'),
    path('recommend/',views.recommend,name = 'recommend'),
    path('recommend/form/1/',views.form1,name = 'form1'),
    path('recommend/form/2/',views.form2,name = 'form2'),
    path('result/',views.result,name = 'result'),
    path('subjects/',views.check_subjects,name = 'check_subjects'),
    path('pre_search/',views.pre_search,name = 'pre_search'),
    #=============================================================================
    path('signin/',views.signin,name = 'signin'),
    path('logout/',views.exit_account,name = 'exit_account'),
    path('create/',views.createaacount,name = 'createaacount'),
    path('verify/account/',views.verify_email,name = 'verify_email'),
    path('reset/',views.resetpassword,name = 'resetpassword'),
    path('renew/password/',views.renewpassword,name = 'renewpassword'),
    #=============================================================================
    path('administrator/',views.administrator,name = 'administrator'),
    path('settings/',views.settings,name = 'settings'),
    path('settings/team/<int:pk>/delete/',views.delete_team,name = 'delete_team'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
