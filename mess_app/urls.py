from django.urls import path
from mess_app import views


urlpatterns = [    
    path("", views.summary, name="home"),
    
    path("summary/",views.summary, name="summary"),
    path("add-bazar/",views.add_bazar, name="add_bazar"),
    path("bazar-report/",views.bazar_report, name="bazar_report"),
    path("meal-report/",views.meal_report, name="meal_report"),
    path("members-info/",views.members_info, name="members_info"),
]