#dangdang
import mysql.connector
config = {
             'user': 'nongxl',
             'password': 'qW2I?-#cj',
             'host': 'localhost',
             'database': 'sgk',
             'charset': 'utf8',
             'pool_size': 10,
             'pool_name': 'offlineserver',
            'pool_reset_session': False,
            'connection_timeout': 120,
            'use_pure': True
}
cnx = mysql.connector.connect(**config)  # 建立连接
cursor = cnx.cursor(dictionary=True)
logfile = 'D:\\dictionary\\dangdang.log'
files = ['D:\\dictionary\\dangdang.csv']
for file in files:
    f = open(file,encoding='utf-8')
    for each_line in f:
        x = each_line.replace('\'', '').replace('\t', '').replace('\"', '').rsplit(',')
        try:
            dictX = {'name': x[0], 'Address': x[1], 'tell': x[2], 'mail': x[3],'notice':''}
            sql = '''
                    INSERT INTO dangdang
                    (name,Address,tell,mail,notice)
                    VALUES
                    (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');
                    ''' % (dictX['name'],dictX['Address'],dictX['tell'],dictX['mail'],dictX['notice'])
            try:
                cursor.execute(sql)
            except BaseException as e:
                print(e,sql)
                l = open(logfile, mode='a',encoding='utf-8')
                l.writelines(str(e))
                l.writelines(sql)
                l.close()
                continue
        except BaseException as err:
            print(err,file,x)
            l = open(logfile, mode='a', encoding='utf-8')
            l.writelines(str(err))
            l.writelines(file)
            l.writelines(str(each_line))
            l.close()
            continue
    f.close()

cursor.close()
cnx.close()