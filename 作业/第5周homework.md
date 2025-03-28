空值的处理，聚集函数的使用。

## 题目一（2分）

请问下面的SQL语句是否合法？用实验验证你的想法。你从实验结果能得到什么结论？
1.
```sql
SELECT dept_name, min(salary)
FROM instructor;
```
不合法

datagrip验证的输出：
```
university.public> SELECT dept_name, min(salary)
                   FROM instructor
[2025-03-28 14:08:50] [42803] 错误: 字段 "instructor.dept_name" 必须出现在 GROUP BY 子句中或者在聚合函数中使用
[2025-03-28 14:08:50] 位置：8
```
结论：根据SQL的标准，如果在SELECT子句中同时有普通列和聚合函数，那么必须使用GROUP BY子句来指定分组依据，否则那些非聚合的列必须都在GROUP BY里出现。我的只管理解是在这个代码中dept_ame和min（salary）并不是一对一的关系，而是多对一的关系。

当我把dept_name移动到group by，语句合法化结果如下：
```
返回 7 行数据
MIN
80000.00
60000.00
87000.00
40000.00
65000.00
72000.00
80000.00
```

2.
```
SELECT dept_name, min(salary)
FROM instructor
GROUP BY dept_name
HAVING name LIKE '%at%';
```
不合法

datagrip验证的输出：
```
[42803] 错误: 字段 "instructor.name" 必须出现在 GROUP BY 子句中或者在聚合函数中使用 位置：76
```
结论：
HAVING子句用于过滤分组后的结果，所以它只能引用聚合函数或者在GROUP BY中的列。而这里的name字段如果不在GROUP BY里，也不是聚合函数的结果
，此时在HAVING中使用name会导致错误，因为每个分组可能有多个不同的name值，无法确定用哪一个。
将name改为dept_name则可以正常运行。

3.
```
SELECT dept_name
FROM instructor
WHERE AVG(salary) > 20000;
```
不合法
datagrip验证的输出：
```
查询执行错误: aggregate functions are not allowed in WHERE LINE 3: WHERE AVG(salary) > 20000; ^
```
结论：聚集函数不能直接放在where子句后面。

WHERE子句的条件是在每一行数据被选择时应用的，而聚合函数是需要在分组后计算的。所以在这种情况下，WHERE子句不能直接使用聚合函数，正确的做法应该是使用HAVING子句，但HAVING必须跟在GROUP BY之后。所以这个语句应该会报错，因为WHERE中不能出现聚合函数，除非是在子查询中。

正确的写法可能需要使用子查询或者将条件放在HAVING中，并配合GROUP BY,可正常运行的代码如下：
```
SELECT dept_name
FROM instructor
GROUP BY dept_name
HAVING AVG(salary) > 20000;
```

## 题目二（3分+3分+2分）

1. 找到工资最高员工的名字，假设工资最高的员工只有一位（至少两种写法）。



3. 找到工资最高员工的名字，假设工资最高的员工有多位（试试多种写法）。

4. 解释下面四句。

```sql
SELECT 1 IN (1);

SELECT 1 = (1);

SELECT (1, 2) = (1, 2);

SELECT (1) IN (1, 2);
```
