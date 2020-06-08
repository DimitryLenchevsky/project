from . models import Genre, Book
from . forms import CreateGenreForm
from django.views.generic import CreateView, UpdateView, ListView
# Create your views here.


from django.views.generic.base import TemplateView

class Test(TemplateView):
    template_name = 'testapp/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate'] = self.get_rate()
        return context

    def get_rate(self):
        # from API
        return 2.75


# для Create
# 1 определить метод get или post
# 2 если get - создать форму, подкинуть в контекст и создать старницу
# 3 если post - получить данные из post запроса, создать объект и сохранить его в БД
# 4 показать другую страницу (сообщение об успехе)

class CreateGenre(CreateView):

    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/create_genre.html'
    success_url = '/test/3'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate'] = 123
        return context

class UpdateGenre(UpdateView):

    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/create_genre.html'
    success_url = '/test/3'

class ListGenre(ListView):

    model = Genre
    template_name = 'testapp/create_genre.html'
    queryset = Genre.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super().get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context