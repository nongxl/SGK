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

DROP TABLE hotel_2000w;

INSERT INTO 12306_13w
(account,pwd1,name,IdNum,pwd2,phone,mailAddr)
VALUES
('1234@account.com','pwd123456','test','451212199210121212','pwd1234567890','13012345678','1234@mail.com');

DELETE FROM 12306_13w WHERE id12306 = '1';
select count(*) from hotel_2000w;

CREATE TABLE IF NOT EXISTS `hotel_2000w`(
   `id_hotel` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `Name` VARCHAR(60) NOT NULL,
   `CardNo` VARCHAR(40),
	 `Descriot` VARCHAR(40),
	 `CtfTp` VARCHAR(40),
	 `CtfId` VARCHAR(40) NOT NULL,
	 `Gender` VARCHAR(40),
	 `Birthday` VARCHAR(40),
   `Address` VARCHAR(100),
   `Zip` VARCHAR(60),
	 `Dirty` VARCHAR(40),
   `District1` VARCHAR(60),
	 `District2` VARCHAR(60),
   `District3` VARCHAR(60),
	 `District4` VARCHAR(60),
   `District5` VARCHAR(60),
	 `District6` VARCHAR(60),
   `FirstNm` VARCHAR(40),
	 `LastNm` VARCHAR(40),
   `Duty` VARCHAR(40),
	 `Mobile` VARCHAR(40),
   `Tel` VARCHAR(40),
	 `Fax` VARCHAR(40),
   `EMail` VARCHAR(60),
	 `Nation` VARCHAR(40),
   `Taste` VARCHAR(40),
	 `Education` VARCHAR(40),
   `Company` VARCHAR(100),
	 `CTel` VARCHAR(40),
   `CAddress` VARCHAR(100),
   `CZip` VARCHAR(40),
	 `Family` VARCHAR(40),
   `Version` VARCHAR(40),
   `id` VARCHAR(40),
	 `Notice` VARCHAR(40),
   `submission_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( `id_hotel` )
)ENGINE=MyISAM DEFAULT CHARSET=utf8;

DELETE FROM hotel_2000w WHERE Name = '﻿Name';
SELECT * FROM hotel_2000w WHERE Name = '﻿Name';