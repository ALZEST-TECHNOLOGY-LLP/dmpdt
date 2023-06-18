from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adddevicedetails/', views.adddevice, name='adddevice'),
    path('device_details/', views.device_details, name='device_details'),
    path('edit_device/<int:device_id>/', views.edit_device, name='edit_device'),
    path('delete_device/<int:pk>/', views.delete_device, name='delete_device'),
    # path('export-excel/', views.export_excel, name='export-excel'),
    path('adduser/', views.adduser, name='adduser'),
    path('userlist/', views.user_details, name='user_details'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('store-data', views.store_data, name='store_data'),
    path('selectvibdata/<int:device_id>', views.selectvibdata, name='selectvibdata'),
    path('selectgasdata/<int:device_id>', views.selectgasdata, name='selectgasdata'),
    path('selecttempadata/<int:device_id>', views.selecttempadata, name='selecttempadata'),
    path('selecthumiditydata/<int:device_id>', views.selecthumiditydata, name='selecthumiditydata'),
    path('selectflexangledata/<int:device_id>', views.selectflexangledata, name='selectflexangledata'),
    path('selectvoldata/<int:device_id>', views.selectvoldata, name='selectvoldata'),
    path('selecttempddata/<int:device_id>', views.selecttempddata, name='selecttempddata'),

]
