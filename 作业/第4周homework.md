    --create database university;
    --问题一
    SELECT DISTINCT T.name
    FROM instructor AS T, instructor AS S
    WHERE T.salary > S.salary AND S.dept_name = 'History';
    
    --问题二
    
    --找到所有以s开头的老师的名字
    --法1
    select name
    from instructor
    where name like 'S%';
    --法2
    select name
    from instructor
    where name similar to 'S%';
    --法3
    select name
    from instructor
    where name ~~ 'S%';
    --4
    SELECT name
    FROM instructor
    WHERE name ~ '^S';
    --5
    SELECT name
    FROM instructor
    WHERE substring(name from 1 for 1) = 'S';
    
    --问题三
    --s输入密码进入服务器
    --\l 展示所有库
    --\c university 切换到university库
    --\dt 展示所有库的表
    --\d instructor 查看instructor的表结构
