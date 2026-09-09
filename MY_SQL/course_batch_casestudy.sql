create database course_batch_db;

use course_batch_db;

-- course[id,title,fee,duration]

create table course(
	id int auto_increment primary key,
    title varchar(200) unique not null,
    fee decimal(8,2) not null,
    duration varchar(100) not null
);

-- batch[id,title,head_count,course_id]

create table batch(
	id int auto_increment primary key,
    title varchar(200) unique not null,
    head_count int not null,
    course_id int not null
);

desc course;
desc batch;