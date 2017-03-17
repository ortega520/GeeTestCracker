# coding:utf-8
from PIL import Image


# 判断两个像素点是否相似(允许一个差异值)
def pixSimilar(pixA, pixB):
    # RGB差异最大值
    max = 50
    diffR = abs(pixA[0] - pixB[0])
    diffG = abs(pixA[1] - pixB[1])
    diffB = abs(pixA[2] - pixB[2])
    return diffR < max and diffG < max and diffB < max
