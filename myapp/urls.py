from django.conf.urls import url
from myapp.views import *

urlpatterns = [
  url(r"^$", home, name="home"),
  url(r"^new_person/$", index, name="index"),
  url(r"^search/$", search, name="search"),
  url(r"^mon_electeur/$", mon_electeur, name="mon_electeur"),
  url(r"^get_person_info/$", get_person_info, name="get_person_info"),
  url(r"^create_person/$", create_person, name="create_person"),
  #url(r'^import/', import_data, name="import"),
  #url(r'^handson_view/', handson_table, name="handson_view"),
  url(r'^simple_upload/', simple_upload, name="simple_upload"),
]