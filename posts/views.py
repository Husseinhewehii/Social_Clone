from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as g
from django.http import Http404
from django.contrib import messages
from braces.views import SelectRelatedMixin
from . import models ,forms

User = get_user_model()

class Post_List(SelectRelatedMixin, g.ListView):

    model = models.Post
    select_related = ('user','group')

class User_Posts(g.ListView):
    model = models.Post
    template_name = 'posts/post_user_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
        
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
    

class Post_Detail(SelectRelatedMixin, g.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get("username"))

class Create_Post(LoginRequiredMixin,SelectRelatedMixin, g.CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
class Delete_Post(LoginRequiredMixin,SelectRelatedMixin,g.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:post_list')


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted Successfully')
        return super().delete(*args,**kwargs)