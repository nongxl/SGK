#批量查询
import searchSGK,sys

def batchSeach(sql,argv):
    pass
def witchSQL(option,argv):
    sqlN = '''
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

    sqlM = '''
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

    sqlC = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE CtfId  LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,CtfId,NULL FROM 12306_13w WHERE CtfId LIKE \'%%%s%%\'
                ORDER BY
                CtfId;
        ''' % (argv, argv)

    sqlE = '''
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
        ''' % (argv, argv, argv, argv, argv)

    sqlA = '''
                SELECT Name,Mobile,Email,CtfId,Address FROM hotel_2000w WHERE Address LIKE \'%%%s%%\'
                UNION ALL
                SELECT Name,Mobile,Email,NULL,Address FROM dangdang WHERE Address LIKE \'%%%s%%\';
        ''' % (argv, argv)
    if option == '-N':
        sql = sqlN
        return sql
    elif option == '-M':
        sql =sqlM
        return sql
    elif option == '-C':
        sql = sqlC
        return sql
    elif option == '-E':
        sql = sqlE
        return  sql
    elif option == '-A':
        sql = sqlA
        return  sql
    else:
        print('参数有误，程序退出')
        sys.exit()
argvs = sys.argv
if len(argvs) < 3:
    print('Usage: python searchSGK.py [-N,-M,-C,-E] [File Path]')
    print('Example:python searchSGK.py -N D:/text.txt')
else:
    option = argvs[1]
    file = argvs[2]
    f = open(file,encoding='utf-8')
    for each_line in f:
        argv = str(each_line).replace('\n','')
        print(argv)
        sql = witchSQL(option,argv)
        searchSGK.search(sql)
    f.close()
