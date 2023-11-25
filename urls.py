from django.urls import path 

from mytask import views

app_name = "mytask"

urlpatterns = [
	path('lista/mytask', views.listamytask, name='listamytask'),	
	# path('lista/mytask/tab/<str:tab>', views.mytasktab, name='mytasktab'),
	# path('lista/mytask/tab/leave/', views.mytasktableave, name='leave'),
	# path('lista/mytask/tab/tab/<str:tab>/<str:status>', views.mytaskpilltab, name='mytaskpilltab'),
	path('lista/mytask/leave/<str:status>', views.leavestatus, name='leavestatus'),
	path('lista/mytask/travel/<str:status>', views.travelstatus, name='travelstatus'),
]

