#acfun
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
logfile = 'D:\\dictionary\\acfun.log'
files = ['D:\\dictionary\\acfun.txt']
for file in files:
    f = open(file,encoding='utf-8')
    for each_line in f:
        x = each_line.replace('\'', '').replace('\t', ',').replace('\"', '').rsplit(',')
        try:
            dictX = {'account': x[0], 'pwd': x[1], 'anoName': x[2], 'notice': ''}
            sql = '''
                    INSERT INTO acfun
                    (account,pwd,anoName,notice)
                    VALUES
                    (\'%s\',\'%s\',\'%s\',\'%s\');
                    ''' % (dictX['account'],dictX['pwd'],dictX['anoName'],dictX['notice'])
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
            print(err,file,str(each_line))
            l = open(logfile, mode='a', encoding='utf-8')
            l.writelines(str(err))
            l.writelines(file)
            l.writelines(str(each_line))
            l.close()
            continue
    f.close()

cursor.close()
cnx.close()