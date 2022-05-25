from django.views.generic import ListView, DetailView, CreateView, UpdateView
from books.models import Book
from reviews import forms as review_forms


class BooksView(ListView):
  
  model = Book
  paginate_by = 10
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "books"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = "All Books"
    return context


class BookDetail(DetailView):
  model = Book
  context_object_name = 'book'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    form = review_forms.CreateReviewForm()
    context["review_form"] = form
    return context


class CreateBook(CreateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )


class UpdateBook(UpdateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )