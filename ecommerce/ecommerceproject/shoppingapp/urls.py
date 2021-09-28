from django.urls import path
from . import views
app_name = 'shoppingapp'
urlpatterns = [
                    path('', views.Cproduct, name='Cproduct'),
                    path('<slug:c_slug>/', views.Cproduct, name='productscat'),
                    path('<slug:c_slug>/<slug:p_slug>/', views.pDetail, name='pcDetail')
]