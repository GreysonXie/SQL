# Basic SQL
SQL是关系数据库的标准查询语言。本周我们学习了如何定义关系，如何进行基本的SQL查询。

## 题目一（3分）
假设拟在数据库添加一个关系，其关系模式是 users(name, pswd, gender)，并让`name`作为主码。请使用`CREATE TABLE`命令添加该关系。

      CREATE TABLE users(
      name varchar(4),
      pswd varchar(10),
      gender char(1),
      primary key (name)
      );


## 题目二（2分+3分）
考虑课堂中使用的`大学`数据库，包括如下关系：
- course(course_id, title, dept_name, credits)
- instructor(ID, name, dept_name, salary)
- teaches(ID, course_id, sec_id, semester, year)
- student(ID, name, dept_name, tot_cred)
- takes(ID, course_id, sec_id, semester, year, grade)

使用SQL语句完成下面的查询：

1. 找到在`计算机`学院开设的不少于`3`个`学分`的课程，并按`学分`进行升序排序。
  
        select *
        from course
        where credits >= 3 and dept_name='计算机'
        order by credit asc;      

            
   
3. 找到所有被名叫`图灵`的老师教过的学生的学号（`ID`），并确保结果没有重复。

       自己尝试理解做的结果：
       select  distinct takes.ID
       from takes, instructor, teaches
       where instructor.ID = teaches.ID
       and takes.course_id = teaches.course_id
       and instructor.name = '图灵'；
   
       反思：未考虑到一些特殊情况，结合AI解析找到错误后并纠正
   
       修正后：
        select distinct takes.ID
        from instructor, teaches, takes
        where 
            instructor.ID = teaches.ID          -- 关联教师与授课记录
            and teaches.course_id = takes.course_id  -- 课程ID相同
            and teaches.sec_id = takes.sec_id        -- 章节相同
            and teaches.semester = takes.semester    -- 学期相同
            and teaches.year = takes.year            -- 年份相同
            and instructor.name = '图灵';             -- 筛选教师名为"图灵"

        
        
## 题目三（2分）
考虑题目二提到的关系模式，请问下面的SQL语句的含义是什么？

```sql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = '会计';
```

      含义是：
      从 instructor 表中找出那些`salary`高于会计学院任意一位教师薪水的教师的姓名，同时结果中不可以包含重复的`name`
