#/use/bin/env python
# _*_ coding: utf-8 _*_
'''
#
#
# python cookbook 第一章 文本
# Writer：hello_hanjx@163.com
# Date：2014-07-01
# github: https://github.com/so-easy/python-cookbook
#
'''

'''
1.1　每次处理一个字符 6
1.2　字符和字符值之间的转换 7
1.3　测试一个对象是否是类字符串 8
1.4　字符串对齐 10
1.5　去除字符串两端的空格 11
1.6　合并字符串 11
1.7　将字符串逐字符或逐词反转 14
1.8　检查字符串中是否包含某字符集合中的字符 15
1.9　简化字符串的translate方法的使用 18
1.10　过滤字符串中不属于指定集合的字符 20
1.11　检查一个字符串是文本还是二进制 23
1.12　控制大小写 25
1.13　访问子字符串 26
1.14　改变多行文本字符串的缩进 29
1.15　扩展和压缩制表符 31
1.16　替换字符串中的子串 33
1.17　替换字符串中的子串-Python 2.4 34
1.18　一次完成多个替换 36
1.19　检查字符串中的结束标记 39
1.20　使用Unicode来处理国际化文本 40
1.21　在Unicode和普通字符串之间转换 43
1.22　在标准输出中打印Unicode字符 45
1.23　对Unicode数据编码并用于XML和HTML 46
1.24　让某些字符串大小写不敏感 49
1.25　将HTML文档转化为文本显示到UNIX终端上 52
'''

'''
每次处理 一个字符
'''
thestring = 'abcde'
#我们可以掉用内建的list，用字符串作为参数
thestring = 'abcde'
thelist = list(thestring)
print thelist
#['a', 'b', 'c', 'd', 'e']

#也可以用for循环
for c in thestring:
    print c
#a b c d e
#也可以用列表推导中的for遍历
result = [ c for c in thestring ]
print result
#['a', 'b', 'c', 'd', 'e']

#和列表推导效果完全一样，可以用内建的map函数

def echoList(x):
    return x
map(echoList,thestring)
#['a', 'b', 'c', 'd', 'e']

#获取字符串的集合可以用sets.Set
import sets
magic_chars = sets.Set(thestring)
magic_chars2 = sets.Set('cdefg')
print ''.join(maginc_chars)
#acbed 如果元素有相同的会去重
#集合的交集
print ''.join(magic_chars & magic_chars2)
#ced

