# 统一 PDF 转换使用方式 - 更新日志

**日期**: 2026-03-29  
**版本**: v0.1.1

---

## 变更内容

### 统一 API 接口
- 在 `MDConverter` 类中添加 `to_pdf` 方法
- 统一 HTML 和 PDF 的使用方式，保持一致性
- 简化 PDF 转换流程，无需手动创建导出器实例

### 功能实现
- `MDConverter.to_pdf` 方法：一键转换 Markdown 到 PDF
- 自动处理输出路径（如果未指定，自动生成同名 PDF 文件）
- 复用 `MDConverter` 初始化时的 CSS 配置

### 代码优化
- 更新 PDF 示例代码，使用 `to_pdf` 方法
- 移除手动创建 `PDFExporter` 实例的步骤
- 保持与 `to_html` 方法相同的调用方式

---

## 影响范围

### 修改文件
- `markconv/converter.py` - 添加 `to_pdf` 方法
- `examples/pdf_example/pdf_example.py` - 更新示例代码

### 使用方式
```python
from markconv import MDConverter

# 创建转换器实例
converter = MDConverter(css_file='custom.css')

# 转换为 PDF
converter.to_pdf('input.md', 'output.pdf')

# 或自动生成输出路径
converter.to_pdf('input.md')  # 生成 input.pdf
```

---

## 对比

### 之前的方式
```python
from markconv import MDConverter
from markconv.exporters import PDFExporter

converter = MDConverter(css_file='custom.css')
parsed_data = converter.parser.parse_file('input.md')
pdf_exporter = PDFExporter(css_file='custom.css')
pdf_exporter.export(parsed_data, 'output.pdf')
```

### 现在的方式
```python
from markconv import MDConverter

converter = MDConverter(css_file='custom.css')
converter.to_pdf('input.md', 'output.pdf')
```

---

## Git 提交
- Commit ID: [待提交] - 统一 PDF 转换使用方式
