import time

from selenium import webdriver
import yaml, time
import pytest

class TestWork:
    @pytest.mark.run(order=1)
    def test_work(self):
        opt = webdriver.ChromeOptions()
        print(111)
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("menu_contacts").click()
        return self.driver.get_cookies()

    @pytest.mark.run(order=2)
    def test_save_cookies(self):
        cookies = TestWork().test_work()
        # print(cookies)
        with open("./data/cookies_data.yaml", 'w', encoding="utf-8") as f:
            yaml.dump(cookies, f)

    @pytest.mark.run(order=3)
    def test_get_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        with open("./data/cookies_data.yaml", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#js_contacts98 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("test")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("001")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("#memberAdd_phone").send_keys("15698562147")
        self.driver.find_element_by_css_selector("#js_contacts98 > div > div.member_colRight > div > div:nth-child(4) > div > form > div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save").click()
        print(333)


