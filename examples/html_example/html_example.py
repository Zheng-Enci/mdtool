# 从 mdconvert 包中导入 MDConverter 类
from mdconvert import MDConverter


def html_basic_example():
    """
    HTML 转换基本使用示例
    
    该函数演示了如何使用 MDConverter 将 Markdown 文件转换为 HTML 文件
    包括：
    - 创建转换器实例（支持自定义 CSS 样式）
    - 指定输入和输出文件路径
    - 执行转换操作
    - 使用自定义 CSS 文件美化输出
    """
    # 打印示例标题
    print("HTML 转换基本使用示例")
    # 打印分隔线
    print("=" * 50)
    
    # 创建 MDConverter 实例，传入自定义 CSS 文件路径
    # 参数说明：
    #   - css_file: 自定义 CSS 样式文件的路径
    #     程序会读取该文件内容并插入到生成的 HTML 的 <style> 标签中
    #     自定义样式会覆盖或补充内置的默认样式
    #   - encoding: 文件编码格式，默认为 'utf-8'
    converter = MDConverter(css_file = "custom.css")
    
    # 定义输入的 Markdown 文件路径（使用原始字符串 r 避免转义问题）
    input_file = r'sample.md'
    # 定义输出的 HTML 文件路径（相对路径）
    output_file = 'examples/sample.html'
    

    # 调用 to_html 方法执行转换
    # 参数说明：
    #   - input_file: 输入的 Markdown 文件路径
    #   - output_file: 输出的 HTML 文件路径（如果目录不存在会自动创建）
    #   - wrap_html=True: 生成完整的 HTML 文档（包含 DOCTYPE、html、head、body 等标签）
    #     如果设置为 False，则只输出 HTML body 内容，适合嵌入到其他网页中
    converter.to_html(input_file, output_file, wrap_html=True)


# 当脚本被直接运行时，执行示例函数
# 如果脚本被导入为模块，则不会执行
if __name__ == '__main__':
    html_basic_example()
