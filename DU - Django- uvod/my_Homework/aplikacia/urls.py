from django.urls import path
from .views import (home, about, contact, members, members_detail)


urlpatterns = [
    path('', home, name="home_name"),
    path('about/', about, name="about_name"),
    path('contact/', contact, name="contact_name"),
    path('members_list/', members, name="members_name"),
    path('members_detail/', members_detail, name="members_detail"),
]