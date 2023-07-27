from string_calculator import string_calculator 
import pytest

def test_string_calculator_1():
    input = '1'
    assert(string_calculator(input)) == ["1", 1.0]

def test_string_calculator_2():
    input = '2'
    assert(string_calculator(input)) == ["2", 2.0]

def test_string_calculator_3():
    input = '10'
    assert(string_calculator(input)) == ["10", 10.0]

def test_string_calculator_4():
    input = '1 + 1'
    assert(string_calculator(input)) == ["1 + 1", 2.0]

def test_string_calculator_5():
    input = '1 + 1.5'
    assert(string_calculator(input)) == ["1 + 1.5", 2.5]

