sum_data = 0
count = 0
average = 0
input_num = []                          #创建元组
min_data = None
max_data = None
while True:
    num = input("please input number:")
    if num =='done':
        break;

    try:
        num = float(num)                 #判断输入的数据是否合法
        input_num.append(num)
    except:
        print("Invalid input")
        continue

    if max_data is None or max_data < num:
        max_data = num

    if min_data is None or min_data > num:
        min_data = num
for i in input_num:
    sum_data = sum_data+ i
    count = count + 1

average = sum_data/count

print(sum_data, count, average,max_data, min_data)
