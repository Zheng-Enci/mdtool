"""
PDF 导出器模块

用于将 Markdown 转换为 PDF 格式
"""

import os
from typing import Dict, Any
import markdown2


def _register_chinese_fonts():
    """
    注册中文字体以支持中文显示
    
    xhtml2pdf 基于 ReportLab，默认不支持中文，需要手动注册中文字体
    """
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    
    windows_fonts = [
        ('Microsoft YaHei', 'C:/Windows/Fonts/msyh.ttc', 0),
        ('Microsoft YaHei Bold', 'C:/Windows/Fonts/msyhbd.ttc', 0),
        ('SimHei', 'C:/Windows/Fonts/simhei.ttf', 0),
        ('SimSun', 'C:/Windows/Fonts/simsun.ttc', 0),
    ]
    
    for font_name, font_path, subfont_index in windows_fonts:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path, subfontIndex=subfont_index))
            except:
                pass
    
    registerFontFamily('Microsoft YaHei', normal='Microsoft YaHei', bold='Microsoft YaHei Bold')


def _link_callback(uri, rel):
    """
    链接回调函数，用于处理相对路径
    
    Args:
        uri: URI 路径
        rel: 相对路径
        
    Returns:
        处理后的路径
    """
    if uri.startswith('http://') or uri.startswith('https://'):
        return uri
    
    return os.path.join(os.path.dirname(__file__), uri)


def _markdown_to_html(markdown_content: str) -> str:
    """
    将 Markdown 内容转换为 HTML

    使用 markdown2 库进行转换，启用多种扩展功能

    Args:
        markdown_content (str): Markdown 格式的内容字符串

    Returns:
        str: 转换后的 HTML 内容

    Note:
        启用的扩展功能包括：
        - fenced-code-blocks: 围栏代码块
        - tables: 表格支持
        - toc: 目录生成
        - code-friendly: 代码友好模式
        - footnotes: 脚注
        - strike: 删除线
        - task_list: 任务列表
    """
    extras = [
        'fenced-code-blocks',
        'tables',
        'toc',
        'code-friendly',
        'footnotes',
        'strike',
        'task_list'
    ]
    return markdown2.markdown(markdown_content, extras=extras)


class PDFExporter:
    """
    PDF 导出器类
    
    将解析后的 Markdown 数据转换为 PDF 文件
    
    Attributes:
        css_file (str): 自定义 CSS 样式文件路径，默认为 None
    """
    
    def __init__(self, css_file: str = None):
        """
        初始化 PDF 导出器
        
        Args:
            css_file (str): 自定义 CSS 样式文件路径，可选
        """
        self.css_file = css_file

    def export(self, parsed_data: Dict[str, Any], output_path: str) -> None:
        """
        将解析后的 Markdown 数据导出为 PDF 文件
        
        该方法执行以下步骤：
        1. 将 Markdown 内容转换为 HTML
        2. 将 HTML 包装在完整的 HTML 文档结构中
        3. 将 HTML 转换为 PDF
        
        Args:
            parsed_data (Dict[str, Any]): 包含 Markdown 解析结果的字典
                - content: Markdown 内容
                - title: 文档标题（可选）
            output_path (str): 输出 PDF 文件的路径
        """
        html_content = _markdown_to_html(parsed_data['content'])
        html_content = self._wrap_html(html_content, parsed_data.get('title', 'Document'))
        
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        self._html_to_pdf(html_content, output_path)

    def _wrap_html(self, body_content: str, title: str) -> str:
        """
        将 HTML 内容包装在完整的 HTML 文档结构中
        
        添加 HTML 头部、元数据和样式，创建完整的 HTML 文档
        
        Args:
            body_content (str): HTML 主体内容
            title (str): 文档标题
            
        Returns:
            str: 完整的 HTML 文档字符串
            
        Note:
            内置样式包括：
            - 中文字体支持（微软雅黑、黑体）
            - 标题样式
            - 代码块样式
            - 表格样式
            - 引用块样式
            - 链接和图片样式
        """
        custom_css = self._get_custom_css()
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <style>
                body {{
                    font-family: 'Microsoft YaHei', 'SimHei', 'SimSun', Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                    color: #333;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #2c3e50;
                    margin-top: 20px;
                    margin-bottom: 10px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Consolas', 'Monaco', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
                blockquote {{
                    border-left: 4px solid #ddd;
                    margin: 0;
                    padding-left: 20px;
                    color: #666;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                a {{
                    color: #3498db;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                }}
                hr {{
                    border: none;
                    border-top: 1px solid #ddd;
                    margin: 20px 0;
                }}
                {custom_css}
            </style>
        </head>
        <body>
            {body_content}
        </body>
        </html>
        """

    def _get_custom_css(self) -> str:
        """
        获取自定义 CSS 样式
        
        如果设置了自定义 CSS 文件，则读取并返回其内容
        
        Returns:
            str: CSS 样式字符串，如果没有设置或文件不存在则返回空字符串
        """
        if self.css_file and os.path.exists(self.css_file):
            with open(self.css_file, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def _html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        将 HTML 内容转换为 PDF 文件
        
        优先使用 WeasyPrint，如果失败则使用 xhtml2pdf
        
        Args:
            html_content (str): HTML 内容字符串
            output_path (str): 输出 PDF 文件的路径
        """
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        try:
            from weasyprint import HTML
            HTML(string=html_content).write_pdf(output_path)
        except ImportError:
            from xhtml2pdf import pisa
            _register_chinese_fonts()
            with open(output_path, 'wb') as pdf_file:
                pisa.CreatePDF(html_content, dest=pdf_file, encoding='UTF-8', link_callback=_link_callback)
