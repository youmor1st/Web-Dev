from django.urls import path
from . import views

urlpatterns = [
    # Company URLs
    path('companies/', views.CompanyListCreateAPIView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:id>/vacancies/', views.CompanyVacanciesList.as_view(), name='company-vacancies'),

    # Vacancy URLs
    path('vacancies/', views.VacancyList.as_view(), name='vacancy-list'),
    path('vacancies/create/', views.VacancyListCreateAPIView.as_view(), name='vacancy-create'),
    path('vacancies/<int:pk>/', views.VacancyDetail.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', views.TopTenVacanciesList.as_view(), name='top-ten-vacancies'),

    # Function-based views URLs
    path('companies-fbv/', views.company_list_create, name='company-list-fbv'),
    path('vacancies-fbv/', views.vacancy_list_create, name='vacancy-list-fbv'),
]
