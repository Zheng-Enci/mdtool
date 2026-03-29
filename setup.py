"""
mdconvert 包的 setup 配置文件
用于将项目发布到 PyPI
"""

from setuptools import setup, find_packages

# 读取 README.md 作为长描述（会显示在 PyPI 网站上）
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# 调用 setup 函数配置包信息
setup(
    # ===== 基本信息 =====
    
    # 包名称（用户执行 pip install 时使用的名称）
    name='mdconvert',
    
    # 版本号（遵循语义化版本规范：主版本.次版本.修订版本）
    version='0.1.0',
    
    # 作者姓名
    author='Zheng EnCi',
    
    # 作者邮箱（用于联系和问题反馈）
    author_email='zheng_enci@qq.com',
    
    # 简短描述（显示在 PyPI 搜索结果中）
    description='一个强大的 Markdown 转换工具库',
    
    # 长描述（显示在 PyPI 包详情页，从 README.md 读取）
    long_description=long_description,
    
    # 长描述的内容类型（告诉 PyPI 是 Markdown 格式）
    long_description_content_type='text/markdown',
    
    # 项目主页 URL（显示在 PyPI 网站上）
    url='https://github.com/Zheng-Enci/mdconvert',
    
    # ===== 包配置 =====
    
    # 自动查找所有 Python 包（mdtool 及其子包）
    packages=find_packages(),
    
    # ===== 分类器（帮助用户在 PyPI 上搜索和发现包）=====
    classifiers=[
        # 开发状态：3 - Alpha（早期开发版本）
        'Development Status :: 3 - Alpha',
        
        # 目标受众：开发者
        'Intended Audience :: Developers',
        
        # 主题：软件开发 -> Python 模块
        'Topic :: Software Development :: Libraries :: Python Modules',
        
        # 许可证：MIT 开源许可证
        'License :: OSI Approved :: MIT License',
        
        # 编程语言：Python 3
        'Programming Language :: Python :: 3',
        
        # 编程语言：Python 3.13 特定版本
        'Programming Language :: Python :: 3.13',
        
        # 操作系统：操作系统无关（跨平台）
        'Operating System :: OS Independent',
    ],
    
    # ===== Python 版本要求 =====
    
    # 要求 Python 版本 >= 3.13
    python_requires='>=3.13',
    
    # ===== 依赖项（安装包时自动安装的依赖库）=====
    install_requires=[
        # 需要 markdown2 库，版本 >= 2.5.5
        'markdown2>=2.5.5',
    ],
    
    # ===== 搜索关键词（帮助用户搜索包）=====
    
    # 用户搜索时可以使用的关键词
    keywords='markdown html converter',
    
    # ===== 项目链接（显示在 PyPI 网站上）=====
    project_urls={
        # 问题反馈链接
        'Bug Reports': 'https://github.com/Zheng-Enci/mdconvert/issues',
        
        # 源代码链接
        'Source': 'https://github.com/Zheng-Enci/mdconvert',
        
        # 文档链接（指向 README.md）
        'Documentation': 'https://github.com/Zheng-Enci/mdconvert/blob/master/README.md',
    },
)