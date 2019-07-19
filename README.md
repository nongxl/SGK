#sgk
依赖：
pip3 install mysql-connector-python

本项目仅用于学习python3的数据处理，所以都是旧数据。
还在继续导入其他数据来源，暂时不打算实现前台查询应用。

建库sql.sql为常用sql语句，作为参考。不要直接运行。

用法：
单一查询 python3 searchSGK.py [-N（姓名）|-M（手机号）|-E（邮箱）|-C（身份证）|-A（地址）|-NA] [姓名|手机号|邮箱（模糊查询，可查询qq号）|身份证（模糊查询）|地址（模糊查询）|姓名 地址（组合模糊查询）]
批量查询 python3 batchSearch.py [-N|-M|-E|-C] [filepath]