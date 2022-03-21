from django.urls import path
from . import views


app_name = 'diary'
urlpatterns =[
    path('index/', views.IndexView.as_view(), name='index'),
    path('diary/create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('diary/create/complete/', views.DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
    path('diary/list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary/detail/<uuid:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/update/<uuid:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/delete/<uuid:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),
]