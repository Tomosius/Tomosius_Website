# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
import views  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add this line for the index page

    # Add more apps here
]