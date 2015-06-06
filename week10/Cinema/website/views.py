from django.shortcuts import render
from .models import Movie, Projection, Reservation


def index(request):
    projections = Projection.objects.all().order_by("-date")
    movies = Movie.objects.all().order_by("id")
    numbers = [x for x in range(1, 101)]
    if request.method == "POST":
        name = request.POST["movielist"].replace("_", " ")
        if name != "All":
            projections = [
                x for x in projections if str(x) == name]
    if request.method == "GET":
        all_l = request.GET.getlist('select')
    return render(request, "index.html", locals())


def about(request):
    return render(request, "about.html")
