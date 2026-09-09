create database todo_db;
use todo_db;

create table user(
	id int auto_increment primary key,
    name varchar(200) not null,
    email varchar(300) unique not null
);

insert into user(name,email) values('Messi','LeoMessi10@gmail.com');
insert into user(name,email) values('yamal','Lamineyamal19@gmail.com');
insert into user(name,email) values('Rodri','Rodri17@gmail.com');

create table todo(
	id int auto_increment primary key,
    title varchar(200) not null,
    status varchar(100) not null,
    user_id int not null
);

insert into todo(title,status,user_id) values('coding practise','completed',2);
insert into todo(title,status,user_id) values('sleeping','completed',1);
insert into todo(title,status,user_id) values('english practise','not completed',2);
insert into todo(title,status,user_id) values('football practise','completed',3);
insert into todo(title,status,user_id) values('workout','completed',1);
insert into todo(title,status,user_id) values('running','not completed',5);

select * from user;
select * from todo;

-- all user.name,todo.title,todo.status

select user.name,todo.title,todo.status from user left join todo on user.id=todo.user_id;

-- all user.name,todo.title,todo.status using inner join

select user.name,todo.title,todo.status from user inner join todo on user.id=todo.user_id;

-- all user.name,todo.title,todo.status using right join

select user.name,todo.title,todo.status from user right join todo on user.id=todo.user_id;