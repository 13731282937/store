'''
数字、布尔、字符串、数组、列表、元组、字典
字典：
    {wo : 我}
    特点：
        键：值存储方式
        无序存储，数据不允许重复

    方法：


'''

dic = {
    "010":"北京",
    "020":"上海",
    "030":"广州",
    "040":"深圳"
}

# 增
dic["050"] = "杭州"

# 删
del dic ["050"]

# 改
dic["010"] = "保定"

# 查
city = dic["010"]

print(city)
print(dic)
print(type(dic))