-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (id INTEGER UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INTEGER NOT NULL FOREIGN KEY REFERENCES states(id), name VARCHAR(256) NOT NULL);
