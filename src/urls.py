
from django.contrib import admin
from django.urls import path, include
from first import views1
from rest_framework.routers import DefaultRouter
from django.db import router
from django.conf.urls import include
from signin import views

router= DefaultRouter()
router.register("hr", views.UserViewSet)

urlpatterns = [

    path ("password.reset/",
    views1.PasswordReset.as_view() ,
    name="reset_password"),

    path ("password.reset/<str:encoded_pk>/<str:token>/",
    views1.ResetPassword.as_view(),
    name="reset_password"),

    path('regn/', include(router.urls)),

    path('admin/', admin.site.urls),


]
