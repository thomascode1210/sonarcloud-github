import pytest
from main import greet_user, calculate_sum, main
from unittest.mock import patch

def test_greet_user_with_name():
    assert greet_user("An") == "Xin chào, An!"

def test_greet_user_without_name():
    assert greet_user("") == "Xin chào, bạn!"

def test_calculate_sum_positive():
    assert calculate_sum(2, 3) == 5

def test_calculate_sum_negative():
    assert calculate_sum(-1, -5) == -6

def test_main(monkeypatch, capsys):
    inputs = iter(["Minh", "4", "5"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()

    captured = capsys.readouterr()
    assert "Xin chào, Minh!" in captured.out
    assert "Tổng của 4 và 5 là: 9" in captured.out
