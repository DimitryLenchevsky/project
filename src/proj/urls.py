"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from testapp.views import Test, CreateGenre, UpdateGenre, ListGenre, DeleteGenre, DetailGenre
from django.conf import settings
from django.conf.urls.static import static
from products.auth_views import MyLogin, MyPasswordChangeView

#from catalogs import urls as catalogs_urls

# http://127.0.0.1:8000/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/<int:pk>', Test.as_view()),
    path('mega-create-genre/', CreateGenre.as_view(), name='create-genre'),
    path('update-genre/<int:pk>', UpdateGenre.as_view(), name='update-genre'),
    path('list-genre/', ListGenre.as_view()),
    path('genre-type/<int:pk>', DetailGenre.as_view(), name='genre-type'),
    path('delete-genre/<int:pk>', DeleteGenre.as_view()),
    path('catalogs/', include('catalogs.urls', namespace='catalogs')),
    path('checkout/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('', include('landing.urls', namespace='landing')),
    path('', include('products.urls', namespace='products')),
    path('', include('orders.urls', namespace='orders')),
    path('login/', MyLogin.as_view(), name='login'),
    path('change-password/', MyPasswordChangeView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
