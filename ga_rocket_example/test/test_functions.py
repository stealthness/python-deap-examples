import unittest
import numpy as np
from ga_rocket_example.individual_class import Individual
from ga_rocket_example.rocket_class import Rocket


class MyTest(unittest.TestCase):

    def assertRocket(self, item, **kwargs):
        if type(item) is Individual:
            rocket = item.rocket
        if type(item) is Rocket:
            rocket = item

        if 'pos' in kwargs:
            np.testing.assert_allclose(kwargs['pos'], rocket.pos)


if __name__ == '__main__':
    unittest.main()
