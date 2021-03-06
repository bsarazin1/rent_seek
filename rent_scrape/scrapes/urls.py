from django.urls import path
from django.conf.urls import static, include
from . import views

urlpatterns = [
    path('', views.search, name='index'),
    path('user/', include('accounts.urls')),
    path('<int:id>/userpage', views.user_page, name='userpage'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('chart/<int:id>', views.chart, name='line_chart'),
]
