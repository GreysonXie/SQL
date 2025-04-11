
```
import random

# 生成 10 万条商品数据
data = []
for i in range(1, 100):
    name = f'Product{i}'
    price = round(random.uniform(10, 200), 2)
    data.append(f'{i},{name},{price}')

# 将数据写入文件
with open('product_data.txt', 'w') as f:
    f.write('\n'.join(data))
```
