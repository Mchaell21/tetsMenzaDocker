from django.urls import path
from bagianVisitor import views

urlpatterns = [
    path('contact/', views.contact, name='contactPage'),
    path('updates/', views.update, name='updatePage'),
    path('payment/', views.payment, name='paymentPage'),
    path('service/', views.service, name='servicePage'),
]