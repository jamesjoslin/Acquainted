from django.http import HttpResponse
from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

# views is how django links diplaying the objects to what html template will be used to do so. connects URL requests with html with models.py
class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    paginate_by = 20

class PostTemplateView(DetailView):
    model = BlogPost
    template_name = 'post_template.html'

class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blogpage')

class AllPostsView(ListView):
    model = BlogPost
    template_name = 'all_posts.html'
    paginate_by = 20
