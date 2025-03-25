file = "text2.txt"
f = open(file, "w")
f.write("Тест:\n"
        "Замена строки в текстовом файле\n"
        "изменить строку в списке\n"
        "записать список в файл\n")
f.close()
f = open(file)
data = f.readlines()
print(data)
f.close()

data[0]="Pos1 = 1\nPos2 = 2\n"
data[1] = "записать список в файл\n"
data[2] = "изменить строку в списке\n"
print(data)

f = open(file, "a")
f.writelines(data)
f.close()