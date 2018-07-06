import allure,pytest
class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤001")
    def test_01(self):
        allure.attach("描述","输入用户名")
        assert 1

    # Severity：严重级别(BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL)
    @allure.step(title="测试步骤002")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_02(self):
        allure.attach("描述", "输入密码")
        assert 0
    # 设置优先级
    @allure.allure.serverity(pytest.allure.severity_level.MINOR)
    @pytest.step("这是对整个测试函数的描述")
    def test_03(self):
        allure.attach("点击","点击登录按钮")
        assert  1
        allure.attch('输入',"输入密码")
        assert 1