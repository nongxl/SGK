CREATE TABLE IF NOT EXISTS `12306_13w`(
   `id12306` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `account` VARCHAR(40) NOT NULL,
   `pwd1` VARCHAR(40) NOT NULL,
	 `name` VARCHAR(40) NOT NULL,
	 `IdNum` VARCHAR(40) NOT NULL,
	 `pwd2` VARCHAR(40) NOT NULL,
	 `phone` VARCHAR(40) NOT NULL,
	 `mailAddr` VARCHAR(40) NOT NULL,
	 `notice` VARCHAR(100),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id12306` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

SELECT COUNT(*) FROM 12306_13w;

CREATE TABLE IF NOT EXISTS `hotel_2000w`(
   `id_hotel` INT UNSIGNED AUTO_INCREMENT NOT NULL,
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
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_hotel` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO 12306_13w
(account,pwd1,name,IdNum,pwd2,phone,mailAddr)
VALUES
('1234@account.com','pwd123456','test','451212199210121212','pwd1234567890','13012345678','1234@mail.com');

DELETE FROM 12306_13w WHERE id12306 = '1';
select count(*) from hotel_2000w;

DELETE FROM hotel_2000w WHERE Name = '﻿Name';
SELECT * FROM hotel_2000w WHERE Address LIKE '广西%';

#DROP TABLE xiaomi_com;
CREATE TABLE IF NOT EXISTS `xiaomi_com`(
   `id_xiaomi` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `usrNam` VARCHAR(40) NOT NULL,
   `pwd` VARCHAR(40) NOT NULL,
	 `account` VARCHAR(50) NOT NULL,
	 `IPAddr` VARCHAR(20),
	 `notice` VARCHAR(40),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_xiaomi` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from xiaomi_com;

#DROP TABLE acfun;
CREATE TABLE IF NOT EXISTS `acfun`(
   `id_acfun` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `account` VARCHAR(40) NOT NULL,
   `pwd` VARCHAR(40) NOT NULL,
	 `anoName` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_acfun` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from acfun;

#DROP TABLE amazonCN;
CREATE TABLE IF NOT EXISTS `amazonCN`(
   `id_amazon` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `account` VARCHAR(60) NOT NULL,
   `name` VARCHAR(40) NOT NULL,
	 `tell` VARCHAR(30) NOT NULL,
	 `mail` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_amazon` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from amazoncn;

#DROP TABLE dangdang;
CREATE TABLE IF NOT EXISTS `dangdang`(
   `id_dd` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `name` VARCHAR(60) NOT NULL,
   `Address` VARCHAR(100) NOT NULL,
	 `tell` VARCHAR(60) NOT NULL,
	 `mail` VARCHAR(50) NOT NULL,
	 `notice` VARCHAR(40),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_dd` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
select count(*) from dangdang;

