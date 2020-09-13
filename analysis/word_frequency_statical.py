# -*- coding:utf-8 -*-

import jieba
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 得到三个类文本List
    type_files = ["good", "bad", "not_bad"]
    list_corpus = []
    for type_file in type_files:
        npy_file_path = "../preprocess/list_{}.npy".format(type_file)
        list_corpus.append(list(np.load(npy_file_path)))
    # print(len(list_corpus), list_corpus)

    # 对每一句分词
    # jieba 中 cut、cut_for_search、区别
    documents = []
    sentences = []
    for corpus in list_corpus:
        for sent in corpus:
            sentences.append(list(jieba.cut(sent)))
        documents.append(sentences)

    print(len(documents), documents)

    # 统计文档集合中的词频 , 优化亮点
    documents_words = []
    for document in documents:
        for sentence in document:
            for word in sentence:
                documents_words.append(word)

    # 去重获得词表
    vocabs_table = list(set(documents_words))

    # 过滤字符集合
    filter_chars = ['，', '。', ' ', '！', '《', '》', '；', ',', '~', '-']

    vocab_dictionary = {}
    for vocab in vocabs_table:
        if vocab not in filter_chars:
            vocab_dictionary[vocab] = documents_words.count(vocab)

    c = sorted(vocab_dictionary.items(), key=lambda x: x[1], reverse=True)
    print(c)

    dataframe = pd.DataFrame(c, columns={'词', '词频'})
    print(dataframe)
    # dataframe.to_excel("vocab_dictionary.xlsx")

    analysis_words = ['姜文', '周润发', '黑色幽默', '他妈的', '惊喜', '剧情', '台词', '演技', '逻辑']

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    # 构建数据
    x = analysis_words
    y = []
    for key_word in analysis_words:
        y.append(vocab_dictionary[key_word])
    # 绘图
    plt.bar(x=x, height=y, label='词频', color='steelblue', alpha=0.8)
    # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x1, yy in zip(x, y):
        plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
    # 设置标题
    plt.title("《让子弹飞》")
    # 为两条坐标轴设置名称
    plt.xlabel("关键词")
    plt.ylabel("出现次数")
    # 显示图例
    plt.legend()
    # plt.savefig("a.jpg")
    plt.show()


