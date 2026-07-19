import sys
sys.path.insert(0, '.')
from pages.form_page import FormPage
from playwright.sync_api import expect

def test_fill_and_submit_form(page):
    """填写 httpbin 表单-> 提交-> 验证结果"""
    form = FormPage(page, base_url= "http://httpbin.org")
    form.navigate()

    #逐字段填写
    form.fill_customer_name("韩文杰")
    form.fill_telephone("18919374451")
    form.fill_email("test@example.com")
    form.select_pizza_size("Medium")
    form.add_topping("Bacon", "Extra Cheese", "Onion")
    form.select_Preferred_delivery_time("12:30")
    form.fill_delivery_instructions("Please be hot")

    #提交表格 ->  拿到结果页的PO
    result = form.submit_order()

    #验证结果页
    expect(page).to_have_url(result.get_url())

    #验证填写的数据出现在结果中
    #解析 JSON 后取字段
    form_data = result.get_form_data()
    assert form_data["custname"] == "韩文杰"
    assert form_data["custtel"] == "18919374451"
    assert form_data["custemail"] == "test@example.com"
    assert form_data["delivery"] == "12:30"
    assert form_data["comments"] == "Please be hot"

    # radio 和 checkbox 也可以验证
    assert form_data["size"] == "medium"
    assert "bacon" in form_data["topping"]
    assert "cheese" in form_data["topping"]


    print("CI 表单提交测试通过 ✅")
    