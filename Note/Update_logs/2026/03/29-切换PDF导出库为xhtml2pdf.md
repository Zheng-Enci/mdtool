# 将 PDF 导出库从 WeasyPrint 切换到 xhtml2pdf

## 修改原因
WeasyPrint 在 Windows 上需要安装复杂的系统依赖（Pango、GTK、GLib 等），安装困难且容易出错。xhtml2pdf 是纯 Python 库，无需系统依赖，安装简单。

## 修改内容

### 1. setup.py
- 将 `weasyprint>=68.1` 替换为 `xhtml2pdf>=0.2.17`

### 2. markconv/exporters/pdf_exporter.py
- 将 `_html_to_pdf` 方法中的 WeasyPrint 导入替换为 xhtml2pdf
- 修改 PDF 生成方式：
  ```python
  # 旧代码（WeasyPrint）
  from weasyprint import HTML
  HTML(string=html_content).write_pdf(output_path)
  
  # 新代码（xhtml2pdf）
  from xhtml2pdf import pisa
  with open(output_path, 'wb') as pdf_file:
      pisa.CreatePDF(html_content, dest=pdf_file)
  ```

### 3. requirements.txt
- 移除 WeasyPrint 及其依赖：
  - weasyprint==68.1
  - cssselect2==0.9.0
  - pydyf==0.12.1
  - pyphen==0.17.2
  - tinycss2==1.5.1
  - tinyhtml5==2.1.0
  - zopfli==0.4.1
- 添加 xhtml2pdf 及其依赖：
  - xhtml2pdf==0.2.5
  - html5lib==1.1
  - reportlab==4.2.5
  - six==1.17.0

## 优势
- ✅ 安装简单：`pip install xhtml2pdf` 即可
- ✅ 无系统依赖：纯 Python 实现
- ✅ 跨平台一致：Windows、Linux、macOS 安装方式相同
- ✅ CSS 支持足够：支持基本的 CSS 样式

## 注意事项
- ⚠️ xhtml2pdf 的 CSS 支持不如 WeasyPrint 完善
- ⚠️ 中文显示可能需要配置字体（已在代码中内置中文字体支持）
- ⚠️ 复杂的 CSS 布局可能不完全支持

## 测试建议
建议运行 PDF 示例验证功能正常：
```bash
cd examples/pdf_example
python pdf_example.py
```

## 更新记录
### 2026-03-29
- 清理 requirements.txt，移除 WeasyPrint 及其依赖
- 保留 xhtml2pdf==0.2.17 作为 PDF 导出库
- 移除的依赖：
  - weasyprint==68.1
  - cssselect2==0.9.0
  - pydyf==0.12.1
  - pyphen==0.17.2
  - tinycss2==1.5.1
  - tinyhtml5==2.1.0
  - zopfli==0.4.1

### 2026-03-29 (第二次更新)
- requirements.txt 已更新，同时包含 WeasyPrint 和 xhtml2pdf
- 修改 pdf_exporter.py 支持两个 PDF 库
- 优先使用 WeasyPrint，如果未安装则自动降级到 xhtml2pdf
- 这样既保证了高级功能（WeasyPrint 的 CSS 支持），又保证了兼容性（xhtml2pdf 的简单安装）

### 2026-03-29 (第三次更新)
- 解决 xhtml2pdf 中文乱码问题
- 添加 `_register_chinese_fonts()` 函数注册中文字体
- 支持 Windows 系统字体：微软雅黑、黑体、宋体
- 在使用 xhtml2pdf 生成 PDF 前自动注册中文字体
- 添加 `encoding='UTF-8'` 参数到 pisa.CreatePDF
- 添加 `_link_callback()` 函数处理相对路径

### 2026-03-29 (第四次更新)
- 移除 HTML CSS 中的 `@font-face` 规则
- xhtml2pdf 不支持 CSS `@font-face` 引用本地字体文件
- 仅通过 ReportLab 的 `pdfmetrics.registerFont()` 注册字体

### 2026-03-29 (第五次更新)
- 创建 `fonts/` 目录并复制 Windows 系统中文字体文件
- 修改 `_link_callback()` 函数支持 `fonts/` 相对路径
- 在 HTML CSS 中重新添加 `@font-face` 规则，使用相对路径引用字体文件
- 字体文件包括：msyh.ttc、msyhbd.ttc、simhei.ttf、simsun.ttc

### 2026-03-29 (第六次更新)
- 发现 `.ttc` 文件（TrueType Collection）在 xhtml2pdf 中无法正常加载
- 改用 `.ttf` 字体文件替代 `.ttc` 文件
- 复制的中文字体文件：simhei.ttf、simkai.ttf、simfang.ttf、simsunb.ttf
- 更新 `_register_chinese_fonts()` 函数使用 `.ttf` 文件
- 更新 HTML CSS 中的 `@font-face` 规则使用 `.ttf` 文件

### 2026-03-29 (第七次更新)
- 修改 `_link_callback()` 函数返回绝对路径
- 使用 `os.path.abspath()` 确保字体文件路径为绝对路径
- 解决 xhtml2pdf 无法打开临时字体文件的问题

### 2026-03-29 (第八次更新)
- 发现 xhtml2pdf 的 `@font-face` 支持有严重问题
- 完全移除 HTML CSS 中的 `@font-face` 规则
- 仅依赖 ReportLab 的 `pdfmetrics.registerFont()` 注册字体
- 通过 CSS `font-family` 指定已注册的字体名称

### 2026-03-29 (第九次更新)
- 添加字体注册调试信息，打印成功/失败状态
- 帮助诊断字体加载问题