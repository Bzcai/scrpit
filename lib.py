import pymysql.cursors

def getMemberId (mobile):
    connection = pymysql.connect(
        host='frontwdb.uat.chunbo.com',
        user='front',
        password='Dt@UDgGa',
        db='memberdb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    sql='SELECT member_id FROM member_info WHERE mobile='+mobile
    cursor = connection.cursor()
    cursor.execute(sql)
    restult = cursor.fetchone()
    return str(restult['member_id'])
    connection.close()