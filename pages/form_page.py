class FormPage:
    """
    代表 httpbin 的表单页面（/forms/post）
    """
    def __init__(self, page, base_url="http://127.0.0.1:8080"):
        self.page = page
        self.base_url = base_url

    def navigate(self):
        """导航到表单页面"""
        self.page.goto(f"{self.base_url}/forms/post")

    def fill_customer_name(self, name: str):
        """填写客户姓名"""
        self.page.get_by_label("Customer name:").fill(name)

    def fill_telephone(self, phone: str):
        """填写客户电话"""
        self.page.get_by_label("Telephone:").fill(phone)

    def fill_email(self, email: str):
        """填写email"""
        self.page.get_by_label("E-mail address:").fill(email)

    def select_pizza_size(self, size: str):
        """填写pizza 大小"""
        self.page.get_by_label(size).check()

    def select_Preferred_delivery_time(self, time: str):
        """填写配送时间"""
        self.page.get_by_label("Preferred delivery time").fill(time)

    def fill_delivery_instructions(self, comments: str):
        """填写配送描述"""
        self.page.get_by_label("Delivery instructions").fill(comments)

    def add_topping(self, *toppings: str):
        """勾选一个 toppings 参数："Bacon", "Extra Cheese", "Onion", "Mushroom" """
        for topping in toppings:
            self.page.get_by_label(topping).check()

    def submit_order(self):
        """
        点击提交按钮，返回结果页面的Page Object
        返回：ResultPage 对象，用于验证提交结果
        """
        self.page.get_by_role("button", name = "Submit order").click()
        # 等待跳转后的页面加载完成。 httpbin 的表单提交之后跳转到 /post
        self.page.wait_for_url("**/post*")
        from pages.result_page import ResultPage
        return ResultPage(self.page)