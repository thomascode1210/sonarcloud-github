# test_main.py
import pytest
from main import greet_user, calculate_sum

def test_greet_user_with_name():
    assert greet_user("An") == "Xin chào, An!"

def test_greet_user_without_name():
    assert greet_user("") == "Xin chào, bạn!"

def test_calculate_sum_positive():
    assert calculate_sum(2, 3) == 5

def test_calculate_sum_negative():
    assert calculate_sum(-1, -5) == -6
