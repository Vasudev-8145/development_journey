-- line comment
-- end of all queries ;

create database movie_db;

show databases;

use movie_db;

-- movie[id,title,year,run_time,rating,genre]


create table movie(

	id int primary key auto_increment,
    title varchar(200) not null,
    year varchar(10) not null,
    run_time int not null,
    rating decimal(2,1) not null,
    genre enum("action","comedy","thriller","drama","horror") default "action"

);

desc movie;

insert into movie(title,year,run_time,rating,genre) values('abcd',2002,120,8.0,'action');
insert into movie(title,year,run_time,rating,genre) values('kgf',2021,160,9.5,'action');
insert into movie(title,year,run_time,rating,genre) values('vazha',2024,140,9.5,'comedy');
insert into movie(title,year,run_time,rating,genre) values('balan',2026,150,9.0,'drama');
insert into movie(title,year,run_time,rating,genre) values('spider man',2026,150,9.0,'action');

select * from movie;

select * from movie where id=2;

update movie set title='vaazha 2',year=2025 where id=3;

select * from movie where id=3;