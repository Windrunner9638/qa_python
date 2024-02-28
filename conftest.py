import pytest

from main import BooksCollector


@pytest.fixture(scope="function")  # фикстура, которая создаёт коллекцию книг
def collector():
    collector = BooksCollector()
    collector.books_genre = {'Великий Гэтсби': 'Фантастика', 'Приключения Шерлока Холмса': 'Детективы',
                             'Дюна': 'Фантастика'}
    collector.favorites = ['Дюна', 'Приключения Шерлока Холмса']
    return collector
