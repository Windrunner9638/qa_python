import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture  # фикстура, которая создаёт коллекцию книг
    def collector(self):
        collector = BooksCollector()
        collector.books_genre = {'Великий Гэтсби': 'Фантастика', 'Приключения Шерлока Холмса': 'Детективы',
                                 'Дюна': 'Фантастика'}
        collector.favorites = ['Дюна', 'Приключения Шерлока Холмса']
        return collector

    def test_books_genre(self):
        collector = BooksCollector()

        assert collector.books_genre == {}

    def test_favorites(self):
        collector = BooksCollector()

        assert collector.favorites == []

    def test_genre(self):
        collector = BooksCollector()

        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating(self):
        collector = BooksCollector()

        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name', ['Кладбище Домашних Животных', 'Анна Каренина', 'Война и Мир'])
    def test_add_new_book_books_are_added(self, collector, name):

        collector.add_new_book(name)
        assert name in collector.books_genre.keys()

    @pytest.mark.parametrize('name, genre', [['Кладбище Домашних Животных', 'Ужасы'], ['Ревизор', 'Комедии']])
    def test_set_book_genre_appropriate_genre_can_be_set_for_existing_book(self, collector, name, genre):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_get_book_genre_new_book_does_not_have_genre(self, collector):

        collector.add_new_book('Анна Каренина')
        assert collector.get_book_genre('Анна Каренина') == ''

    def test_get_books_with_specific_genre_true(self, collector):

        assert collector.get_books_with_specific_genre('Фантастика') == ['Великий Гэтсби', 'Дюна']

    def test_get_books_genre_true(self, collector):

        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_true(self, collector):

        assert collector.get_books_for_children() == ['Великий Гэтсби', 'Дюна']

    def test_add_book_in_favorites_book_is_added(self, collector):

        collector.add_book_in_favorites('Великий Гэтсби')
        assert 'Великий Гэтсби' in collector.favorites

    def test_delete_book_from_favorites_book_is_deleted(self, collector):

        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.favorites

    def test_get_list_of_favorites_books_true(self, collector):

        assert collector.get_list_of_favorites_books() == collector.favorites
