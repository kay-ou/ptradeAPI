#!/usr/bin/env python3
"""
检查文档链接有效性的脚本
"""
import os
import re
import glob

def check_file_exists(file_path, base_dir):
    """检查文件是否存在"""
    if file_path.startswith('/'):
        return os.path.exists(file_path)
    else:
        full_path = os.path.join(base_dir, file_path)
        return os.path.exists(full_path)

def extract_md_links(content):
    """提取markdown文件中的链接"""
    # 匹配 [text](link.md) 格式的链接
    pattern = r'\[([^\]]+)\]\(([^)]+\.md[^)]*)\)'
    return re.findall(pattern, pattern)

def check_document_links():
    """检查所有文档的链接"""
    print("🔍 开始检查文档链接...")
    
    # 获取所有markdown文件
    md_files = []
    md_files.extend(glob.glob('docs/**/*.md', recursive=True))
    md_files.append('README.md')
    
    total_links = 0
    broken_links = 0
    
    for md_file in md_files:
        print(f"\n📄 检查文件: {md_file}")
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ 无法读取文件: {e}")
            continue
            
        # 提取链接
        links = re.findall(r'\[([^\]]+)\]\(([^)]+\.md[^)]*)\)', content)
        
        for link_text, link_path in links:
            total_links += 1
            
            # 移除锚点
            clean_path = link_path.split('#')[0]
            
            # 计算相对路径
            base_dir = os.path.dirname(md_file)
            if clean_path.startswith('../'):
                # 相对路径
                full_path = os.path.normpath(os.path.join(base_dir, clean_path))
            elif clean_path.startswith('docs/'):
                # 从根目录开始的路径
                full_path = clean_path
            else:
                # 同目录下的文件
                full_path = os.path.join(base_dir, clean_path)
            
            if os.path.exists(full_path):
                print(f"  ✅ {link_text} -> {clean_path}")
            else:
                print(f"  ❌ {link_text} -> {clean_path} (文件不存在: {full_path})")
                broken_links += 1
    
    print(f"\n📊 检查结果:")
    print(f"总链接数: {total_links}")
    print(f"有效链接: {total_links - broken_links}")
    print(f"无效链接: {broken_links}")
    
    if broken_links == 0:
        print("🎉 所有链接都有效！")
        return True
    else:
        print("⚠️  发现无效链接，需要修复")
        return False

if __name__ == "__main__":
    check_document_links()
