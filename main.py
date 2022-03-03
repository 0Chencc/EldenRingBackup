import os
import sys
import time
import zipfile

elden_ring_save_dir_path = os.path.expanduser('~\\AppData\\Roaming\\EldenRing')
print(f"存档位置为：{elden_ring_save_dir_path}")
zip_name = f'.\\backup {time.strftime("%Y-%m-%d %H时%M分%S秒", time.localtime())}.zip'
back_zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
for path, dirs, files in os.walk(elden_ring_save_dir_path):
    tmp = path.replace(elden_ring_save_dir_path, '')
    for name in files:
        full_name = os.path.join(path, name)
        name = tmp + '\\' + name
        back_zip.write(full_name, name)
back_zip.close()
print(f'备份完成\n存档文件储存在：{sys.path[0]}{zip_name.strip(".")}')
