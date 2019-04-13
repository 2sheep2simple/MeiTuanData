# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 10:44
# @Author  : 2simple
# @Site    : 
# @File    : GuoGou.py
# @Software: PyCharm
import xlwt
from lxml import etree


def getdata(html):  # 从html里获取节点数据
    divs = html.xpath('//*[@id="app"]/div/div')
    names = divs[1].xpath('//div/div/div/div[1]/a/text()')  # 名稱
    nums = divs[1].xpath('//div/div/div/div[1]/div[1]/span[3]/text()')  # 評論數
    location = divs[1].xpath('//div/div/div/div[1]/div[2]/div[1]/span[1]/span[2]/text()')  # 地區
    kind = divs[1].xpath('//div/div/div/div[1]/div[2]/div[1]/span[1]/span[1]/text()')  # 種類
    address = divs[1].xpath('//div/div/div/div[1]/div[2]/div[1]/span[2]/text()')  # 详细地址
    score = divs[1].xpath('//div/div/div/div[1]/div[1]/span[2]/text()')  # 评分
    averageprice = divs[1].xpath('//div/div/div/div[1]/div[3]/div/span/text()')
    for i in names:
        if '\r\n                                ' in names:
            names.remove('\r\n                                ')
        if '\r\n                            ' in names:
            names.remove('\r\n                            ')
        if '\r\n                                ' in names:
            names.remove('\r\n                                ')
        if '\r\n                                ' in names:
            names.remove('\r\n                                ')
        if '\r\n                            ' in names:
            names.remove('\r\n                            ')
        if '\r\n                                ' in names:
            names.remove('\r\n                                ')
        if '\r\n                                    ' in names:
            names.remove('\r\n                                    ')
    for i in location:
        if '|' in location:
            location.remove('|')

    print(names)
    print(nums)
    print(location)
    print(kind)
    print(address)
    print(score)
    print(averageprice)
    print("获取到店铺名称的数量：", len(names))
    print("获取到店铺的评论的数量", len(nums))
    print("获取到地区的数量", len(location))
    print("获取到的店铺种类的数量", len(kind))
    print("获取到详细地址的数量", len(address))
    print("获取到的评分的数量", len(score))
    print("获取到的均价的数量", len(averageprice))
    data = [names, nums, location, kind, score, address,averageprice]
    return data


def doexcel(data,synthesis):
    excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = excel.add_sheet(cell_overwrite_ok=True,sheetname=synthesis)  # 創建sheet
    rows = len(data[0])  # 行數
    cols = len(data)  # 列數
    for col in range(0, cols):  # 寫入excel
        rows = len(data[col])
        for row in range(0, rows):
            sheet.write(row, col, data[col][row])
    # xls = synthesis+".xls"
    excel.save(r''+synthesis+'.xls')
    # Excel表保存为world.xls


if __name__ == "__main__":
    synthesis = input()
    html = "./"+synthesis+".html"
    html = etree.parse(html, etree.HTMLParser())
    data = getdata(html)
    doexcel(data, synthesis)

# 1.清除空格
# 2.清除人均等文字  人均¥ ¥ |
# 3.清除人评论等字   人评论
# 4.清除起等字      起