sum=0
with open("num.txt",mode="r",encoding="utf-8") as file:
    for line in file: #一行一行的讀取
        print("讀入數值為",int(line))
        sum+=int(line)
print("最後加總數值為",sum)