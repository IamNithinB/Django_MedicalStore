
from django.urls import path,include
from .import views

urlpatterns = [
    path('simpleapi',views.simpleapi,name='simple_api'),
    path('login',views.login,name="login_api"),
    path('signup',views.signup,name="signup_api"),
    path('postMedic',views.postMedic,name='postMedic_api'),
    path('getMedic',views.getMedic,name='getMedic'),
    path('editMedic/<int:id>',views.editMedic,name='editMedic_api'),
    path('deleteMedic/<int:id>/',views.delete,name='deleteMedic_api'),
    path('viewMedic/<int:id>',views.viewMedic,name="viewMedic_api")
]

