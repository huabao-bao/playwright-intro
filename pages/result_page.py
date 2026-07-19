import json
class ResultPage:
    """
    代表httpbin 表单提交后到结果页面
    """
    def __init__(self, page):
        self.page = page

    def get_url(self) -> str:
        """返回当前页面URL"""
        return self.page.url
    
    def get_page_text(self) -> str:
        """返回页面上的 JSON 文本。只取pre文本, 用于快速验证提交的数据是否出现在结果中"""
        return self.page.locator("pre").inner_text()
    
    def get_form_data(self) -> dict:
        """返回 JSON 中的 form 字段（已解码中文）"""
        text = self.page.locator("pre").inner_text()
        data = json.loads(text)              # ← 解析 JSON，自动解码 \uXXXX → 中文
        return data.get("form", {})
