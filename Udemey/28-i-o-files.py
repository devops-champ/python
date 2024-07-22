# text = open('myfile.txt')
# print(text.read())
# text.seek(0)  #if you want to read it again
# print(text.readlines())
# #output of readlines()
# #['Lorem ipsum dolor sit amet\n', 'Sed ut perspiciati\n', 'Nemo enim ipsam voluptatem\n', 'Neque porro quisquam\n', 'Ut enim ad minima']

# text.close()

#read a file
with open('myfile.txt', mode = 'r', encoding='utf-8') as f:
    print(f.read())

#append only

with open('myfile.txt', 'a', encoding='utf-8') as f:
    f.write('\npython is awesome')
    
#write 
with open('auto-gen.txt', 'w', encoding='utf-8') as w:
    w.write("Python created this file")