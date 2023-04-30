from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
# Create your views here.



class PropertyList(ListView):
    model = Property
    paginate_by = 1





class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(Category=self.get_object().Category)[:2]
        return context
    
    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.author = request.user
            myform.save()

            return redirect('/')

