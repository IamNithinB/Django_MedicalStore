from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.log,name='log'),
    path('signup/',views.signup,name='signup'),
    path('addMedic/',views.medCreate,name='addMedic'),
    path('medicList/',views.medList,name='medicList'),
    path('medicview/<int:id>/',views.medView,name='medicview'),
    path('medicEdit/<int:id>/',views.medEdit,name='medicedit'),
    path('medicDelete/<int:id>/',views.medDelete,name='medDelete'),
    path('logout',views.logout_view,name='logout')
    # path('')
]
