关系模式`product(product_no, name, price)`

## 题目一（4分）

在数据库中创建该关系，并自建上面关系的txt数据文件：

1. 使用`COPY`命令导入数据库（PostgreSQL）
2. 将该关系导出为任意文件（如SQL、Txt、CSV、JSON等）。

实现步骤和代码：

利用python生成txt符合格式的文件，相关代码已给出在此文件目录。

1.登录psql，切换到目标数据库，我切入的是新建的homework6数据库，代码如下：
```
\c homework6
```
2.创建表
```
CREATE TABLE product (product_no INTEGER PRIMARY KEY,name VARCHAR(100) NOT NULL,price NUMERIC(10,2));
```
3.导入（注意文件路径斜杠为‘/’）
```
\copy product(product_no,name,price) FROM 'C:/Users/21310/OneDrive/Desktop/大三下作业/数据库原理/product_data.txt'
```
4.导出
```
-- 导出为 CSV 文件
\copy product TO 'C:/Users/21310/OneDrive/Desktop/大三下作业/数据库原理/product_export.csv' WITH CSV HEADER;
```
导出结果见本目录pdf附件

## 题目二（6分）

1. 添加一个新的商品，编号为`666`，名字为`cake`，价格不详。
```
INSERT INTO product (product_no, name，price) 
VALUES (666, 'cake',NULL);
```  
2. 使用一条SQL语句同时添加3个商品，内容自拟。
```
INSERT INTO product (product_no, name, price)
VALUES
  (77, 'USB Cable', 12.99),
  (88, 'Notebook', 5.50),
  (99, 'Speaker', 89.00);
```
3. 将商品价格统一打8折。
```
UPDATE product
SET price = price * 0.8;  --price=null记录仍然为null  
```
4. 将价格大于100的商品上涨2%，其余上涨4%。
```
UPDATE product
SET price = 
  CASE 
    WHEN price > 100 THEN price * 1.02
    ELSE price * 1.04 
  END
WHERE price IS NOT NULL;
```
5. 将名字包含`cake`的商品删除。
```
DELETE FROM product
WHERE name ILIKE '%cake%';  
```
6. 将价格高于平均价格的商品删除。
```
DELETE FROM product
WHERE price > (SELECT AVG(price) FROM product);
```   

## 题目三（5分）

### 针对PostgreSQL

1.使用参考下面的语句添加10万条商品，

```sql
-- PostgreSQL Only
INSERT INTO product (name, price)
SELECT
    'Product' || generate_series, -- 生成名称 Product1, Product2, ...
    ROUND((random() * 1000)::numeric, 2) -- 生成0到1000之间的随机价格，保留2位小数
FROM generate_series(1, 100000);
```
方案：

在pg Admin4的查询工作台直接执行以上语句会报错显示：
```
错误:  null value in column "product_no" of relation "product" violates not-null constraint
SQL
```
因为关系模式为product(product_no, name, price)， product_no 是主键且没有默认值，而此插入语句未显式生成该字段的值
所以，可以 1.product_no为主码不能删除，需要自动生成product_no值；2.或者为product_no设置默认值

因此，我先
```
-- 清空原表,避免于新生成的主码冲突
TRUNCATE TABLE product;
```
```
-- （添加 product_no 字段）
INSERT INTO product (product_no, name, price)
SELECT
    generate_series,  -- 生成 product_no（从1开始递增）
    'Product' || generate_series,
    ROUND((random() * 1000)::numeric, 2)
FROM generate_series(1, 100000);
```
成功生成

2。比较`DELETE`和`TRUNCATE`的性能差异。

析：

实验：在datagrip中的该库的查询控制台分别执行这2个命令

(1) 使用 DELETE 删除全部数据
```
DELETE FROM product;
```

(2) 使用 TRUNCATE 删除全部数据
```
TRUNCATE TABLE product;
```
直观感受：
delete耗时更长，truncate极快。

性能差异与对比：

1.delete逐行删除数据，而truncate直接删除数据文件，不逐行操作，不记录单行删除日志。

2.I/O负载：DELETE因记录详细日志导致更高I/O压力；TRUNCATE日志极少，I/O开销低。

3.事务与回滚：DELETE支持事务回滚（通过日志逐行恢复）；TRUNCATE，虽可包含在事务中，但无法单步回滚（需整体回滚事务）。

4.CPU/内存：DELETE因逐行处理和触发器执行占用更高资源；TRUNCATE资源消耗极低。

5.磁盘空间：DELETE仅标记数据为“可覆盖”，需手动VACUUM回收空间；TRUNCATE立即释放空间至操作系统，无需额外操作。

6.外键约束：TRUNCATE默认需无外键引用，或使用CASCADE级联删除。DELETE可配合ON DELETE规则灵活处理依赖。

7.自增序列：TRUNCATE重置自增计数器（如SERIAL），DELETE保留当前序列值。

性能差异总结：若需闪电清空全表，选TRUNCATE；若需精准控制删除逻辑，选DELETE。两者本质是“批量快刀”与“精细手术刀”之别。
