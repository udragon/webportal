from django.shortcuts import render
from models import Category, Link

# Create your views here.
def homepage(request):
    return render(request, "index.html", \
         { 'categories' : Category.objects.all().order_by("name"), })

def show_category(request, category_name):

    # Search for a matching category
    try: category = Category.objects.get(name=category_name)
    except: return homepage(request)

    links = Link.objects.filter(category=category).order_by("name")
    return render(request, "category.html", \
         { 'categories' : Category.objects.all().order_by("name"),
           'links'      : links, })

