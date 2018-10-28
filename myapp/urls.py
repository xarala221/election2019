from django.conf.urls import url
from myapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
  url(r"^$", homepage, name="home"),
  url(r'^sign_in/$', sign_in, name='login'),
  url(r'logout/$', LogoutView.as_view(), name='logout'),
  #url(r"^home/$", homepage, name="homepage"),
  url(r"^new_person/$", index, name="index"),
  url(r"^search/$", search, name="search"),
  url(r"^mon_electeur/$", mon_electeur, name="mon_electeur"),
  url(r"^get_person_info/$", get_person_info, name="get_person_info"),
  url(r"^create_person/$", create_person, name="create_person"),
]