import os  #通过os模块调用系统命令

file_path = "D:/临时文件夹/2020/11月/导航站1.1/应用icon/icon"  #文件路径
path_list = os.listdir(file_path) #遍历整个文件夹下的文件name并返回一个列表

path_name = []#定义一个空列表

common_name = 'https://test-nav.seasungame.com/uploadfile/2020/1124/'

for i in path_list:
    path_name.append(i) #若带有后缀名，利用循环遍历path_list列表，split去掉后缀名;只取文件名=>i.split(".")[0]

#path_name.sort() #排序

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("D:/临时文件夹/2020/11月/导航站1.1/应用icon/icon/dataset2.txt", "a") as file:
        file.write(common_name+file_name + "\n")
        print(file_name)
    file.close()
