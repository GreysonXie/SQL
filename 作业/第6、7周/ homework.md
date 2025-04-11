关系模式`product(product_no, name, price)`

## 题目一（4分）

在数据库中创建该关系，并自建上面关系的txt数据文件：

1. 使用`COPY`命令导入数据库（PostgreSQL）
2. 将该关系导出为任意文件（如SQL、Txt、CSV、JSON等）。

实现步骤和代码：

1.登录psql，切换到目标数据库，我切入的是新建的homework6数据库，代码如下：
```
\c homework6
```
2.导入（注意文件路径斜杠为‘/’）
```
\copy product(product_no,name,price) FROM 'C:/Users/21310/OneDrive/Desktop/大三下作业/数据库原理/product_data.txt'
```
3.导出
```
-- 导出为 CSV 文件
\copy product TO 'C:/Users/21310/OneDrive/Desktop/大三下作业/数据库原理/product_export.csv' WITH CSV HEADER;
```


## 题目二（6分）

1. 添加一个新的商品，编号为`666`，名字为`cake`，价格不详。
```

```  
2. 使用一条SQL语句同时添加3个商品，内容自拟。
```

```
3. 将商品价格统一打8折。
```

```
4. 将价格大于100的商品上涨2%，其余上涨4%。
```

```
5. 将名字包含`cake`的商品删除。
```

```
6. 将价格高于平均价格的商品删除。
```

```   

## 题目三（5分）

### 针对PostgreSQL

使用参考下面的语句添加10万条商品，

```sql
-- PostgreSQL Only
INSERT INTO product (name, price)
SELECT
    'Product' || generate_series, -- 生成名称 Product1, Product2, ...
    ROUND((random() * 1000)::numeric, 2) -- 生成0到1000之间的随机价格，保留2位小数
FROM generate_series(1, 100000);
```

比较`DELETE`和`TRUNCATE`的性能差异。

