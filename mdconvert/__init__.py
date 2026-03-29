"""
mdtool - Markdown 转换工具库

一个强大的 Python 库，用于将 Markdown 文件转换为 HTML 格式。

主要功能：
- Markdown 到 HTML 的转换
- 批量文件转换
- 自定义样式支持
- 中文友好

Example:
    >>> from mdtool import MDConverter
    >>> converter = MDConverter()
    >>> converter.to_html('input.md', 'output.html')
"""

from .html_converter import MDConverter

__version__ = '0.1.0'
__all__ = ['MDConverter']
