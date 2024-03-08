"""FoodOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Main.views import *

urlpatterns = [
    path("" , Home , name="Home"),
    path("Category/<int:id>" , Categories , name="Category"),
    path('Product/<int:id>',Product , name="Product"),
    path("Cart", CartOrder , name="Order"),
    path("Login" , UserLogin , name="Login"),
    path("Signup" , UserSignup , name = "Signup"),
    path('Logout', UserLogout, name='Logout'), 
    path('admin/', admin.site.urls),
]
admin.site.index_title = "Project"
admin.site.site_title = "Project Admin Login"
admin.site.site_header = "Project Pannel"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
