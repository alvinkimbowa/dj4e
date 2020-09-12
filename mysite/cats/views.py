from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views import generic
from django.urls import reverse_lazy

from cats.models import Breed, Cat

# Create your views here.

# This is one way to hard code the view
# class MainView(LoginRequiredMixin, View):
#     def get(self, request):
#         breed_count = Breed.objects.all().count()
#         cat_list = Cat.objects.all()

#         context = {'breed_count': breed_count, 'cat_list': cat_list}

#         return render(request, 'cats/cat_list.html', context=context)

# This is another way: using inheritance
class MainView(LoginRequiredMixin, generic.ListView):
    model = Cat
    # template_name = 'cats/cat_list.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count();

        return context


# You can just use ListView
# You also don't need to add the template name (u can add it just for convinience
class BreedView(LoginRequiredMixin, generic.ListView):
    model = Breed
    # By convention, the template name is like below
    # template_name = 'cats/breed_list.html'

    # def get(self, request):
    #     breed_list = Breed.objects.all();
    #     context = {'breed_list': breed_list};
    #     return render(request, 'cats/breed_list.html', context=context)


class BreedCreateView(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedUpdateView(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

class BreedDeleteView(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')


class CatCreateView(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdateView(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDeleteView(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

