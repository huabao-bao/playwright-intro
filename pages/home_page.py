class HomePage:
    def __init__(self, page):
        """
        page: Playwright 的 page 对象
        """
        self.page = page

    def navigate(self):
        """
        导航到JSONPlaceholder 首页
        """
        self.page.goto("https://jsonplaceholder.typicode.com")

    def click_resources(self, name: str):
        """
        点击首页的资源链接
        name不带斜杠，如“posts”
        """
        self.page.locator(f"a[href = '/{name}']").first.click()
        
    def get_main_heading(self):
        """返回页面主标题元素(第一个 h1)"""
        return self.page.locator("h1").first
    
    def is_resource_visible(self, name:str) -> bool:
        """ 检查某个资源链接在页面上是否可见"""
        return self.page.locator(f"a[href = '/{name}']").first.is_visible