from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Publication, Author
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def about(request):
    return render(request, 'limaye/about.html')

class ObjectCreateView(CreateView):

    def form_valid(self, form):
        form.instance.image_set = ImageSet.objects.create(created_by=self.request.user)
        return super(CloudSpottingCreateView, self).form_valid(form)

class PublicationListView(ListView):

    model = Publication


class PublicationCreateView(CreateView):
    model = Publication
    fields = '__all__'
