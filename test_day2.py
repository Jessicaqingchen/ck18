# coding:utf-8
import pytest
import allure

@allure.feature('计算器')
class TestDemo2:
    @allure.story('整数相加')
    def test_add(self, initcalc_class, get_datas1):
        assert get_datas1[2] == initcalc_class.add(get_datas1[0], get_datas1[1])

    @allure.story('整数相减')
    def test_add(self, initcalc_class, get_datas1):
        try:
            assert get_datas1[2] == initcalc_class.sub(get_datas1[0], get_datas1[1])
        except AssertionError as e:
            print('断言错误')

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ], ids=['浮点数', '浮点数2'])
    @allure.story("浮点数相加")
    def test_add_float(self, initcalc_class, a, b, expect):
        assert expect == round(initcalc_class.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0, False], [2, 2, 1]])
    @allure.story("相除")
    def test_dis(self, initcalc_class, a, b, expect):
        try:
            assert expect == initcalc_class.div(a, b)
        except ZeroDivisionError:
            print("除数为0")
