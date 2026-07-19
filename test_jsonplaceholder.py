from playwright.sync_api import sync_playwright, expect

def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        #1. 打开JSONPlaceholder首页
        page.goto("https://jsonplaceholder.typicode.com")

        #2. 断言标题包含 “JSONPlaceholder”
        expect(page).to_have_title("JSONPlaceholder - Free Fake REST API")

        #3. 断言页面主要标题是可见的
        main_heading = page.locator("h1").first
        expect(main_heading).to_be_visible()

        browser.close()
        
def test_navigate_to_posts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()

        #1. 打开首页
        page.goto("https://jsonplaceholder.typicode.com")

        #2. 点击导航栏中的 “/posts” 链接
        page.click("a[href='/posts']")

        #3. 断言url变成 /posts
        expect(page).to_have_url("https://jsonplaceholder.typicode.com/posts")

        browser.close()

def test_homepage_resources_count():
    """首页应该列出 6 种资源"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://jsonplaceholder.typicode.com")

        #定位表格中所有资源链接（每个/xxx是一个链接）
        resources = ["/posts", "/comments", "/albums", "/photos", "/todos", "/users"]
        for resource in resources:
            expect(page.locator(f"a[href='{resource}']").first).to_be_visible()

        browser .close()

def test_homepage_heading_text():
    """首页主题应该是 JSONPlaceholder"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://jsonplaceholder.typicode.com")

        #用 get_by_role 定位标题
        heading = page.get_by_role("heading", name = "JSONPlaceholder")
        expect(heading).to_have_text("JSONPlaceholder")

        browser.close()

def test_httpbin_from_fill():
    """测试表单填写和提交"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()

        # httpbin 自带一个 HTML 表单页面
        page.goto("http://127.0.0.1:8080/forms/post")

        # 填写表单
        page.get_by_label("Customer name:").fill("韩文杰")
        page.get_by_label("Telephone:").fill("1380013800")
        page.get_by_label("E-mail address:").fill("test@example.com")

        # 选择 pizza size (radio button)
        page.get_by_label("Medium").check()
        
        # 勾选 toppings （checkbox）
        page.get_by_label("Bacon").check()
        page.get_by_label("Extra Cheese").check()

        # 点击提交
        page.get_by_role("button", name = "Submit order").click()

        # 验证提交之后URL应该变化（httpbin 的 form post 会跳转到/post）
        expect(page).to_have_url("http://127.0.0.1:8080/post")

        browser.close()

def test_take_screenshot():
    """截图保存, 用于手动检查页面状态"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto("https://jsonplaceholder.typicode.com")

        # 全页截图
        page.screenshot(path = "homepage.png", full_page=True)

        browser.close()