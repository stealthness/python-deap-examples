from unittest import TestCase

from ga_simple_mouse.mouse_class import IntMouse


class TestIntMouse(TestCase):

    def setUp(self) -> None:
        self.mouse0 = IntMouse('m0')

    def test_initial_IntMouse_has_default_0_0(self):
        self.assertEqual(0, self.mouse0.x, f'mouse x:{self.mouse0.x}')
        self.assertEqual(0, self.mouse0.y, f'mouse y:{self.mouse0.y}')

    def test_m0_move_to_the_left_by_1(self):
        self.mouse0.move('left')
        self.assertEqual(-1, self.mouse0.x, f'mouse x:{self.mouse0.x}')
        self.assertEqual(0, self.mouse0.y, f'mouse y:{self.mouse0.y}')

    def test_m0_move_to_the_right_by_1(self):
        self.mouse0.move('right')
        self.assertEqual(1, self.mouse0.x, f'mouse x:{self.mouse0.x}')
        self.assertEqual(0, self.mouse0.y, f'mouse y:{self.mouse0.y}')

    def test_m0_move_to_the_up_by_1(self):
        self.mouse0.move('up')
        self.assertEqual(0, self.mouse0.x, f'mouse x:{self.mouse0.x}')
        self.assertEqual(1, self.mouse0.y, f'mouse y:{self.mouse0.y}')

    def test_m0_move_to_the_down_by_1(self):
        self.mouse0.move('down')
        self.assertEqual(0, self.mouse0.x, f'mouse x:{self.mouse0.x}')
        self.assertEqual(-1, self.mouse0.y, f'mouse y:{self.mouse0.y}')
