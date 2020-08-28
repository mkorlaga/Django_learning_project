from django.urls import path
from .views import CustomProfileView, ProfileOverview
from users import views as user_view

# /profile/
urlpatterns = [
    # path('', user_view.profile, name='profile'),
    path('', ProfileOverview.as_view(template_name='users/profile.html'), name='profile'),
    path('<str:username>/', CustomProfileView.as_view(template_name='users/custom_profile.html'), name='custom-profile')
]
