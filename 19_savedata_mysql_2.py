# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
import pymysql
import xlrd

# 打开数据所在的路径表名
book = xlrd.open_workbook('平台城市对应关系表20220107.xls')
# 这个是表里的sheet名称（注意大小写）
sheet = book.sheet_by_name('城市对应表')

config = {
    'host': '192.168.99.7',
    'port': 7306,
    'user': 'zmn_mct',
    'password': 'zmn_mct123456',
    'database': 'zmn_mct',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.Cursor,
}

db = pymysql.connect(**config)

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

# 创建插入sql语句
sql = 'insert into zmn_mct.mct_area_relation' \
      '(plat_id,province,province_id,city,city_id,third_province,third_province_id,third_city,third_city_id)' \
      'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'

try:
    for r in range(1, sheet.nrows):
        # (r, 0)表示第二行的0就是表里的A1:A1
        province_id = sheet.cell(r, 0).value
        province = sheet.cell(r, 1).value
        city_id = sheet.cell(r, 2).value
        city = sheet.cell(r, 3).value

        third_province_id = sheet.cell(r, 4).value
        third_province = sheet.cell(r, 5).value
        third_city_id = sheet.cell(r, 6).value
        third_city = sheet.cell(r, 7).value

        if third_city_id is None or third_city_id == '':
            third_city_id = 0
        if third_province_id is None or third_province_id == '':
            third_province_id = 0
        values_360 = (
            270, province, province_id, city, city_id, third_province, third_province_id, third_city, third_city_id)
        # 执行sql语句
        cursor.execute(sql, values_360)

        third_province_id = sheet.cell(r, 8).value
        third_province = sheet.cell(r, 9).value
        third_city_id = sheet.cell(r, 10).value
        third_city = sheet.cell(r, 11).value
        if third_city_id is None or third_city_id == '':
            third_city_id = 0
        if third_province_id is None or third_province_id == '':
            third_province_id = 0
        values_shenma = (
            280, province, province_id, city, city_id, third_province, third_province_id, third_city, third_city_id)
        cursor.execute(sql, values_shenma)

        third_province_id = sheet.cell(r, 12).value
        third_province = sheet.cell(r, 13).value
        third_city_id = sheet.cell(r, 14).value
        third_city = sheet.cell(r, 15).value

        if third_city_id is None or third_city_id == '':
            third_city_id = 0
        if third_province_id is None or third_province_id == '':
            third_province_id = 0
        sql_sougou = (
        260, province, province_id, city, city_id, third_province, third_province_id, third_city, third_city_id)
        cursor.execute(sql, sql_sougou)

        third_province_id = sheet.cell(r, 16).value
        third_province = sheet.cell(r, 17).value
        third_city_id = sheet.cell(r, 18).value
        third_city = sheet.cell(r, 19).value

        if third_city_id is None or third_city_id == '':
            third_city_id = 0
        if third_province_id is None or third_province_id == '':
            third_province_id = 0
        sql_baidu = (
        140, province, province_id, city, city_id, third_province, third_province_id, third_city, third_city_id)
        cursor.execute(sql, sql_baidu)

        third_province_id = sheet.cell(r, 20).value
        third_province = sheet.cell(r, 21).value
        third_city_id = sheet.cell(r, 22).value
        third_city = sheet.cell(r, 23).value

        if third_city_id is None or third_city_id == '':
            third_city_id = 0
        if third_province_id is None or third_province_id == '':
            third_province_id = 0
        sql_toutiao = (
            210, province, province_id, city, city_id, third_province, third_province_id, third_city, third_city_id)
        cursor.execute(sql, sql_toutiao)

    db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()

# 显示导入多少列
columns = str(sheet.ncols)
# 显示导入多少行
rows = str(sheet.nrows)
print('导入' + columns + '列' + rows + '行数据到MySQL数据库!')
