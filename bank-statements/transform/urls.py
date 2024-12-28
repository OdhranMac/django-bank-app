from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.display_page),
    # path('transform/', views.display_page),
    # path('?mybtn=Click#', views.post_to_azure),
    # path('run/', views.display_running)
]