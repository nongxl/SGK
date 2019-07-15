CREATE TABLE IF NOT EXISTS `12306_13w`(
   `Account` VARCHAR(40) NOT NULL,
   `PWD1` VARCHAR(40) NOT NULL,
	 `Name` VARCHAR(40) NOT NULL,
	 `CtfId` VARCHAR(40) NOT NULL,
	 `PWD2` VARCHAR(40) NOT NULL,
	 `Mobile` VARCHAR(40) NOT NULL,
	 `Email` VARCHAR(40) NOT NULL,
	 `Notice` VARCHAR(100),
   PRIMARY KEY ( `account` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

SELECT COUNT(*) FROM 12306_13w;

CREATE TABLE IF NOT EXISTS `hotel_2000w`(
   `Name` VARCHAR(60) NOT NULL,
   `CardNo` VARCHAR(40),
	 `Descriot` VARCHAR(100),
	 `CtfTp` VARCHAR(40),
	 `CtfId` VARCHAR(40) NOT NULL,
	 `Gender` VARCHAR(40),
	 `Birthday` VARCHAR(40),
   `Address` VARCHAR(100),
   `Zip` VARCHAR(60),
	 `Dirty` VARCHAR(60),
   `District1` VARCHAR(60),
	 `District2` VARCHAR(60),
   `District3` VARCHAR(60),
	 `District4` VARCHAR(60),
   `District5` VARCHAR(60),
	 `District6` VARCHAR(60),
   `FirstNm` VARCHAR(40),
	 `LastNm` VARCHAR(40),
   `Duty` VARCHAR(60),
	 `Mobile` VARCHAR(40),
   `Tel` VARCHAR(40),
	 `Fax` VARCHAR(60),
   `EMail` VARCHAR(60),
	 `Nation` VARCHAR(40),
   `Taste` VARCHAR(100),
	 `Education` VARCHAR(60),
   `Company` VARCHAR(100),
	 `CTel` VARCHAR(60),
   `CAddress` VARCHAR(100),
   `CZip` VARCHAR(60),
	 `Family` VARCHAR(60),
   `Version` VARCHAR(60),
   `id` VARCHAR(40),
	 `Notice` VARCHAR(60),
   PRIMARY KEY ( `name` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO 12306_13w
(account,pwd1,name,IdNum,pwd2,phone,mailAddr)
VALUES
('1234@account.com','pwd123456','test','451212199210121212','pwd1234567890','13012345678','1234@mail.com');

DELETE FROM 12306_13w WHERE id12306 = '1';
select count(*) from hotel_2000w;

#DELETE FROM hotel_2000w WHERE Name = '﻿Name';
SELECT * FROM hotel_2000w WHERE Address LIKE '广西%';
#CREATE INDEX index_Hotel_2000w ON hotel_2000w(username(length));
SELECT * FROM hotel_2000w WHERE Name = '';



#DROP TABLE xiaomi_com;
CREATE TABLE IF NOT EXISTS `xiaomi_com`(
   `usrNam` VARCHAR(40) NOT NULL,
   `pwd` VARCHAR(40) NOT NULL,
	 `account` VARCHAR(50) NOT NULL,
	 `IPAddr` VARCHAR(20),
	 `notice` VARCHAR(40),
   PRIMARY KEY ( `account` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from xiaomi_com;

#DROP TABLE acfun;
CREATE TABLE IF NOT EXISTS `acfun`(
   `Account` VARCHAR(40) NOT NULL,
   `pwd` VARCHAR(40) NOT NULL,
	 `anoName` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   PRIMARY KEY ( `account` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from acfun;

#DROP TABLE amazonCN;
CREATE TABLE IF NOT EXISTS `amazonCN`(
   `Account` VARCHAR(60) NOT NULL,
   `Name` VARCHAR(40) NOT NULL,
	 `Mobile` VARCHAR(30) NOT NULL,
	 `Email` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   PRIMARY KEY ( `name` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from amazoncn;

#DROP TABLE dangdang;
CREATE TABLE IF NOT EXISTS `dangdang`(
   `Name` VARCHAR(60) NOT NULL,
   `Address` VARCHAR(100) NOT NULL,
	 `Mobile` VARCHAR(60) NOT NULL,
	 `Email` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   PRIMARY KEY ( `name` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from dangdang;


#建表的时候没注意优化的问题
#删除自增长再删除主键
ALTER TABLE hotel_2000w MODIFY id_hotel INT UNSIGNED;
ALTER TABLE hotel_2000w DROP PRIMARY KEY;
ALTER TABLE hotel_2000w DROP COLUMN id_hotel;
ALTER TABLE hotel_2000w DROP COLUMN submission_date;

ALTER TABLE hotel_2000w DROP INDEX Name;
ALTER TABLE hotel_2000w ADD INDEX idx_hotel(Name,CtfId,Address,Email,Mobile);
ALTER TABLE hotel_2000w ADD INDEX idx_name(Name);
ALTER TABLE hotel_2000w ADD INDEX idx_CtfId(CtfId);
ALTER TABLE hotel_2000w ADD INDEX idx_Addr(Address);
ALTER TABLE hotel_2000w ADD INDEX idx_Email(Email);
ALTER TABLE hotel_2000w ADD INDEX idx_Mobile(Mobile);


SHOW INDEX FROM hotel_2000w;
SHOW COLUMNS FROM hotel_2000w;

#小米
ALTER TABLE xiaomi_com MODIFY id_xiaomi INT UNSIGNED;
ALTER TABLE xiaomi_com DROP PRIMARY KEY;
ALTER TABLE xiaomi_com DROP COLUMN id_xiaomi;
ALTER TABLE xiaomi_com DROP COLUMN submission_date;

ALTER TABLE xiaomi_com ADD INDEX idx_xiaomi(usrNam,account);
ALTER TABLE xiaomi_com ADD INDEX idx_acc(account);
ALTER TABLE xiaomi_com ADD INDEX idx_usrNam(usrNam);
ALTER TABLE xiaomi_com DROP INDEX usrNam;

SHOW INDEX FROM xiaomi_com;
SELECT * FROM xiaomi_com WHERE account = '1187917113@qq.com';

#12306
SELECT account,name,IdNum,phone,mailAddr FROM 12306_13w WHERE mailAddr = '1187917113@qq.com';
ALTER TABLE 12306_13w MODIFY id12306 INT UNSIGNED;
ALTER TABLE 12306_13w DROP PRIMARY KEY;
ALTER TABLE 12306_13w DROP COLUMN id12306;
ALTER TABLE 12306_13w DROP COLUMN submission_date;

ALTER TABLE 12306_13w ADD INDEX idx_12306(account,name,idNum,phone,mailAddr);
ALTER TABLE 12306_13w ADD INDEX idx_acc(account);
ALTER TABLE 12306_13w ADD INDEX idx_name(name);
ALTER TABLE 12306_13w ADD INDEX idx_idNum(idNum);
ALTER TABLE 12306_13w ADD INDEX idx_phone(phone);
ALTER TABLE 12306_13w ADD INDEX idx_mail(mailAddr);

SHOW INDEX FROM 12306_13w;

#acfun
ALTER TABLE acfun MODIFY id_acfun INT UNSIGNED;
ALTER TABLE acfun DROP PRIMARY KEY;
ALTER TABLE acfun DROP COLUMN id_acfun;
ALTER TABLE acfun DROP COLUMN submission_date;

ALTER TABLE acfun ADD INDEX idx_acfun(account);

SHOW INDEX FROM acfun;

#amazon
ALTER TABLE amazoncn MODIFY id_amazon INT UNSIGNED;
ALTER TABLE amazoncn DROP PRIMARY KEY;
ALTER TABLE amazoncn DROP COLUMN id_amazon;
ALTER TABLE amazoncn DROP COLUMN submission_date;

ALTER TABLE amazoncn DROP INDEX idx_amazon;
ALTER TABLE amazoncn ADD INDEX idx__amazon_acc(account);
ALTER TABLE amazoncn ADD INDEX idx_amazon_name(name);
ALTER TABLE amazoncn ADD INDEX idx_amazon_mail(mail);
ALTER TABLE amazoncn ADD INDEX idx_amazon_tell(tell);

SHOW INDEX FROM amazoncn;

#dangdang
ALTER TABLE dangdang MODIFY id_dd INT UNSIGNED;
ALTER TABLE dangdang DROP PRIMARY KEY;
ALTER TABLE dangdang DROP COLUMN id_dd;
ALTER TABLE dangdang DROP COLUMN submission_date;

ALTER TABLE dangdang ADD INDEX idx_dangdang(name,Address,mail,tell);

ALTER TABLE amazoncn DROP INDEX idx_dangdang;

SHOW INDEX FROM dangdang;


#统一列名
ALTER TABLE 12306_13w CHANGE name Name VARCHAR(40);
ALTER TABLE 12306_13w CHANGE mail Email VARCHAR(40);
ALTER TABLE 12306_13w CHANGE IdNum CtfId VARCHAR(40);
ALTER TABLE 12306_13w CHANGE phone Mobile VARCHAR(40);

ALTER TABLE amazoncn CHANGE name Name VARCHAR(40);
ALTER TABLE amazoncn CHANGE tell Mobile VARCHAR(30);
ALTER TABLE amazoncn CHANGE mail Email VARCHAR(50);

ALTER TABLE dangdang CHANGE name Name VARCHAR(60);
ALTER TABLE dangdang CHANGE tell Mobile VARCHAR(60);
ALTER TABLE dangdang CHANGE mail Email VARCHAR(50);

#查询语句
SELECT Name,Mobile,Email,CtfId FROM hotel_2000w WHERE Name = '李华';
SELECT Name,Mobile,Email,CtfId FROM 12306_13w WHERE Name = '李华';
SELECT Name,Mobile,Email FROM amazoncn WHERE Name = '李华';
SELECT Name,Mobile,Email FROM dangdang WHERE Name = '李华';

#按姓名组合查询
SELECT Name,Mobile,Email,CtfId FROM hotel_2000w WHERE Name = '李华'
UNION ALL
SELECT Name,Mobile,Email,CtfId FROM 12306_13w WHERE Name = '李华'
UNION ALL
SELECT Name,Mobile,Email,NULL FROM amazoncn WHERE Name = '李华'
UNION ALL
SELECT Name,Mobile,Email,NULL FROM dangdang WHERE Name = '李华';



