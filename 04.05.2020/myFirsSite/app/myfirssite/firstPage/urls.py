from django.urls import path
from .views import *

urlpatterns = [
    path('', first),
    path('blog/', blog),
    path('about/', about),
]
