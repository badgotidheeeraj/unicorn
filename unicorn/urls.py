from django.contrib import admin
from django.urls import path,include
from myapp import views
from unicorn.components.chandu import ChanduView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path("", views.index,name="index"),   
]

from django.urls import path

urlpatterns = [
    path("book", ChanduView.as_view(), name="book"),
]
