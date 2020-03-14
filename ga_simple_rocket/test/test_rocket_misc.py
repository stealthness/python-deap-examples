from ga_simple_rocket.simple_rocket_class import SimpleRocket
from ga_simple_rocket.test.test_functions import MyTest  # extend unittest


class MyTestCase(MyTest):

    def setUp(self):
        self.rocket = SimpleRocket('test')

    def test_create(self):
        self.assertRocket(self.rocket, exp_pos=0.0, exp_vel=0.0, exp_acc=-9.8, has_landed=False, has_failed=False)

    def test_create_with_pos(self):
        self.rocket = SimpleRocket('test', pos=100.0)
        self.assertRocket(self.rocket, exp_pos=100.0, exp_vel=0.0, exp_acc=-9.8, has_landed=False, has_failed=False)

    def test_create_with_vel(self):
        self.rocket = SimpleRocket('test', vel=-10.0)
        self.assertRocket(self.rocket, exp_pos=0.0, exp_vel=-10.0, exp_acc=-9.8, has_landed=False, has_failed=False)

    def test_create_with_acc(self):
        self.rocket = SimpleRocket('test', acc=100)
        self.assertRocket(self.rocket, exp_pos=0.0, exp_vel=0.0, exp_acc=100, has_landed=False, has_failed=False)
