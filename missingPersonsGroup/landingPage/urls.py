'''
Authors: Megan Bates, Steven Armstrong, Kayla Tansiongco, Laura Nielson, Elise Pickett, Autumn Eaton.
Purpose: To store the routes for each page in the application.
'''
# importing urls and setting up path
from django.urls import path
from .views import indexPageView, individualPageView, resourcesPageView, databasePageView


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("home", indexPageView, name = "index"),
    path("individual", individualPageView, name = "individual"),
    path("resources", resourcesPageView, name = "resources"),
    path('database', databasePageView, name = "database")
]
