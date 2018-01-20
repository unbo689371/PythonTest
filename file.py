with open("test.txt", "wt") as out_file:
    out_file.write("文本會寫入到文件中\n看到我了拔！")
 
# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()
 
print(text)