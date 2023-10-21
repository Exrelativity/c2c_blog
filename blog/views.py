from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from post.models import Category, Post
from post.forms import SearchForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request, msg=None):
    categories = Category.objects.prefetch_related("subCategory__post").filter(status=True, front=True)[:7]
    paginator = Paginator(categories, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"msg": msg, "page_obj": page_obj, "categories": categories })

def about(request, msg=None):
    return render(request, "about.html", {"msg": msg})

def contact(request, msg=None):
    return render(request, "contact.html", {"msg": msg})

def faq(request, msg=None):
    return render(request, "faq.html", {"msg": msg})

def search(request, msg=None):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_terms = form.cleaned_data.get("search").split()
            posts = Post.objects.filter(Q(title__icontains=search_terms[0]) | Q(content__icontains=search_terms[0]))
            for term in search_terms[1:]:
                posts = posts.filter(Q(title__icontains=term) | Q(content__icontains=term))
            paginator = Paginator(posts, 15)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "post-front/search.html", {"msg": msg, "form": form, "page_obj": page_obj})
    else:
        form = SearchForm()
    return render(request, "post-front/search.html", {"msg": msg, "form": form})

@login_required
def dashboard(request, msg=None):
    categories = Category.objects.prefetch_related("subCategory__post").filter(status=True, front=True)[:7]
    return render(request, "dashboard.html", {"msg": msg, "categories": categories })

def error_404_handler(request, exception):
    return render(request, 'notfound.html')

def login_redirect(request):
    return reverse('login')  # Use a named URL for login
