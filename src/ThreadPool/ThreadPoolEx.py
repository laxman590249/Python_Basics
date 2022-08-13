from concurrent.futures import ThreadPoolExecutor
from time import sleep
import functools


def add_future(list_values):
    return sum(list_values)


def main_sum(list_r):
   executor = ThreadPoolExecutor(5)
   future_1 = executor.submit(add_future, (list_r[:5000]))
   future_2 = executor.submit(add_future, (list_r[5000:]))
   # print(future_1.result() + future_2.result())
   return future_1.result() + future_2.result()

def main_sum_2(list_r):
   return sum(list_r)

def process_sum(internal_list):
  return functools.reduce(lambda a, b: a+b, internal_list)

def sum_up(_array):
  """
  Will sum up all the elements in the array, FAST.
  :return: sum of value of all the elements in the array
  :raises: ValueError if array was not given during the class init
  """
  if isinstance(_array, list):
      # sum_value = 0
      # for outer_list in _array:
      sum_value = process_sum(_array)
      return sum_value
  raise ValueError
