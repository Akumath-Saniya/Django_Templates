from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),

    path('tenth/', views.tenth, name='tenth'),

    # INTERMEDIATE FLOW
    path('inter/', views.inter, name='inter'),
    path('inter/groups/<year>/', views.inter_groups, name='inter_groups'),
    path('inter/subjects/<year>/<group>/', views.subjects, name='subjects'),

    path('btech1/', views.btech1, name='btech1'),

    path('content/', views.content, name='content'),
]
