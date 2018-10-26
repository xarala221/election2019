from django.conf.urls import url
from myapp.views import *

urlpatterns = [
  url(r"^$", index, name="index"),
  url(r"^search/$", search, name="search"),
  #url(r'^import/', import_data, name="import"),
  #url(r'^handson_view/', handson_table, name="handson_view"),
  url(r'^simple_upload/', simple_upload, name="simple_upload"),
]