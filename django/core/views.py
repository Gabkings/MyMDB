from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from core.models import Movie,Person

class MovieList(ListView):
    model = Movie
    paginate_by = 10

    def get_context_data(self,
                         **kwargs):
        ctx = super(MovieList,
                    self).get_context_data(
            **kwargs)
        page = ctx['page_obj']
        paginator = ctx['paginator']
        ctx['page_is_first'] = (
            page.number == 1)
        ctx['page_is_last'] = (
            page.number == paginator.num_pages)
        return ctx


class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons()
    )

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()