from src.draw.application.drawer import Drawer
from src.draw.application.models import LottoDraw


class TestDrawer:
    def test_draw_winning_numbers(self):
        test_result = Drawer.draw_winning_numbers()

        assert isinstance(test_result, list)
        assert all([isinstance(element, int) for element in test_result])
        assert all(list(filter(lambda x: x >= 1 and x <= 49, test_result)))

    def test_draw_winning_numbers_different_results(self):
        test_result = Drawer.draw_winning_numbers()
        test_result_2 = Drawer.draw_winning_numbers()

        assert test_result is not test_result_2

    def test_draw_super_number(self):
        test_result = Drawer.draw_super_number()

        assert isinstance(test_result, list)
        assert isinstance(test_result[0], int)
        assert len(test_result) == 1
        assert (test_result[0] >= 0) and (test_result[0] <= 49)

    def test_draw(self):
        test_result = Drawer.draw()

        assert isinstance(test_result, LottoDraw)
