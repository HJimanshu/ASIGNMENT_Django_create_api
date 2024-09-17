from django.urls import path,include
from social.views import index

urlpatterns = [
    path('',index)
    ]
