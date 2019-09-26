# -*- coding:GB18030 -*-
import io
class Properties(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getdict(self, strName, dictName, value):
        # print(value)
        dictName[strName] = value
        return

    def getproperties(self):
        try:
            # print("开始读取文件")
            pro_file = io.open(self.fileName, 'r+', encoding='GB18030')
            # print(pro_file)
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                # print(line)
                if line.find('=') > 0:
                    # print("没#符号")
                    strs = line.split('=')
                    strs[1] = line[len(strs[0]) + 1:]
                    # print(strs[1])
                    self.__getdict(strs[0].strip(), self.properties, strs[1].strip())
        except Exception as e:
            print("解析异常:", e)
        else:
            pro_file.close()
        return self.properties
