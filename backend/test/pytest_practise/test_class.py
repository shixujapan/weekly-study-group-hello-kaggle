import pytest
@pytest.fixture(scope="module",params=['test1','test2'])
def text(request):
    print("开始执行")
    yield request.param
    print("执行完毕")

def test_one(text):
    print("执行第一个用例")
    print(text)

def test_two(text):
    print("执行第二个用例")