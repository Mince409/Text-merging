import os
import tkinter as tk
from tkinter import filedialog, messagebox


def merge_txt_files(file_paths, output_path):
    try:
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
        messagebox.showinfo("完成", "文件合并完成！")
    except Exception as e:
        messagebox.showerror("错误", f"写入文件 {output_path} 时出错: {e}")


def select_input_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("TXT Files", "*.txt")])
    input_files_str = ', '.join(file_paths)
    input_files_entry.delete(0, tk.END)
    input_files_entry.insert(0, input_files_str)


def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)


def perform_merge():
    input_files = input_files_entry.get().split(', ')
    output_base_path = output_dir_entry.get()
    output_filename = output_filename_entry.get()

    if not input_files or not output_base_path or not output_filename:
        messagebox.showerror("错误", "请填写所有必填字段！")
        return

    output_file = os.path.join(output_base_path, output_filename)

    merge_txt_files(input_files, output_file)


# 创建主窗口
root = tk.Tk()
root.title("TXT 文件合并工具")

# 输入文件选择
input_files_label = tk.Label(root, text="选择输入文件:")
input_files_label.pack()
input_files_entry = tk.Entry(root, width=50)
input_files_entry.pack()
input_files_button = tk.Button(root, text="选择文件", command=select_input_files)
input_files_button.pack()

# 输出目录选择
output_dir_label = tk.Label(root, text="输出文件目录:")
output_dir_label.pack()
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.pack()
output_dir_button = tk.Button(root, text="选择目录", command=select_output_dir)
output_dir_button.pack()

# 输出文件名输入
output_filename_label = tk.Label(root, text="输出文件名 (需要含.txt后缀):")
output_filename_label.pack()
output_filename_entry = tk.Entry(root, width=50)
output_filename_entry.pack()

# 合并按钮
merge_button = tk.Button(root, text="合并文件", command=perform_merge)
merge_button.pack()

# 运行主循环
root.mainloop()
