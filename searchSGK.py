#测试
import mysql.connector,sys
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
    cnx = mysql.connector.connect(**config)  # 建立连接
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    i = 0
    print('姓名      手机号        邮箱            身份证                地址')
    for res in result:
        print(res['Name'],res['Mobile'],res['Email'],res['CtfId'],res['Address'])
        i = i+1
    print('共查询到'+ str(i) +'条记录')

argv = sys.argv
print(argv)
if len(argv) < 3:
    print('Usage: python searchSGK.py [-N,-M,-C,-E] [Name,Mobile,CtfId,Email]')
    print('Example:python searchSGK.py -N 李华')
elif len(argv) == 4 and argv[1] == '--NA':
    argvN = argv[2]
    argvA = argv[3]
    print('按姓名地址' + str(argvN)+ str(argvA) + '组合模糊查找')
    sql = '''
            SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Name = \'%s\' AND Address LIKE \'%%%s%%\' 
            UNION ALL
            SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Name = \'%s\' AND Address LIKE \'%%%s%%\'
            ORDER BY
            Name;
    ''' % (argvN, argvA, argvN, argvA)
    search(sql)
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
                UNION ALL
                SELECT usrNam,NULL,account,NULL,IPAddr FROM xiaomi_com WHERE account  LIKE \'%%%s%%\'
                ORDER BY
                Email;
        ''' % (argv, argv, argv, argv,argv)
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
        print(len(argv))
        print('Usage: python searchSGK.py [-N,-M,-C,-E] [Name,Mobile,CtfId,Email]')
        print('Example:python searchSGK.py -N 李华')
        print('Example:python searchSGK.py -M 13012345678')