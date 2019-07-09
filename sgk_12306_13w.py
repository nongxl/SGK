#处理13w+12306社工库
import mysql.connector
config = {
      'user': 'nongxl',
      'password': 'qW2I?-#cj',
      'host': 'localhost',
      'database': 'sgk',
      'charset': 'utf8',
      "connection_timeout": 5,
      "use_pure": True
}
cnx = mysql.connector.connect(**config)  # 建立连接
cursor = cnx.cursor(dictionary=True)
f = open('D:\\dictionary\\13w_12306.txt',encoding='utf-8')
for each_line in f:
    x = str(each_line).rsplit('----')
    dictX = {'account': x[0],'pwd1': x[1],'name':x[2],'IdNum':x[3],'pwd2':x[4],'phone':x[5],'mailAddr':x[6].replace('\n','')}
    print(dictX)
    sql = '''
    INSERT INTO 12306_13w
    (account,pwd1,name,IdNum,pwd2,phone,mailAddr)
    VALUES
    (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');
    ''' % (dictX['account'],dictX['pwd1'],dictX['name'],dictX['IdNum'],dictX['pwd2'],dictX['phone'],dictX['mailAddr'])
    print(sql)
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
cursor.close()
cnx.close()
f.close()
