from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Author
from .forms import AuthorForm

# Create your views here.


# def hello_world(request):
#     """
#         Hello World View
#     """
#     return HttpResponse("Hello World")

# def hello_world_2(request):
#     """
#         Hello World View
#     """
#     return HttpResponse("Hello World 2")


def index(request):
    """
        FBV -> Function Based Views
        Return the Home Page
    """

    return render(request, 'index.html')


def contact_us(request):
    """
        FBV -> Function Based Views
        Return the Home Page
    """
    return render(
        request,
        'contact_us.html',
        {
            'name': 'Nauman Arif',
            'linkedin': '@naumanarif21',
            'github': '@naumanarif21'
        }
    )


def author_view(request):
    """
       This View Returns all the authors present
    """

    if request.method == 'POST':
        name = request.POST.get('name')
        Author.objects.create(name=name)

    # authors = Author.objects.filter(name__icontains="a")
    # authors = Author.objects.filter(name="Nauman Arif")
    authors = Author.objects.all()

    return render(
        request,
        'author.html',
        {
            'authors': authors
        }
    )


class AuthorAddView(View):
    """
        CBV
    """

    def get(self, request, *args, **kwargs):
        form = AuthorForm()
        authors = Author.objects.all()

        return render(
            request, 
            'cbv/author_add.html', 
            {'form': form, 'authors': authors}
            )


    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        authors = Author.objects.all()

        if form.is_valid():
            form.save()
            form = AuthorForm()
            return render(
                request, 
                'cbv/author_add.html', 
                {'form': form, 'authors': authors}
                )   
        return render(request, 'cbv/author_add.html', {'form': form, 'authors': authors}
)
