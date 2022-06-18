import pytest

@pytest.fixture()
def text():
    print("开始执行")
    yield
    print("执行完毕")