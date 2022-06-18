import pytest

@pytest.fixture()
def text():
    print("开始执行")          #使用pytest.fixture()装饰一个函数成为fixture

def test_one():
    print("执行第一个用例")

def test_two(text):          #用例传入fixture函数名，以此来确认执行
    print("执行第二个用例")