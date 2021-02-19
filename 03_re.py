import re

# content = 'Xiaoshuaib has 100 bananas'
# 贪婪匹配
# res = re.match('^Xi.*(\d+)\s.*s$', content)
# 非贪婪匹配
# res = re.match('^Xi.*?(\d+)\s.*s$', content)


# content = "Xiaoshuaib has 100 \n" \
#           "bananas"
# 换行匹配
# res = re.match('^Xi.*?(\d+)\s.*s$', content, re.S)

# 匹配第一个
# res = re.search('Xi.*?(\d+)\s.*s', content, re.S)

# print(res.group(1))

# 获取所有匹配结果
# content = """Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;"""
# res = re.findall('Xi.*?(\d+)\s.*?s;', content, re.S)
# print(res)

# 替换匹配的结果
# content = """Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;"""
# content = re.sub('\d+', '250', content)
# print(content)

# compile 编译匹配
content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s',re.S)
# res = re.match('^Xi.*?(\d+)\s.*s$',content,re.S)
res = re.match(pattern, content)

print(res.group(1))

