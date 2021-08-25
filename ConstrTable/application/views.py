from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Application, ConstructionSite
from .forms import ApplicationForm


class HomeApplication(ListView):
    model = Application
    template_name = 'application/home_application_list.html'
    context_object_name = 'application' #указываем название вместо "object"
    #extra_context = {'name': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Application.objects.filter(is_executed=False)


class ApplicationByArea(ListView):
    model = Application
    template_name = 'application/home_application_list.html'
    context_object_name = 'application'
    #allow_empty = False показывает только невыполненные заявки

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = ConstructionSite.objects.get(pk=self.kwargs['area_id'])
        return context

    def get_queryset(self):
        return Application.objects.filter(area_id=self.kwargs['area_id'], is_executed=False)


# def index(request):
#     application = Application.objects.all()
#     context = {
#         'application': application,
#         'name': 'Заявка',
#     }
#     return render(request, template_name='application/index.html', context=context)


def get_area(request, area_id):
    application = Application.objects.filter(area_id=area_id)
    area = ConstructionSite.objects.get(pk=area_id)
    return render(request, 'application/area.html', {'application': application, 'area': area})


class ViewApplication(DetailView):
    model = Application
    context_object_name = 'application_item'
    #template_name = 'application/application_detail.html'
    #pk_url_kwarg = 'application_id'


class CreateApplication(CreateView):
    form_class = ApplicationForm
    template_name = 'application/add_application.html'
    success_url = reverse_lazy('home')

# def view_application(request, application_id):
#     #application_item = Application.objects.get(pk=application_id)
#     application_item = get_object_or_404(Application, pk=application_id)
#     return render(request, 'application/view_application.html', {"application_item": application_item})


# def add_application(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             #application = Application.objects.create(**form.cleaned_data)
#             application = form.save()
#             return redirect(application)
#     else:
#         form = ApplicationForm()
#     return render(request, 'application/add_application.html', {'form': form})
