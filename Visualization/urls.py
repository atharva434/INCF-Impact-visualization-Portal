from django.contrib import admin
from django.urls import path,include
from Visualization import views

urlpatterns = [
    path("adminpage",views.adminpage,name="adminpage"),
    path("",views.homepage,name="homepage"),
    path("total",views.total_impact),
    path("org",views.organization),
    path("detail/<int:id>",views.detail),
    path("chatbot",views.chatbot, name="chatbot"),
    path("get_qa_model", views.get_qa_model, name='get_qa_model'),
    path("upload",views.upload, name="upload"),
    path("add/<int:id>",views.add),
    path("search", views.search_view, name='search'),
    # path("project/<int:id>/", views.ProjectDetailView.as_view(), name='project_detail'),
    path("fproject/<int:id>/", views.FProjectDetailView.as_view(), name='fproject_detail'),
    path("publication/<int:id>/", views.PublicationDetailView.as_view(), name='publication_detail'),
    path("country_collab", views.country_collab, name='country_collab'),
    path("world_collab", views.world_collab, name='world_collab'),
    path("get_names_by_country/<str:country>/", views.get_names_by_country, name='get_names_by_country'),
    # path("publication_counts/", views.publication_count, name='publication_counts'),
    path('all_publications/', views.all_publications, name='all_publications'),
    path("publications", views.publications, name='publications'),
    path('fprojects/', views.get_fprojects_data, name='get_fprojects_data'),
    path('viz_fprojects', views.viz_fprojects, name='viz_fprojects')
]