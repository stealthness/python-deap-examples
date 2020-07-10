from unittest import TestCase

from ga_simple_mouse.mouse_class import IntMouse


class TestIntMouse(TestCase):

    def setUp(self) -> None:
        self.mouse0 = IntMouse('m0')

    def test_initial_IntMouse_has_default_0_0(self):
        self.assert_mouse_position(0, 0, self.mouse0.get_pos(), msg='test mouse at initial position')

    def test_m0_move_to_the_left_by_1(self):
        self.mouse0.move('left')
        self.assert_mouse_position(-1, 0, self.mouse0.get_pos(), msg='move left')

    def test_m0_move_to_the_right_by_1(self):
        self.mouse0.move('right')
        self.assert_mouse_position(1, 0, self.mouse0.get_pos(), msg='move right')

    def test_m0_move_to_the_up_by_1(self):
        self.mouse0.move('up')
        self.assert_mouse_position(0, 1, self.mouse0.get_pos(), msg='move up')

    def test_m0_move_to_the_down_by_1(self):
        self.mouse0.move('down')
        self.assert_mouse_position(0, -1, self.mouse0.get_pos(), msg='move down')

    # misc test

    def test_assert(self):
        self.assert_mouse_position(0, 0, (0, 0), msg="0")
        self.assert_mouse_position(0, 1, (0, 1), msg="1")
        self.assert_mouse_position(1, 0, (1, 0), msg="2")
        self.assert_mouse_position(1, 1, (1, 1), msg="3")

    # Assert functions

    def assert_mouse_position(self, exp_x: int, exp_y: int, pos: tuple, **kwargs):
        """
        Assert the position of a mouse
        :param exp_x:
        :param exp_y:
        :param pos:
        :param kwargs:
        :return:
        """
        err_msg = ''
        if kwargs == 'msg':
            err_msg = kwargs['msg']
        if exp_x is not None:
            self.assertEqual(exp_x, pos[0], f'{err_msg} : exp_x:{exp_x}')
        if exp_y is not None:
            self.assertEqual(exp_y, pos[1], f'{err_msg} : exp_y:{exp_x}')
