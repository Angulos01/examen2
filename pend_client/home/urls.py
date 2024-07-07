from django.urls import path
from home import views

app_name = "home"


urlpatterns = [
    path('pendientes/list/',views.ListPendientesView.as_view(),name="list_pend"),
    path('pendientes/create/',views.CreatePendienteView.as_view(),name="create_pend"),
    # path('v1/create/grantgoal/',views.CreateGrantGoalAPIView.as_view(),name="create_gg_api"),
    # path('v1/Detail/grantgoal/',views.DetailGrantGoalAPIView.as_view(),name="detail_gg_api"),
    # path('v1/update/grantgoal/',views.UpdateGrantGoalAPIView.as_view(),name="update_gg_api"),
    # path('v1/delete/grantgoal/',views.DeleteGrantGoalAPIView.as_view(),name="delete_gg_api"),
]