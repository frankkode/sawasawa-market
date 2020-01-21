from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import modelformset_factory
from django.contrib import messages
import urllib.parse
from .forms import *
from django.urls import reverse
from .models import Post, Images
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

from .models import Post, Images


def home(request):
    context = {
        'posts': Post.objects.all(),
        'images': Images.objects.all()
    }
    return render(request, 'blog/home.html', context)


def PostListView(request):
    context = {
        'posts': Post.objects.all(),
        'images': Images.objects.all()
    }
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'posts': posts,
        'page_range': page_range,
    }
    
    
    
    return render(request, 'blog/home.html', context)

def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

def UserPostListView(request, username):
    context = {
        'posts': Post.objects.filter(author__username=username),
    }
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    def get_queryset(self):
        username = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    return render(request, 'blog/user_posts.html', context)


def PostDetailView(request, id):
    post= Post.objects.get(id=id)
    context = {
        'post': post,
    }
    model = Post 
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'
    return render(request, 'blog/post_detail.html', context)


def PostCreateView(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print(formset.cleaned_data)
            for f in formset:
                print(f.cleaned_data)
                try:
                    photo = Images(post=post, image=f.cleaned_data.get('image'))
                    photo.save()
                except Exception as e:
                    break
            messages.success(request, "Post has been successfully created.")
            return render(request, 'blog/home.html')
    else:
        form = PostCreateForm()
        formset = ImageFormset(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'blog/post_form.html', context)

    


def PostUpdateView(request, id):
    post = get_object_or_404(Post, id=id)
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=4, max_num=4)
    if post.author != request.user:
        raise Http404()
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            print(formset.cleaned_data)
            data = Images.objects.filter(post=post)
            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        photo.save()
                    elif f.cleaned_data['image'] is False:
                        photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        d = Images.objects.get(id=data[index].id)
                        d.image = photo.image
                        d.save()
            messages.success(request, "{} has been successfully updated!".format(post.title))
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
        formset = ImageFormset(queryset=Images.objects.filter(post=post))
    context = {
    'form': form,
    'post': post,
    'formset': formset,
    }
    return render(request, 'blog/post_form.html', context)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def PostDeleteView(request, id):
    
    obj = get_object_or_404(Post, id=id)
    obj.delete()
        
    query = Post.objects.filter(id=id)
    query.delete()
    messages.warning(request, 'post has been successfully deleted!')
    return redirect('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('blog/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
            "New contact form email",
            content,
            "Creative web" + '',
            ['masasimpafra@gmail.com'],
            headers = { 'Reply To': contact_email }
        )

        email.send()

        return redirect('blog-success')
    return render(request, 'blog/contact.html', {'form':Contact_Form })

# redirect success page
def Success(request):
    return render(request, 'blog/success.html')

#def charge(request):
  #  return render(request, 'blog/charge.html')


#def pay_success(request, **kwargs):
   # return render(request, 'blog/pay_success.html')

    
def footer(request):
    return render(request, 'blog/footer.html', {'title': 'footer'})


def navigation(request):
    return render(request, 'blog/navigation.html', {'title': 'navigation'})



def base(request):
    return render(request, 'blog/base.html', {'title': 'base'})

