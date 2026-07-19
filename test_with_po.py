import sys
sys.path.insert(0, '.') #让python 能找到 pages/目录
from pages.home_page import HomePage
from playwright.sync_api import expect

def test_homepage_title(page):
    """检验首页标题"""
    home = HomePage(page)
    home.navigate()
    expect(page).to_have_title("JSONPlaceholder - Free Fake REST API")

def test_homepage_heading_visible(page):
    """验证首页主标题可见"""
    home = HomePage(page)
    home.navigate()
    expect(home.get_main_heading()).to_be_visible()

def test_navigate_to_posts(page):
    """ 点击/posts 链接跳转到正确的界面"""
    home = HomePage(page)
    home.navigate()
    home.click_resources("posts")
    expect(page).to_have_url("https://jsonplaceholder.typicode.com/posts")


def tests_all_resources_visible(page):
    """ 验证所有6种资源在首页可见"""
    home = HomePage(page)
    home.navigate()
    resources = ["posts", "comments", "albums", "photos", "todos", "users"]
    for r in resources:
        assert home.is_resource_visible(r), f"{r} 不可见"