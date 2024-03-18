import pytest

from task_1_test_1 import get_data, get_count_names
from task_1_test_2 import get_sorted_courses
from task_1_test_3 import get_unique_names


class TestTask1Pytest:

    @pytest.mark.parametrize(
        'word', (
                'courses',
                'mentors'
        )
    )
    def test_value_in_list(self, word):
        result = get_data(word)
        assert len(result) == 4

    def test_text_in_result(self):
        result = get_count_names()
        assert isinstance(result, str)


class TestTask2Pytest:

    def test_text_in_result(self):
        result = get_sorted_courses()
        assert isinstance(result, str)


class TestTask3Pytest:

    def test_get_unique_names(self):
        result = get_unique_names()
        assert isinstance(result, str)
