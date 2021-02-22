from django.shortcuts import render, HttpResponse, redirect
from .models import Blog, Contact
from .forms import BlogForm, ContactForm
import math

# Create your views here.


def home(request):
    context = {'home_page': 'active'}
    return render(request, 'my_blog/index.html', context)


def blogHome(request):
    no_of_post = 6

    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    blogs = Blog.objects.all()[::-1]

    print(blogs)
    lenght = len(blogs)
    blogs = blogs[(page-1)*no_of_post: page*no_of_post]
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page < math.ceil(lenght/no_of_post):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'blog_page': 'active',
               'prev': prev, 'nxt': nxt}
    return render(request, 'my_blog/blog.html', context)


def blogPost(request, slug):
    blog = Blog.objects.filter(slug=slug).last()

    edit_blog = BlogForm(instance=blog)
    if request.method == 'POST':
        blog.delete()
        return redirect('/blog')
    context = {'blog': blog, 'edit_blog': edit_blog, 'blog_page': 'active'}
    return render(request, 'my_blog/blogpost.html', context)


def about(request):
    context = {'about_page': 'active'}
    return render(request, 'my_blog/about.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'contact_page': 'active', 'form': form}
    return render(request, 'my_blog/contact.html', context)


def msgDetails(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/dashboard')
    context = {'contact': contact, 'blog_page': 'active'}
    return render(request, 'my_blog/msg_detail.html', context)


def search(request):
    # if request.method == post:

    return render(request, 'my_blog/search.html')


def createBlog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog')
    context = {'create_blog_page': 'active', 'form': form}
    return render(request, 'my_blog/create_blog.html', context)

def EditBlog(request, slug):
    blog = Blog.objects.filter(slug=slug).last()

    edit_blog = BlogForm(instance=blog)

    context = {'edit_blog': edit_blog,}
    return render(request, 'my_blog/edit_blogpost.html', context)


def Dashboard(request):
    blogs = Blog.objects.all()
    r_blogs = blogs[::-1]
    contacts = Contact.objects.all()
    r_contacts = contacts[::-1]
    no_of_blogs = blogs.count()
    no_of_msg = contacts.count()
    context = {'dashboard_page': 'active',
               'no_of_blogs': no_of_blogs, 'no_of_msg': no_of_msg, 'blogs': r_blogs, 'contacts': r_contacts}
    return render(request, 'my_blog/dashboard.html', context)
