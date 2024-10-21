from django.urls import path
from logAuth import views

urlpatterns = [
    path('login/', views.logPage, name='loginPage'),
    path('session_log/', views.sess_login, name='sesLog'),
    path('logout/', views.logout_page, name='logout'),
    path('homeadmin/', views.home, name='homePageAdmin'),
    path('contact list/', views.contactList, name='contactListPage'),
    path('contact/delete/<slug:slug>/', views.deleteContact, name='deleteContact'),
    path('postService/', views.postService, name='postService'),
    path('enable_image/<int:pk>/', views.enable_image, name='enable_image'),
    path('disable_image/<int:pk>/', views.disable_image, name='disable_image'),
    path('toggle_image_status/<int:pk>/', views.toggle_image_status, name='toggle_image_status'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('create-post/', views.create_post_view, name='create_post'),
    path('listPost/', views.listPost, name='listPost'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('toggle_image_status/', views.toggle_image_status, name='toggle_image_status'),
    path('logoList/', views.postLogo, name='postLogo'),
    path('enable_logo/<int:pk>/', views.enable_logo, name='enable_logo'),
    path('disable_logo/<int:pk>/', views.disable_logo, name='disable_logo'),
    path('toggle_logo_status/<int:pk>/', views.toggle_logo_status, name='toggle_logo_status'),
    path('delete_logo/<int:pk>/', views.delete_logo, name='delete_logo'),
]