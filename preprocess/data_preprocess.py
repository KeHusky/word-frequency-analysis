# -*- coding:utf-8 -*-

# 无汉字
# @XXXX

import numpy as np

class Processer(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.texts = []
        self.results = []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip("\n")
                self.texts.append(line)

    def _hasChinese(self, text):
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    def _isUserId(self, text):
        # re.sub("@[A-Za-z0-9_\-\u4e00-\u9fa5]+", "", text)
        if '@' in text:
            return True
        else:
            return False

    def getProcessResult(self):
        for text in self.texts:
            flag_a = self._hasChinese(text)
            flag_b = self._isUserId(text)
            if not flag_a or flag_b:
                continue
            else:
                self.results.append(text)
        return self.results

if __name__ == "__main__":
    type_file = "bad"
    file_path = "../web_scrapy/{}.txt".format(type_file)
    data_processer = Processer(file_path)
    results = data_processer.getProcessResult()
    print(len(results), results)
    np.save("list_{}.npy".format(type_file), results)