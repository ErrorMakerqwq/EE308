'''
@Project ：pythonProject1 
@File    ：main.py
@Author  ：ErrorMaker
@Date    ：2021/9/21 22:21 
'''



#ui
def ui():
    # 输入用户数据
    path = input('请输入文件路径（默认路径为File.c)：')
    level = input('请输入运行等级：')
    return path,level
#选择器

def chooseingFuction(path,level):
    #level1
    if(level=='1'):
        countingKwords(path)
    #level2
    elif(level=='2'):
        keywrdsList = countingKwords(path)
        couterSClist = countingswtichStructure(keywrdsList)
        print('case num: ',end='')
        for i in range(0, len(couterSClist)):
            print(couterSClist[i]," ",end='')
    else:
        print('还没写完')





# Counting fuction
def countingKwords(path):
    countkeywrds = 0
    keywrdsList = list()
    with open(path) as fileStream:
        #分割字符串
        strarr = fileStream.read().split()
        #遍历str
        for str in strarr:
            #遍历关键字表
            for kw in keywrds:
                #如果有关键字countkeywrds + 1
                if (str.__contains__(kw)):
                    countkeywrds = countkeywrds + 1
                    #添加item
                    keywrdsList.append(kw)
                    break
    print('total num:', countkeywrds)
    return  keywrdsList

# Counting swtich structure
def countingswtichStructure(keywrdsList):
    counterSwitch = 0
    couterSClist = []
    i = 0;
    # find "swtich"
    for i in range(len(keywrdsList)):
        counter2 = 0
        if (keywrdsList[i] == "switch"):

            counterSwitch = counterSwitch + 1

            for j in range(i + 1, len(keywrdsList)):
                if (keywrdsList[j] == "case"):
                    counter2 = counter2 + 1

                elif (keywrdsList[j] == 'switch'):

                    break

            couterSClist.append(counter2)
    print('switch num:', counterSwitch)
    return couterSClist

# Counting if-else and if-elseif-else structure
#def countingEifStructure(keywrdsList):
 #关键字表
keywrds = ["auto", "break", "case", "char", "const", "continue", "default"
        , "double", "do", "else", "enum", "extern", "float", "for", "goto", "if"
        , "int", "long", "register", "return", "short", "signed", "sizeof", "static"
        , "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

if __name__ == '__main__':

    path,level=ui()


    chooseingFuction(path, level)





