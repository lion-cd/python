#!/bin/env python
# -*- coding:GB18030 -*-

import sys
import io
from properties import Properties


def replace(file_path, old_str, new_str):
    try:
        f = io.open(file_path, 'r+', encoding='GB18030')
        all_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_lines:
            # print(line)
            line = line.replace(old_str, new_str)
            f.write(line)
        f.close()
        # print("修改成功")
    except IOError:
        print("失败")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("need 1 params")
        sys.exit(1)

    file_name = sys.argv[1]
    dictProperties = Properties(file_name).getproperties()
    # print(dictProperties.get("cn.com.agree.ab.communication/name"))
    name = dictProperties.get("cn.com.agree.ab.communication/name")
    strs = name.split('_')
    shortname = dictProperties.get("cn.com.agree.ab.communication/shortname")
    if "1" in strs[2]:
        xh = "01"
        # print("01")
    elif "2" in strs[2]:
        xh = "02"
        # print("02")
    elif "3" in strs[2]:
        xh = "03"
        # print(xh)
    dst_str = strs[1] + xh;
    # print("输出结果：", strs[1] + xh)
    # if len(sys.argv) < 4:
    #     print("need 3 params"
    #     sys.exit(1)
    # file_name = sys.argv[1]
    # src_str = sys.argv[2]
    # dst_str = sys.argv[3]
    replace(file_name, shortname, dst_str)
