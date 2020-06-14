from django.urls import path
from . import views
app_name = 'catalogs'

urlpatterns = [
    path('create-phone-type/', views.CreatePhoneTypeView.as_view(), name='create'),
    path('update-phone-type/<int:pk>', views.UpdatePhoneTypeView.as_view(), name='update'),
    path('delete-phone-type/<int:pk>', views.DeletePhoneTypeView.as_view(), name='delete'),
    path('phone-type/<int:pk>', views.PhoneTypeView.as_view(), name='detail'),
    path('list-phone-type/', views.PhoneTypeListView.as_view(), name='list'),
]
 