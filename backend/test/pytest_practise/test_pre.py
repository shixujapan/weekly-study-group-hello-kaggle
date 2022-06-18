import py
import pytest
import fixture

class TestClass:
    
    def setup_class(self):
        print("setup_class：类中所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：类中所有用例执行之前")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def test_one(self):
        print("执行第一个用例")

    def test_two(self):
        print("执行第二个用例")

def setup_module():
    print("setup_module：整个.py模块只执行一次")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次")

def setup_function():
    print("setup_function：每个方法用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个方法用例结束前都会执行")

def test_three():
        print("执行第三个用例")