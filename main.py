from mdconvert import MDConverter


def main():
    print("mdconvert - Markdown 转 HTML 工具")
    print("=" * 50)
    
    converter = MDConverter()
    
    input_file = r'F:\BaiduSyncdisk\ZhengEnCi\mdtool\README.md'
    output_file = 'examples/sample.html'
    
    print(f"正在转换: {input_file}")
    print(f"输出到: {output_file}")
    
    try:
        result = converter.to_html(input_file, output_file)
        print(f"\n✅ 转换成功！")
        print(f"HTML 文件已保存到: {result}")
    except FileNotFoundError as e:
        print(f"\n❌ 错误: {e}")
        print("请确保输入文件存在")
    except Exception as e:
        print(f"\n❌ 转换失败: {e}")


if __name__ == '__main__':
    main()
