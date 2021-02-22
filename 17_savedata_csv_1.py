import pandas

xiaoshuaib = pandas.read_csv('xiaoshuaib.csv', encoding='gb2312')

print(xiaoshuaib)

b = ['小帅b', '小帅c', '小帅d']
c = ['18岁', '19岁', '20岁']
d = ['18cm', '17cm', '16cm']

df = pandas.DataFrame({'你是谁': b, '你几岁': c, '你多高': d})
df.to_csv("xsb.csv", index=False, sep=',')
