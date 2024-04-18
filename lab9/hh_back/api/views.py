from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = {"companies": list(companies.values())}
    return JsonResponse(data)

def company_detail(request, id):
    company = Company.objects.get(id=id)
    data = {"company": model_to_dict(company)}
    return JsonResponse(data)

def company_vacancies(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    data = {"vacancies": list(vacancies.values())}
    return JsonResponse(data)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {"vacancies": list(vacancies.values())}
    return JsonResponse(data)

def vacancy_detail(request, id):
    vacancy = Vacancy.objects.get(id=id)
    data = {"vacancy": model_to_dict(vacancy)}
    return JsonResponse(data)

def top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {"vacancies": list(top_vacancies.values())}
    return JsonResponse(data)
