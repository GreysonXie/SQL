
```
import random

# 生成示例产品数据
products = []
product_names = ["Laptop", "Phone", "Keyboard", "Monitor", "Mouse", "Headphones", 
                "Tablet", "Printer", "Webcam",'cake']

for idx in range(1, 21):  # 生成10条示例数据
    name = random.choice(product_names)
    price = round(random.uniform(20.0, 200), 2)  # 生成20-999之间的随机价格
    products.append((idx, name, price))


# 写入txt文件（使用制表符分隔）
file_path = "product_data.txt"  # 文件保存路径（默认当前目录）
with open(file_path, 'w', encoding='utf-8') as f:
    for product in products:
        line = f"{product[0]}\t{product[1]}\t{product[2]}\n"  # 关键点：用\t分隔
        f.write(line)

print(f"数据文件已生成至：{file_path}")
    
```
