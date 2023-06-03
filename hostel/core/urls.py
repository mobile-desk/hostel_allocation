from django.contrib import admin
from django.urls import path, include
from hostel import settings
from . import views
from .views import allocate_hostel
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    path('create-profile', views.create_profile, name="create_profile"),
    path('allocate-hostel/', allocate_hostel, name='allocate_hostel'),
]


urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)