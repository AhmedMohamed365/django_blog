from django.shortcuts import render
from django.http import HttpResponse
#imported models
from django.views.generic import ListView , DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.



def Home(request):
    context = {
        'posts': Post.objects.all(),
        'title' : 'Home'
    }
    return render(request,'blog/home.html',context=context)

# rewrite as class based view

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request.user)
        return super().form_valid(form)
    
    # is it user who posted that post ?
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user: 
            return True
        else:
            return False
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    # is it user who posted that post ?
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user: 
            return True
        else:
            return False
    
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    



def about(request):
    return render(request,'blog/about.html') 

