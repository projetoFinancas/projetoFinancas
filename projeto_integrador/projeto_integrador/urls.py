from django.contrib import admin
from django.urls import include, path
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pagina/', views.index, name='pagina'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('database/', include('database.urls')), 
]
