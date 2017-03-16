# coding:utf-8
import urllib2
import time
import random
import json
from PIL import Image

print ""

# 一号包
rad = random.randrange(0, 10000)
now = str(int(time.time()) * 100 + rad) + "0"
packoneHeader ={
    'Host': 'www.gsxt.gov.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'utf-8',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '__jsluid=f62265eaef032bc68316aa9732e03407; CNZZDATA1261033118=1815167979-1488259307-http%253A%252F%252Fgsxt.saic.gov.cn%252F%7C1489630931; Hm_lvt_cdb4bc83287f8c1282df45ed61c4eac9=1489631494,1489631614,1489632397,1489632399; UM_distinctid=15ad4c53e7c680-0c682ad44b9aa3-76276751-1fa400-15ad4c53e7d304; JSESSIONID=977607945B30239ECE38EEE3404FA223-n2:-1; tlb_cookie=115query_8080; Hm_lpvt_cdb4bc83287f8c1282df45ed61c4eac9=1489633319',
    'Connection': 'keep-alive'
}
request = urllib2.Request("http://www.gsxt.gov.cn/SearchItemCaptcha?v=" + now, headers=packoneHeader)
result = urllib2.urlopen(request).read()
print "一号包:   " + result + "\n"
one = json.loads(result)

# 二号包
rad = random.randrange(0, 10000)
now = str(int(time.time()) * 100 + rad) + "0"
packtwoHeader = {
    'Host': 'api.geetest.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
    'Cookie': 'GeeTestUser=53c440a337719bb4a6acf620fb256e39; Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4=1489631119,1489632094,1489632490; _ga=GA1.2.799249996.1489631119; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215ad4ef086731f-019423a1b707d6-76276751-2073600-15ad4ef0868355%22%7D; sensorsdata_is_new_user=true; _qddaz=QD.sp78ag.9d3o5g.j0brwo9a; Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4=1489632648',
    'Connection': 'keep-alive',
}
request = urllib2.Request("http://api.geetest.com/gettype.php?gt=" + one['gt'] + "&callback=geetest_" + now, headers=packtwoHeader)
result = urllib2.urlopen(request).read()
result = result[22:-1]
print "二号包:   " + result + "\n"
two = json.loads(result)

# 三号包
rad = random.randrange(0, 10000)
now = str(int(time.time()) * 100 + rad) + "0"
packthreeHeader = {
    'Host': 'api.geetest.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
    'Cookie': 'GeeTestUser=53c440a337719bb4a6acf620fb256e39; Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4=1489631119,1489632094,1489632490; _ga=GA1.2.799249996.1489631119; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215ad4ef086731f-019423a1b707d6-76276751-2073600-15ad4ef0868355%22%7D; sensorsdata_is_new_user=true; _qddaz=QD.sp78ag.9d3o5g.j0brwo9a; Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4=1489632648',
    'Connection': 'keep-alive',
}
request = urllib2.Request("http://api.geetest.com/get.php?"
                          "gt=" + one['gt'] + "&"
                          "challenge="+one['challenge']+"&"
                          "product=popup&"
                          "offline=false&"
                          "protocol=&"
                          "path=/static/js/geetest.5.10.10.js&"
                          "type=slide&"
                          "callback=geetest_" + now, headers=packthreeHeader)
result = urllib2.urlopen(request).read()
result = result[22:-1]
print "三号包:   " + result + "\n"
three = json.loads(result)

# 构造图片地址
bgUrl = "http://static.geetest.com/" + three['bg']
fullbgUrl = "http://static.geetest.com/" + three['fullbg']

# 下载图片
getPicHeader = {
    'Host': 'static.geetest.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-search-1.html',
    'origin': 'http://www.gsxt.gov.cn',
    'Connection': 'keep-alive',

}

request = urllib2.Request(bgUrl, headers=getPicHeader)
bgResult = urllib2.urlopen(request)
with open("bg.png", "wb") as f:
    f.write(bgResult.read())

request = urllib2.Request(fullbgUrl, headers=getPicHeader)
fullbgResult = urllib2.urlopen(request)
with open("fullbg.png", "wb") as f:
    f.write(fullbgResult.read())


#  图像还原
#  X偏移值: (n[i] % 26 * 12 + 1)
#  Y偏移值: (n[i] > 25 ? f.config.height / 2 : 0)
# 恢复前图像
bg = Image.open("bg.png","r")
fullbg = Image.open("fullbg.png","r")
rows = 2  # 行
columns = 26  # 列
sliceWidth = 10  # 列宽
sliceHeight = 58  # 行高
#  创建恢复后图像
recoverBg = Image.new("RGBA", (columns * sliceWidth, rows * sliceHeight))
recoverFullBg = Image.new("RGBA", (columns * sliceWidth, rows * sliceHeight))

n = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
startingX = 0
startingY = 0
offsetX = 0
offsetY = 0
for row in range(rows):
    for column in range(columns):
        startingX = column * sliceWidth
        startingY = row * sliceHeight
        offsetX = n[row * columns + column] % 26 * 12 + 1
        if n[row * columns + column] > 25:
            offsetY = int(116 / 2)
        else:
            offsetY = 0
        for x in range(sliceWidth):
            for y in range(sliceHeight):
                bgPix = bg.getpixel((offsetX + x, offsetY + y))
                recoverBg.putpixel((startingX + x, startingY + y),
                                       bgPix)
                fullbgPix = fullbg.getpixel((offsetX + x, offsetY + y))
                recoverFullBg.putpixel((startingX + x, startingY + y),
                                           fullbgPix)


recoverBg.save("recoverBg.png", "PNG")
recoverFullBg.save("recoverFullBg.png", "PNG")