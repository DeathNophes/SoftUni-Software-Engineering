from django.urls import path, include
from Frutipedia.fruits import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.CreateFruitView.as_view(), name='create_fruit'),
    path('create-category/', views.create_category, name='create_category'),
    path("<int:pk>/", include([
        path('edit-fruit/', views.edit_fruit, name='edit_fruit'),
        path('delete-fruit/', views.DeleteFruitView.as_view(), name='delete_fruit'),
        path('details-fruit/', views.detail_fruit, name='details_fruit'),
    ]))
)