from django.urls import path
from django.conf.urls import url
from backend.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("deatails",views.UserDetail)
urlpatterns=[]

urlpatterns+=router.urls