from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("details/<int:id>", views.listing, name="listing"),
    path("close/<int:id>", views.closeAuction, name="close"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("removeWatch/<int:p_id>", views.removeWatch, name="removeWatch"),
    path("addWatch/<int:p_id>", views.addWatch, name="addWatch"),

]
