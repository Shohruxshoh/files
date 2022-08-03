from django.urls import path
from .views import home, FilesCreateVeiw, FilesListView, FilesUpdateView, FilesDeleteView, FilesDetailView, SignUpView, logout_view


urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('create/', FilesCreateVeiw.as_view(), name='create'),
    path('view/', FilesListView.as_view(), name='view'), 
    path('detail/<int:pk>', FilesDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', FilesUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', FilesDeleteView.as_view(), name='delete'),
]
