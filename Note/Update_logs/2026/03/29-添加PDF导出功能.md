# 添加 PDF 导出功能 - 更新日志

**日期**: 2026-03-29  
**版本**: v0.1.1

---

## 变更内容

### 新增 PDF 导出器
- 新增 `markconv/exporters/pdf_exporter.py` 文件
- 实现 `PDFExporter` 类，支持将 Markdown 转换为 PDF
- 复制 HTML 导出器的核心代码，实现独立的 PDF 导出功能

### 功能实现
- `_markdown_to_html` 函数：将 Markdown 转换为 HTML
- `_wrap_html` 方法：包装 HTML 文档结构
- `_get_custom_css` 方法：支持自定义 CSS 样式
- `_html_to_pdf` 方法：使用 weasyprint 库将 HTML 转换为 PDF

### 依赖更新
- 在 `setup.py` 中将 weasyprint 设为必需依赖
- PDF 功能需要安装 `weasyprint>=68.1`
- 安装 markconv 时自动安装 weasyprint

### 代码优化
- 移除 `_html_to_pdf` 方法中的 try-except 处理
- weasyprint 是必需依赖，无需检查安装状态

---

## 影响范围

### 新增文件
- `markconv/exporters/pdf_exporter.py` - PDF 导出器实现

### 修改文件
- `markconv/exporters/__init__.py` - 导出 PDFExporter
- `setup.py` - 添加 PDF 可选依赖

### 使用方式
```python
from markconv import MDConverter
from markconv.exporters import PDFExporter

# 使用 PDF 导出器
pdf_exporter = PDFExporter(css_file='custom.css')
pdf_exporter.export(parsed_data, 'output.pdf')
```

---

## Git 提交
- Commit ID: 2dfd831 - 添加 PDF 导出器框架
- Commit ID: f299a9b - 实现 PDF 导出器基础功能
- Commit ID: b4652cb - 实现 HTML 转 PDF 功能
- Commit ID: 5ea749c - 将 weasyprint 设为必需依赖
- Commit ID: f9112ed - 移除 PDF 导出器的 try-except 处理
