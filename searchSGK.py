#实现查询
import mysql.connector,sys,time
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

def search(sql):
    t1 = time.process_time()
    cnx = mysql.connector.connect(**config)  # 建立连接
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    i = 0
    for res in result:
        print('姓名      手机号        邮箱            身份证                地址')
        print(res['Name'],res['Mobile'],res['Email'],res['CtfId'],res['Address'])
        i = i+1
    print('共查询到'+ str(i) +'条记录')
    t2 = time.process_time()
    print(t1,t2)
    t = t2 - t1
    print(t)

argv = sys.argv
print(argv)
if len(argv) <3:
    print('Usage: python searchSGK.py [-N,-M,-C,-E] [Name,Mobile,CtfId,Email]')
    print('Example:python searchSGK.py -N 李华')
else:
    if argv[1] == '-N':
        argv = argv[2]
        print('按姓名' + str(argv) + '查找')
        sql = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Name = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,CtfId,NULL FROM 12306_13w WHERE Name = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,NULL FROM amazoncn WHERE Name = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Name = \'%s\'
                ORDER BY
                Name;
        ''' % (argv, argv, argv, argv)
        search(sql)
    elif argv[1] == '-M':
        argv = argv[2]
        print('按手机号' + str(argv) + '精确查找')
        sql = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Mobile = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,CtfId,NULL FROM 12306_13w WHERE Mobile = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,NULL FROM amazoncn WHERE Mobile = \'%s\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Mobile = \'%s\'
                ORDER BY
                Mobile;
        ''' % (argv, argv, argv, argv)
        search(sql)
    elif argv[1] == '-C':
        argv = argv[2]
        print('按身份证' + str(argv) + '模糊查找')
        sql = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE CtfId  LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,CtfId,NULL FROM 12306_13w WHERE CtfId LIKE \'%%%s%%\'
                ORDER BY
                CtfId;
        ''' % (argv,argv)
        search(sql)
    elif argv[1] == '-E':
        argv = argv[2]
        print('按邮箱' + str(argv) + '模糊查找')
        sql = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Email LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,CtfId,NULL FROM 12306_13w WHERE Email LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,NULL FROM amazoncn WHERE Email  LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Email  LIKE \'%%%s%%\'
                ORDER BY
                Email;
        ''' % (argv, argv, argv, argv)
        search(sql)
    elif argv[1] == '-A':
        argv = argv[2]
        print('按地址' + str(argv) + '查找')
        sql = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Address LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Address LIKE \'%%%s%%\';
        ''' % (argv,argv)
        print(sql)
        search(sql)
    else:
        print('Usage: python searchSGK.py [-N,-M,-C,-E] [Name,Mobile,CtfId,Email]')
        print('Example:python searchSGK.py -N 李华')
        print('Example:python searchSGK.py -M 13012345678')