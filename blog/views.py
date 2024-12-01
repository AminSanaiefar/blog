from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm
from .models import BlogPost


class BlogPostView(generic.ListView):
    # model = BlogPost
    template_name = 'blog/blog_posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPost.STATUS_CHOICES[0][0]).order_by('-datetime_modified')


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'post'


class BlogPostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'


class BlogPostUpdateView(generic.UpdateView):
    model = BlogPost
    form_class = PostForm
    # fields = ['title', 'text', 'author', 'status']
    template_name = 'blog/create_post.html'


class BlogPostDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')


# def blog_post_view(request):
#     # posts = BlogPost.objects.all()
#     posts = BlogPost.objects.filter(status=BlogPost.STATUS_CHOICES[0][0]).order_by('-datetime_modified')
#     context = {'posts_list': posts}
#     return render(request, 'blog/blog_posts_list.html', context)

# def blog_post_detail_view(request, pk):
#     # Ways To Handle The Object Does Not Exist | 404 --->
#     # try:
#     #     post = BlogPost.objects.get(id=pk)
#     # except ObjectDoesNotExist:
#     #     pass
#     # except BlogPost.DoesNotExist:
#     #     pass
#
#     post = get_object_or_404(BlogPost, pk=pk)
#     return render(request, 'blog/blog_post_detail.html', {'post': post})

# def create_post_view(request):
#     # Using Django ModelForm For Getting Data From Html Form And Validate Them By ModelForm-->
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PostForm()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/create_post.html', {'form': form})
#     # without using Django ModelForm -->
#     # if request.method == 'POST':
#     #     BlogPost.objects.create(
#     #         title=request.POST.get('title'),
#     #         text=request.POST.get('text'),
#     #         author=User.objects.all()[0],
#     #         status='pub'
#     #     )
#     # else:
#     #     pass
#     # return render(request, 'blog/create_post.html')

# def post_update_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#
#     return render(request, 'blog/create_post.html', context={'form': form})

# def post_delete_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', context={'post': post})
