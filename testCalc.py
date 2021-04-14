# coding:utf-8
# author:ck18
# data:2021-04-09
import pytest

@pytest.mark.parametrize('x, y', [(1, 2), (0, 6)] )
class TestCalc:
    def setup(self):
        print("-----开始计算------")

    def teardown(self):
        print("------结束计算------")

    def test_add(self, x, y):
        print(("x+y=", x + y))
        return x + y

    def test_sub(self, x, y):
        print(("x-y=", x - y))
        return x - y

    def test_mult(self, x, y):
        print(("x*y=", x * y))
        return x * y

    def test_division(self, x, y):
        # pytest.xfail(reason='除数不能为0')
        print("x/y=", x / y)
        return x / y


if __name__ == '__main__':
    pytest.main(['-s','-r','testCalc.py'])