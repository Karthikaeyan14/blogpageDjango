from django.urls import path
from .import views
app_name='app'


urlpatterns = [
    path("",views.home,name="home"),
    path("post/<int:post_id>",views.value,name="value"),
     path("new_url_some",views.new_url,name="new_url"),
      path("old_url",views.old_url,name="old_url"),
        path("contact",views.contact_view,name="contact"),
         path("about",views.about,name="about"),
]
