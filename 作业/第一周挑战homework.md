# Relational Model
数据模型是描述数据、数据联系、数据语义以及一致性约束的概念工具的集合。

# 本周作业（第1次作业）
## 题目一（3分+4分）
考虑一个`银行`数据库，其关系模式如下所示：

- branch (branch_name, branch_city, assets)
- customer (ID, customer_name, customer_street, customer_city)
- loan (loan_number, branch_name, amount)
- borrower (ID, loan_number)
- account (account_number, branch_name, balance)
- depositor (ID, account_number)

使用`关系代数`完成下面的查询：

1. 找到位于`成都`市的支行的名字。

        $\Pi_{branch_name}(\sigma_{branch_city='成都'}(branch))$


2. 找到在`杨柳`支行有贷款（`loan`）的借款人（`borrower`）的ID。
 
        $\Pi_{ID}(\sigma_{branch_name='杨柳',amount>0}(loan ⋈ borrower))$


## 题目二（3分）
假设数据库中存储用户名和密码的关系模式是 users(name, pswd, gender)，请结合关系代数简述实现`用户登录`逻辑的思路。

    实现用户登录逻辑，实际上是验证用户输入的用户名和密码与数据库中存储的记录是否匹配。

    σ_{name='input_name' ^ pswd='input_pswd'}(users)表示从users关系中挑选出name属性值为input_name，并且pswd属性值为input_pswd的那些元组。

    如果数据库中存在这样的元组，说明用户输入的用户名和密码是正确的，会显示登陆成功；如果不存在，就意味着用户名或密码错误，显示登陆失败请重新输入。
