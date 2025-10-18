# esto lo hago yo !! es personal

from django.urls import path
from coder.views import index


urlpatterns = [
    path("", index, name="index"),
]