#vancl
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
logfile = 'D:\\dictionary\\vancl\\vancl.log'
files = ['D:\\dictionary\\vancl\\vancl_com1.csv','D:\\dictionary\\vancl\\vancl_com2.csv','D:\\dictionary\\vancl\\vancl_com3.csv']
for file in files:
    f = open(file,encoding='utf-8')
    for each_line in f:
        x = each_line.replace('\'', '').replace('\t', '').replace('\"', '').rsplit(',')
        try:
            dictX = {'Name': x[0], 'Mobile': x[1], 'Address': x[2], 'zip': x[3],'notice':''}
            sql = '''
                    INSERT INTO vancl
                    (Name,Mobile,Address,zip,notice)
                    VALUES
                    (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');
                    ''' % (dictX['Name'],dictX['Address'],dictX['Mobile'],dictX['zip'],dictX['notice'])
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