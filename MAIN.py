import os

def merge_txt_files(file_paths, output_path):
    try:
        # 对文件路径列表进行排序
        sorted_file_paths = sorted(file_paths)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for file_path in sorted_file_paths:
                if os.path.exists(file_path) and file_path.endswith('.txt'):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as input_file:
                            content = input_file.read()
                            output_file.write(content)
                            output_file.write('\n')
                    except Exception as e:
                        print(f"读取文件 {file_path} 时出错: {e}")
                else:
                    print(f"文件 {file_path} 不存在或者不是 TXT 文件。")
    except Exception as e:
        print(f"写入文件 {output_path} 时出错: {e}")

if __name__ == "__main__":
    input_base_path = r'C:\Users\cisco\Desktop'
    # 要合并的 TXT 文件路径列表
    txt_files = [os.path.join(input_base_path, 'file1.txt'),
                 os.path.join(input_base_path, 'file2.txt'),
                 os.path.join(input_base_path, 'file3.txt'),
                 os.path.join(input_base_path, 'file4.txt')]
    output_base_path = r'C:\Users\cisco\Desktop'
    # 合并后的输出文件路径
    output_file = os.path.join(output_base_path, 'merged.txt')
    merge_txt_files(txt_files, output_file)
