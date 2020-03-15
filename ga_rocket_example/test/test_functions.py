import unittest
import numpy as np
from ga_rocket_example.individual_class import Individual
from ga_rocket_example.rocket_class import Rocket


class MyTest(unittest.TestCase):

    def assertItem(self, item, **kwargs):
        if 'err_msg' not in kwargs:
            kwargs["err_msg"] = ''
        if type(item) is Individual:
            rocket = item.rocket
        elif type(item) is Rocket:
            rocket = item
        else:
            raise TypeError('type not testable')

        if 'exp_pos' in kwargs:
            np.testing.assert_allclose(kwargs['exp_pos'], rocket.pos,
                                       err_msg=f'{kwargs["err_msg"]}, exp_pos: {kwargs["exp_pos"]}, act_pos:{rocket.pos}')

        if 'exp_vel' in kwargs:
            np.testing.assert_allclose(kwargs['exp_vel'], rocket.vel,
                                       err_msg=f'{kwargs["err_msg"]}, exp_vel: {kwargs["exp_vel"]}, act_vel:{rocket.vel}')

        if 'exp_acc' in kwargs:
            np.testing.assert_allclose(kwargs['exp_acc'], rocket.acc,
                                       err_msg=f'{kwargs["err_msg"]}, exp_acc: {kwargs["exp_acc"]}, act_acc:{rocket.acc}')

        if 'exp_dir' in kwargs:
            np.testing.assert_allclose(kwargs['exp_dir'], rocket.dir,
                                       err_msg=f'{kwargs["err_msg"]}, exp_dir: {kwargs["exp_dir"]}, act_dir:{rocket.dir}')

    def assertRocket(self, rocket, **kwargs):
        self.assertItem(rocket, **kwargs)

    def assertIndividual(self, individual, **kwargs):
        pass


if __name__ == '__main__':
    unittest.main()
