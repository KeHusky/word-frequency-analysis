# -*- coding:utf-8 -*-

from selenium import webdriver
import time

if __name__ == "__main__":

    # 原生未标注语料目录
    nativeCorpusFilePath = "good.txt"
    # 存放所有评论
    comment = []
    # 启动浏览器
    browser = webdriver.Chrome()
    # 打开要抓取的新闻页面，修改搜狐新闻文件时，需将搜狐新闻文件的网页地址填入即可
    browser.get('https://movie.douban.com/subject/3742360/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h')
    # 打开文件
    nativeCorpusFile = open(nativeCorpusFilePath, "w", encoding="utf-8")
    # 根据XPath获取当前页的评论元素集合
    comment_current_elements = browser.find_elements_by_xpath('//div[@class="comment"]/p/span[@class="short"]')
    # 遍历当前页评论集合
    for i_comment in comment_current_elements:
        print(i_comment.text)
        comment.append(i_comment.text)

    # 循环获取评论
    while True:
        try:
            # 获取跳到下页的链接元素
            isGet = browser.find_element_by_xpath('//div[@class="center"]/a[@class="next"]')
            # 点击事件，获取后续评论
            isGet.click()
            time.sleep(3)
            comment_next_elements = browser.find_elements_by_xpath('//div[@class="comment"]/p/span[@class="short"]')
            for i_comment in comment_next_elements:
                print(i_comment.text)
                comment.append(i_comment.text)
                nativeCorpusFile.writelines(i_comment.text)
                nativeCorpusFile.write("\n")
        except:
            print("An exception occurred")
            # 关闭文件及浏览器
            nativeCorpusFile.close()
            browser.close()


