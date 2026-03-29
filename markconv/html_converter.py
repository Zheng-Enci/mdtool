from typing import Optional
from .parsers import MarkdownParser
from .exporters import HTMLExporter


class MDConverter:
    """
    Markdown 转换器主类
    
    提供统一的接口将 Markdown 文件转换为 HTML 格式
    支持单个文件转换和批量转换
    
    Attributes:
        parser (MarkdownParser): Markdown 解析器实例
        html_exporter (HTMLExporter): HTML 导出器实例
    """
    
    def __init__(self, encoding: str = 'utf-8', css_file: Optional[str] = None):
        """
        初始化 Markdown 转换器
        
        Args:
            encoding (str): 文件编码格式，默认为 'utf-8'
            css_file (Optional[str]): 自定义 CSS 样式文件路径，可选
        """
        self.parser = MarkdownParser(encoding=encoding)
        self.html_exporter = HTMLExporter(css_file=css_file)

    def to_html(self, input_path: str, output_path: Optional[str] = None, wrap_html: bool = True) -> None:
        """
        将 Markdown 文件转换为 HTML
        
        该方法执行以下步骤：
        1. 验证输入文件是否存在
        2. 如果未指定输出路径，则根据输入文件名生成输出路径
        3. 解析 Markdown 文件
        4. 导出为 HTML 文件
        
        Args:
            input_path (str): 输入的 Markdown 文件路径
            output_path (Optional[str]): 输出的 HTML 文件路径
                如果为 None，则在输入文件同目录下生成同名 HTML 文件
            wrap_html (bool): 是否包装为完整的 HTML 文档，默认为 True
                如果为 False，则只输出 HTML body 内容
                
        Returns:
            str: 输出 HTML 文件的完整路径
            
        Raises:
            FileNotFoundError: 当输入文件不存在时抛出异常
            
        Example:
            >>> converter = MDConverter()
            >>> converter.to_html('input.md', 'output.html')
            'output.html'
            >>> converter.to_html('input.md')
            'input.html'
        """

        parsed_data = self.parser.parse_file(input_path)
        
        html_exporter = HTMLExporter(css_file=self.html_exporter.css_file, wrap_html=wrap_html)
        html_exporter.export(parsed_data, output_path)



