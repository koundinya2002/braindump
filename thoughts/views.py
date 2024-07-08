from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Thoughts
from .forms import AddForm, EditForm
from django.urls import reverse_lazy


@login_required
def home(request):
    thought = Thoughts.objects.filter(owner=request.user)
    thoughts = reversed(thought)
    return render(request, "home.html", {
        "thoughts": thoughts
    })


class AddView(CreateView):
    model = Thoughts
    form_class = AddForm
    template_name = 'add.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    

class DeleteView(DeleteView):
    model = Thoughts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class EditView(UpdateView):
    model = Thoughts
    form_class = EditForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home')