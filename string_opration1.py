str = input("Please enter a string:")

i = str.rfind(":")                 #查找字符：出现的下标
new_string = str[i+1:]

f = float(new_string)              #将字符转换成字符型数据

print(f)