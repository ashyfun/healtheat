from django.urls import path

from healtheat.apps.menu.views import DailyMenuList, DailyMenuDetail

urlpatterns = [
    path('daily-menu/', DailyMenuList.as_view()),
    path('daily-menu/<int:day>/', DailyMenuDetail.as_view()),
]
