# -*- coding: utf-8 -*-
"""Comp 354.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DlJ6xfuunDOX3Kjft0pxws9rbKVipHmH
"""

import math

''' HyperbolicSine class is used to calculate Sinh(x).
Which x can be a real or complex number.
The instance of the class is then stored in calculator history. '''


class HyperbolicSine:

    '''HyperbolicSine has only one parameter:
Value is the real number or complex number which we want to calculate Sinh on.
We define EulerNum and use the math library for importing
the constant e(the Euler's number). '''
    def __init__(self, value):
        self._value = value
        self._EulerNum = math.e
        self._Sinh = 0

    # In this function we calculate e^x and return the value
    def _calculate_exponential(self, value):
        return (math.e)**value

    # In this function, we calculate the numinator of Sinh which is e^x - e^-x
    def _calculate_numerator(self, value):
        return (self._calculate_exponential(value) -
                self._calculate_exponential(-1*value))

    # In this function, we calculate Sinh which is (e^x - e^-x)/2
    def calculate_Sinh(self):
        self._Sinh = (self._calculate_numerator(self._value))/2
        return self._Sinh

    # Returns the instanced value list
    def get_value(self):
        return self._value

    # Set instanced value
    def set_value(self, new_value):
        self._value = new_value

    # Returns the Sinh value
    def get_Sinh(self):
        return self._Sinh