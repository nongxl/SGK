#处理酒店200W条数据库
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
logfile = 'D:\\dictionary\\xiaomi_log.txt'
files = ['D:\\dictionary\\xiaomi_com.txt']
i = 2
for file in files:
    f = open(file,encoding='utf-8')
    #有些人取名用了特殊字符，需要处理一下。
    for each_line in f:
        x = str(each_line).replace('\'', '').replace('\\', '').replace('\"', '').rsplit('|')
        x.remove(x[0])
        while(len(x) > 5):
            x[i] = x[i-1] + x[i]
            x.remove(x[1])
        try:
            dictX = {'id_xiaomi': x[0], 'usrNam': x[1], 'pwd': x[2], 'account': x[3], 'IPAddr': x[4], 'notice': ''}
            sql = '''
                    INSERT INTO xiaomi_com
                    (id_xiaomi,usrNam,pwd,account,IPAddr,notice)
                    VALUES
                    (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');
                    ''' % (dictX['id_xiaomi'],dictX['usrNam'],dictX['pwd'],dictX['account'],dictX['IPAddr'],dictX['notice'])
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
    l = open(logfile, mode='a', encoding='utf-8')
    f.close()

cursor.close()
cnx.close()