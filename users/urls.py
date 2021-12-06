from django.urls import path
from .views import SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	# path('password_reset/', reset_password, name='password_reset'),
]
