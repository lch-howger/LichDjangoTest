import urllib.request
import re
import sqlite3
from lxml import html

base_url = 'https://www.d1xz.net/yunshi/'
sql_insert_task = "REPLACE INTO stars VALUES('{}','{}','{}','{}')"

db = sqlite3.connect('./stars.db')

for i in range(5):
    id01 = ''
    time = ''
    if i == 0:
        id01 = '00'
        time = 'today'
    elif i == 1:
        id01 = '01'
        time = 'tomorrow'
    elif i == 2:
        id01 = '02'
        time = 'week'
    elif i == 3:
        id01 = '03'
        time = 'nextweek'
    elif i == 4:
        id01 = '04'
        time = 'month'
    for j in range(12):
        id02 = ''
        star = ''
        if j == 0:
            id02 = '00'
            star = 'Aries'
        elif j == 1:
            id02 = '01'
            star = 'Taurus'
        elif j == 2:
            id02 = '02'
            star = 'Gemini'
        elif j == 3:
            id02 = '03'
            star = 'Cancer'
        elif j == 4:
            id02 = '04'
            star = 'Leo'
        elif j == 5:
            id02 = '05'
            star = 'Virgo'
        elif j == 6:
            id02 = '06'
            star = 'Libra'
        elif j == 7:
            id02 = '07'
            star = 'Scorpio'
        elif j == 8:
            id02 = '08'
            star = 'Sagittarius'
        elif j == 9:
            id02 = '09'
            star = 'Capricorn'
        elif j == 10:
            id02 = '10'
            star = 'Aquarius'
        elif j == 11:
            id02 = '11'
            star = 'Pisces'

        # 拼接id
        id = id01 + id02

        # 拼接url
        url = base_url + time + '/' + star

        # 请求得到response
        response = urllib.request.urlopen(url)
        decode = response.read().decode()

        # 用etree来解析
        etree = html.etree
        etree_html = etree.HTML(decode)

        # 从html中取出元素class
        result = ''
        if i == 0 or i == 1:
            xpath = etree_html.xpath('//*[@class="det"] ')
        elif i == 2 or i == 3 or i == 4:
            xpath = etree_html.xpath('//*[@class="det week_det"] ')

        result = etree.tostring(xpath[0], encoding='utf-8').decode('utf-8')
        print(result)

        # 把记录添加到数据库
        cursor = db.cursor()
        cursor.execute(sql_insert_task.format(id, star, time, result))
        db.commit()
        cursor.close()
