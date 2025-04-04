with open('data.txt') as f:
    num = [int(line.strip()) for line in f]
print(num)
print(sum(num))
print(sum(num)/len(num))
print(max(num))
print(min(num))
with open('write.txt','w') as f:
    f.write(f"Сумма: {[(sum(num))]}\n")
    f.write(f"Среднее:{[sum(num)/len(num)]}\n")
    f.write(f"Максимум:{[max(num)]}\n")
    f.write(f"Минимум:{[min(num)]}\n")

