from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

def about(request):
    return render(request, 'about.html')

class ObjectCreateView(CreateView):

    def form_valid(self, form):
        form.instance.image_set = ImageSet.objects.create(created_by=self.request.user)
        return super(CloudSpottingCreateView, self).form_valid(form)
