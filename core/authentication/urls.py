from django.urls import  path
from rest_framework.routers import SimpleRouter

from . import  views

router = SimpleRouter()
# router.register('//', view, basename="")
urlpatterns = router.urls


urlpatterns.append(path('auth/register/', views.RegisterCreateView.as_view()))
urlpatterns.append(path('auth/login/', views.LoginAPIView.as_view()))
urlpatterns.append(path('auth/profile/', views.ProfileCreateAPIView.as_view()))
