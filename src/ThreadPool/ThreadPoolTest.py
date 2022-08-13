import random
from unittest import TestCase
import numpy as np
from ThreadPoolEx import main_sum, main_sum_2, sum_up


class TestThreadPool(TestCase):
    # def test_sum_pool(self):
    #     # given...
    #     list_r = [100] * 10000
    #     expected_value = sum(list_r)
    #     result = main_sum(list_r)
    #     # when...
    #     # result = summator.sum_up()
    #     # then...
    #     self.assertEqual(expected_value, result)
    #
    #
    # def test_up(self):
    #     # given...
    #     list_r = [100] * 10000
    #     expected_value = sum(list_r)
    #     result = main_sum_2(list_r)
    #     # when...
    #     # result = summator.sum_up()
    #     # then...
    #     self.assertEqual(expected_value, result)

    def test_sum_up(self):
        # given...
        list_r = [100] * 10000
        expected_value = sum(list_r)
        print(expected_value)
        result = sum_up(list_r)
        print(result)
        # when...
        # result = summator.sum_up()
        # then...
        self.assertEqual(expected_value, result)