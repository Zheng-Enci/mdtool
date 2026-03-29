import os
from typing import Dict, Any


class MarkdownParser:
    """
    Markdown 解析器类
    
    用于解析 Markdown 文件和内容，提取标题、元数据等信息
    
    Attributes:
        encoding (str): 文件编码格式，默认为 'utf-8'
    """
    
    def __init__(self, encoding: str = 'utf-8'):
        """
        初始化 Markdown 解析器
        
        Args:
            encoding (str): 文件编码格式，默认为 'utf-8'
        """
        self.encoding = encoding

    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """
        解析 Markdown 文件
        
        从指定路径读取 Markdown 文件，并解析其内容
        
        Args:
            file_path (str): Markdown 文件的路径
            
        Returns:
            Dict[str, Any]: 包含解析结果的字典，包括：
                - content: 原始 Markdown 内容
                - title: 提取的标题
                - metadata: 元数据字典
                
        Raises:
            FileNotFoundError: 当文件不存在时抛出异常
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding=self.encoding) as f:
            content = f.read()

        return self.parse_content(content)

    def parse_content(self, content: str) -> Dict[str, Any]:
        """
        解析 Markdown 内容字符串
        
        直接解析 Markdown 内容字符串，提取标题和元数据
        
        Args:
            content (str): Markdown 内容字符串
            
        Returns:
            Dict[str, Any]: 包含解析结果的字典，包括：
                - content: 原始 Markdown 内容
                - title: 提取的标题
                - metadata: 元数据字典
        """
        return {
            'content': content,
            'title': self._extract_title(content),
            'metadata': self._extract_metadata(content)
        }

    def _extract_title(self, content: str) -> str:
        """
        从 Markdown 内容中提取标题
        
        查找第一个一级标题（# 开头）作为文档标题
        
        Args:
            content (str): Markdown 内容字符串
            
        Returns:
            str: 提取的标题，如果没有找到则返回 'Untitled'
        """
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        return 'Untitled'

    def _extract_metadata(self, content: str) -> Dict[str, str]:
        """
        从 Markdown 内容中提取元数据
        
        解析 YAML Front Matter 格式的元数据
        元数据位于文档开头的 --- 分隔符之间
        
        Args:
            content (str): Markdown 内容字符串
            
        Returns:
            Dict[str, str]: 元数据字典，键值对形式存储
        """
        metadata = {}
        lines = content.split('\n')
        
        in_metadata = False
        for line in lines:
            line = line.strip()
            if line == '---':
                in_metadata = not in_metadata
                continue
            if in_metadata and ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        return metadata
