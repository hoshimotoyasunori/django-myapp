from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import DiaryForm
from .models import Diary
from django.utils import timezone





class IndexView(TemplateView):
    template_name = 'index.html'

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary

class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary

class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.update_at = timezone.now()
        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')