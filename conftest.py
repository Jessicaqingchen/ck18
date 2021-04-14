# coding:utf-8
import pytest, yaml
from ck18.Calculator import Calculator
from typing import List

@pytest.fixture(autouse=True)
def a():
    print("测试auto")

def get_datas():
    with open('./data/test_demo.yaml') as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.fixture(params=get_datas()['int_datas'], ids=get_datas()['ids'])
def get_datas1(request):
    return request.param

@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc
    # teardown
    print("teardown")

def pytest_collection_modifyitems(session, config, items: List):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # if 'test_add' in item.name:
        #     item.add_marker(pytest.mark.test_add)
        # elif 'test_dev' in item.name:
        #     item.add_marker(pytest.mark.test_dev)

