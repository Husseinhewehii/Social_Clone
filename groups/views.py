from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic as g
from . import models as m

class Create_Group(LoginRequiredMixin, g.CreateView):

    model = m.Group
    fields = ('name','description')

class Single_Group(g.DetailView):
    model = m.Group

class List_Groups(g.ListView):
    model = m.Group

class Join_Group(LoginRequiredMixin,g.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(m.Group,slug=self.kwargs.get('slug'))

        try:
            m.Group_Members.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'Already a Member')
        else:
            messages.success(self.request,'You Are Now a Member, Welcome .')
        
        return super().get(request,*args,**kwargs)

class Leave_Group(LoginRequiredMixin, g.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = m.Group_Members.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        except m.Group_Members.DoesNotExist:
            messages.warning(self.request,'Sorry, You Are not in this Group')
        else:
            membership.delete()
            messages.success(self.request,'You Left')
        
        return super().get(request,*args,**kwargs)
