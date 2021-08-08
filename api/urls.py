from django.urls import path
from .views.client_views import Clients, ClientDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('clients/', Clients.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password')
]
