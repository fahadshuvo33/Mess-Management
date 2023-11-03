from django.urls import path
from mess_app import views


urlpatterns = [    
    path("", views.dashboard, name="dashboard"),
    
    path("add-bazar/",views.add_bazar, name="add_bazar"),
    path("my-bazar/",views.my_bazar, name="my_bazar"),
    path("all-bazar/",views.all_bazar, name="all_bazar"),
    path("meal-sheet/",views.meal_sheet, name="meal_sheet"),
    path("members-info/",views.members_info, name="members_info"),
    path("utilities/",views.utility, name="utility"),
]