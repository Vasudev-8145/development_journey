"""
==> QUERIES

--> query for creating new database

    -- create database database_name;

--> query for listing database

    -- show databases;

--> query for using databae

    -- use database_name;

--> query for creating table

    -- create table table_name(
        
       column_name datatype constraint,
       column_name datatype constraint,
       column_name datatype constraint,
       column_name datatype constraint,
);

--> query for describing table

    -- desc table_name

--> query for inserting into table  (post)

    -- insert into table_name(col1,col2,col3,,,) values(val1,val2,val3,,,)

--> query for listing all records  (get)

    -- select * from table_name;  # * means all columns

--> query for listing one row using condition  (retreive)

    -- select * from table_name where condition;

--> query for updating record (put)

    -- update table_name set col1=value1,col2=value2,col3=value3 where condition;

--> query for deleting record (delete)

    -- delete from table_name where condition;
"""

"""
==> to comment line -- 
==> at the end of every query ;

"""

"""
in == while using multiple or

between == use while range

order by == use for sorting...use desc last for descending order

limit == to limit the records

offset == to skip records

max,min,sum,count,avg == aggregate functions

distinct == to remove duplicates from fetched records

group by == to group columns

having == used to give condition while using group by

"""

"""
==> JOINS

    --> used to join tables
    --> syntax:- select columns from joins on matching columns

--> Left join => all records of left side table and matching records of right side table
    eg:- select course.title,course.fee,batch.title.batch.head_count from course left join batch on course.id=batch.course_id

--> Inner join => matching records of both tables
    eg:- select course.title,course.fee,batch.title.batch.head_count from course inner join batch on course.id=batch.course_id

--> Right join => all records of right side table and matching records of left side table
    eg:- select course.title,course.fee,batch.title,batch.head_count from course right join batch on course.id=batch.course_id;
"""