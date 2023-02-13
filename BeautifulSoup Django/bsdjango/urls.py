from django.contrib import admin
from django.urls import path, include
# importing from app folder, the view file
from .views import list_scrap

urlpatterns = [
    path('admin/', admin.site.urls),
    # for the home function in the view file
    path('', list_scrap, name="list_scrap"),
    # for the create function in the view file
    

]

