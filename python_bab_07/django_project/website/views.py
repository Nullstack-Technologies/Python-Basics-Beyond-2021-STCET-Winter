from django.shortcuts import render
from django.http import HttpResponse

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
