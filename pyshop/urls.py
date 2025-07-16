from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),           # 新增首頁目錄頁
    path('products/', include('products.urls')), 
]
