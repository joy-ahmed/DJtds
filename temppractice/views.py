
from django.http import HttpResponse
from django.shortcuts import render


# def intialData(request):
#     return render(request, "index.html",
#                   {"data": "It is a long established fact \
#                    that a reader will be distracted by the readable content \
#                    of a page when looking at its layout. \
#                    The point of using Lorem Ipsum is that \
#                    it has a more-or-less normal distribution\
#                     of letters, as opposed to using 'Content here, content here', making"})


def home(request):
    return render(request, "index.html")


def portfolio(request):
    return render(request, "portfolio-details.html")
