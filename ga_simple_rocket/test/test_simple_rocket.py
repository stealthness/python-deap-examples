"""
In this test we are dealing with constant acceleration of small time interval

a(t) = - g + F where F is force of the engine acceleration, for simplicity since acceleration is constant over time
interval, then a(t) = a Therefore change in acceleration is da = 0 Since acceleration is approximated as linear over
the time interval then, change in velocity is the time interval multiplied the acceleration
dv = a*dt
Since we assumed that the change in velocity is linear due constant acceleration then change in distance is
ds  = (v - u)*dt/2
    = dv*dt/2
    = (a*dt^2)/2

"""
from ga_rocket_example import config
from ga_simple_rocket.simple_rocket_class import SimpleRocket
from ga_simple_rocket.test.test_functions import MyTest
# MyTest extends unittest


class MyTestCase(MyTest):

    def setUp(self):
        self.r = SimpleRocket('rocket')

    def test_gravity_1d(self):
        self.assertEqual(-9.8, config.GRAVITY_1d)

    def test_create(self):
        exp_name = 'rocket'
        self.assertEqual(exp_name, self.r.name)
        self.assertAlmostEqual(0.0, self.r.pos, delta=MyTest.TOL, msg="pos")
        self.assertAlmostEqual(0.0, self.r.vel, delta=MyTest.TOL, msg='vel')
        self.assertAlmostEqual(0.0, self.r.acc, delta=MyTest.TOL, msg='acc')

    def test_rocket_after_1s_update(self):
        for x in range(config.TIME_INTERVALS):
            self.r.update()
        self.assertAlmostEqual(-4.9, self.r.pos, delta=MyTest.TOL, msg='pos')
        self.assertAlmostEqual(-9.8, self.r.vel, delta=MyTest.TOL, msg='vel')
        self.assertAlmostEqual(-9.8, self.r.acc, delta=MyTest.TOL, msg='acc')

    def test_rocket_after_3s_update(self):
        for x in range(3*config.TIME_INTERVALS):
            self.r.update()
        self.assertAlmostEqual(-44.1, self.r.pos, delta=MyTest.TOL, msg='pos')
        self.assertAlmostEqual(-29.4, self.r.vel, delta=MyTest.TOL, msg='vel')
        self.assertAlmostEqual(-9.8, self.r.acc, delta=MyTest.TOL, msg='acc')

    def test_config_gravity_1d(self):
        self.assertAlmostEqual(float(-9.8), config.GRAVITY_1d, MyTest.TOL)

    def test_config_engine_on_in_equilibrium(self):
        self.r.engine_force = -config.GRAVITY_1d
        self.r.engine_on = True
        for i in range(100):
            self.r.update()
            self.assertAlmostEqual(-0.0, self.r.pos, delta=MyTest.TOL, msg='pos')
            self.assertAlmostEqual(-0.0, self.r.vel, delta=MyTest.TOL, msg='vel')
            self.assertAlmostEqual(-0.0, self.r.acc, delta=MyTest.TOL, msg='acc')

    def test_rocket_after_1s_update_engine_on(self):
        self.r.engine_force = -config.GRAVITY_1d*2
        self.r.engine_on = True
        for x in range(config.TIME_INTERVALS):
            self.r.update()
        self.assertAlmostEqual(4.9, self.r.pos, delta=MyTest.TOL, msg='pos')
        self.assertAlmostEqual(9.8, self.r.vel, delta=MyTest.TOL, msg='vel')
        self.assertAlmostEqual(9.8, self.r.acc, delta=MyTest.TOL, msg='acc')

    def test_rocket_after_3s_update_engine(self):
        self.r.engine_force = -config.GRAVITY_1d*2
        self.r.engine_on = True
        for x in range(3*config.TIME_INTERVALS):
            self.r.update()
        self.assertAlmostEqual(44.1, self.r.pos, delta=MyTest.TOL, msg='pos')
        self.assertAlmostEqual(29.4, self.r.vel, delta=MyTest.TOL, msg='vel')
        self.assertAlmostEqual(9.8, self.r.acc, delta=MyTest.TOL, msg='acc')


if __name__ == '__main__':
    MyTest.main()
