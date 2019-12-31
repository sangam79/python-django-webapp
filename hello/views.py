from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import TemplateView,ListView
from .models import College
from django.core.files.storage import FileSystemStorage




class HomeView(TemplateView):
    template_name='Home.html'



class GovernmentList(ListView):
    model = College
    template_name = 'government_list.html'

    def get_queryset(self,**kwargs):
        query = self.request.GET.get('userinput')

        object_list = College.objects.filter(Q(name__icontains = query))
        return object_list
