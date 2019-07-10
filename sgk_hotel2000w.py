#处理酒店200W条数据库
import mysql.connector
import sys
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
files = ['D:\\dictionary\\酒店2000W数据库csv格式\\1-200W.csv','D:\\dictionary\\酒店2000W数据库csv格式\\200W-400W.csv',
         'D:\\dictionary\\酒店2000W数据库csv格式\\400W-600W.csv','D:\\dictionary\\酒店2000W数据库csv格式\\600W-800W.csv',
         'D:\\dictionary\\酒店2000W数据库csv格式\\800W-1000W.csv','D:\\dictionary\\酒店2000W数据库csv格式\\1000W-1200W.csv',
         'D:\\dictionary\\酒店2000W数据库csv格式\\1200W-1400W.csv','D:\\dictionary\\酒店2000W数据库csv格式\\1400W-1600W.csv',
         'D:\\dictionary\\酒店2000W数据库csv格式\\1600w-1800w.csv','D:\\dictionary\\酒店2000W数据库csv格式\\1800w-2000w.csv',
         'D:\\dictionary\\酒店2000W数据库csv格式\\last5000.csv']
for file in files:
    print('insertting'+file)
    f = open(file,encoding='utf-8')
    for each_line in f:
        x = str(each_line).replace('\'', 'null').replace('\\','').replace('\\n','').rsplit(',')
        try:
            dictX = {'Name': x[0], 'CardNo': x[1], 'Descriot': x[2], 'CtfTp': x[3], 'CtfId': x[4], 'Gender': x[5],
                    'Birthday': x[6], 'Address': x[7], 'Zip': x[8], 'Dirty': x[9], 'District1': x[10], 'District2': x[11],
                    'District3': x[12], 'District4': x[13], 'District5': x[14], 'District6': x[15], 'FirstNm': x[16],
                    'LastNm': x[17], 'Duty': x[18], 'Mobile': x[19], 'Tel': x[20], 'Fax': x[21], 'EMail': x[22],
                    'Nation': x[23], 'Taste': x[24], 'Education': x[25], 'Company': x[26], 'CTel': x[27], 'CAddress': x[28],
                    'CZip': x[29], 'Family': x[30], 'Version': x[31], 'id': x[32]}
            sql = '''
                    INSERT INTO hotel_2000w
                    (Name,CardNo,Descriot,CtfTp,CtfId,Gender,Birthday,Address,Zip,Dirty,District1,District2,District3,District4,
                    District5,District6,FirstNm,LastNm,Duty,Mobile,Tel,Fax,EMail,Nation,Taste,Education,Company,CTel,CAddress,
                    CZip,Family,Version,id)
                    VALUES
                    (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',
                    \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');
                    ''' % (dictX['Name'],dictX['CardNo'],dictX['Descriot'],dictX['CtfTp'],dictX['CtfId'],dictX['Gender'],
                        dictX['Birthday'],dictX['Address'],dictX['Zip'],dictX['Dirty'],dictX['District1'],dictX['District2'],
                        dictX['District3'],dictX['District4'],dictX['District5'],dictX['District6'],dictX['FirstNm'],dictX['LastNm'],
                        dictX['Duty'],dictX['Mobile'],dictX['Tel'],dictX['Fax'],dictX['EMail'],dictX['Nation'],dictX['Taste'],
                        dictX['Education'],dictX['Company'],dictX['CTel'],dictX['CAddress'],dictX['CZip'],dictX['Family'],dictX['Version'],dictX['id'])
            try:
                cursor.execute(sql)
            except BaseException as e:
                print(e,sql)
                continue
        except BaseException as err:
            print(err,file,x)
            continue
    print(file+'done insert!')
    #dele = '''DELETE FROM hotel_2000w WHERE Name = '﻿Name';'''
    #cursor.execute(dele)
    f.close()
cursor.close()
cnx.close()