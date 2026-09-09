-- mysql expense_db

create database expense_db;
show databases;
use expense_db;

-- ["id","title","amount","category","owner"]

create table expense(
		id int primary key auto_increment,
        title varchar(200) not null,
        amount int not null,
        category enum('gpay','cash','card') default('cash'),
        owner varchar(100) not null
);

desc expense;

insert into expense(title,amount,category,owner) values("food expense",300,"gpay","messi");
insert into expense(title,amount,category,owner) values("travel expense",150,"cash","ronaldo");
insert into expense(title,amount,category,owner) values("grocery expense",200,"gpay","neymar");
insert into expense(title,amount,category,owner) values("shopping",1000,"card","mbappe");
insert into expense(title,amount,category,owner) values("movie",300,"gpay","haaland");

select * from expense;

select * from expense where id=2;

update expense set title="food expense",category="card" where id=2;