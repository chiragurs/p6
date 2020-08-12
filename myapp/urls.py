from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trial/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('registration/',views.registration,name="registration"),
    path('multi/',views.multi,name="multiselect")
]