from django.urls import path 

from mytask import views

app_name = "mytask"

urlpatterns = [
	path('lista/mytask', views.listamytask, name='listamytask'),	
	path('lista/mytask/tab/<str:tab>', views.mytasktab, name='mytasktab'),
	path('lista/mytask/tab/tab/<str:tab>/<str:status>', views.mytaskpilltab, name='mytaskpilltab'),
]

