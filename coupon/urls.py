from django.urls import path
from . import views

urlpatterns = [
    # path("", views.profile, name="profile"),
    path("add_coupon/<code>", views.add_coupon, name="add_coupon"),
]