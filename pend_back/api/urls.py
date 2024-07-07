from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path('pendientes/list/',views.ListPendienteAPIView.as_view(),name="list_pend_api"),
    path('pendientes/create/',views.CreatePendienteAPIView.as_view(),name="create_pend_api"),
    path('pendientes/update/<int:pk>',views.UpdatePendienteAPIView.as_view(),name="update_gg_api"),
    path('pendientes/delete/<int:pk>',views.DeletePendienteAPIView.as_view(),name="delete_gg_api"),
]