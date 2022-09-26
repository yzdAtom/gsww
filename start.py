"""
@Project ：gsww 
@File    ：start.py
@IDE     ：PyCharm 
@Author  ：Atomyzd
@Useage    ：使用命令执行scrapy项目
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl gsww_spider".split(" "))
