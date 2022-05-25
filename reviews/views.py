from django.shortcuts import redirect, reverse
from books.models import Book
from movies.models import Movie
from . import forms


def create_review(request, pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        type = request.POST.get("type")
        if type == "book":
          try:
            book = Book.objects.get(pk=pk)
            if not book:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.book = book
                review.created_by = request.user
                review.save()
                return redirect(reverse("books:book", kwargs={"pk":pk}))
          except:
            return redirect(reverse("core:home"))

        elif type == "movie":
          try:
            movie = Movie.objects.get(pk=pk)
            if not movie:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.movie = movie
                review.created_by = request.user
                review.save()
                return redirect(reverse("movies:movie", kwargs={"pk":pk}))
          except:
            return redirect(reverse("core:home"))