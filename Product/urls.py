from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.product_list),
    path('admin/', admin.site.urls),
]
