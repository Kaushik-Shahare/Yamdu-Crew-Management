from django.urls import path
from . import views
from . import views_user

urlpatterns = [
    # User Related URLs
    path('auth/createUser/', views_user.createUser, name='createUser'),
    path('getUser/', views_user.getUser, name='getUser'),
    path('auth/editUser/<int:user_id>/', views_user.editUser, name='editUser'),

    # For testing
    path('table/', views.cast_and_crew_table, name='table'),

    # Crew and Cast Related URLs
    path('crew/', views.getCrew, name='getCrew'),
    path('crew/<int:crew_id>/', views.getCrewById, name='getCrewById'),
    path('cast/', views.getCrew, name='getCast'),
    path('cast/<int:cast_id>/', views.getCrewById, name='getCastById'),
    path('assignPost/', views.assignPost, name='assignPost'),
    path('createCrewPosition/', views.emptyCrewPosition, name='createCrewPosition'),
    path('createProject/', views.createProject, name='createProject'),
    path('project/getCrew/<int:project_id>', views.getProjectCrew, name='getCrewForProject'),
    path('project/getCast/<int:project_id>', views.getProjectCast, name='getCastForProject'),
]