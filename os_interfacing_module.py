import os


f_name = 'Hello.txt'


f_path = 'root\pigeon'


ab_path = os.path.join(f_path, f_name)
print(ab_path)