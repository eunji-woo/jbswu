from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings

# app_name = 'qna'

urlpatterns = [
    path('writepage/', views.writepage, name='writepage'),
    path('admin/', admin.site.urls, name='admin'),
    path('create/', views.create, name='create'),
    path('detail/<int:write_id>/delete', views.detail, name='detail'),
    # path('detail/<int:pk>/delete/', views.board_delete, name='broad_delete'),
    path('delete/<int:write_id>', views.delete, name="delete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)