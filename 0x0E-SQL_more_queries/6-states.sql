-- creating a database and table
-- id should be autogenerated, not null and primary key
-- varchar cant be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS states (PRIMARY KEY(`id`),
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL);
