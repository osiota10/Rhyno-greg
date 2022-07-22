from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('services', ServicesView.as_view(), name='services'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('testimonials', TestimonialView.as_view(), name='testimonials'),
    path('contact', contact, name='contact'),
    path('services/<slug:slug>', ServicesDetailView.as_view(), name='services-detail'),
    path('projects/<slug:slug>', ProjectsDetailView.as_view(), name='projects-detail'),
    path('projects/category/<str:cats>', projects_categories_view, name='projects-categories'),
    path('projects/all/<str:status>', ProjectStatusView.as_view(), name='projects-status'),
    path('thank-you', thank_you, name='thank-you'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('terms-and-conditions', terms_and_conditions, name='terms-and-conditions'),
]
