'''
@Project ：pythonProject1 
@File    ：main.py
@Author  ：ErrorMaker
@Date    ：2021/9/21 22:21 
'''



#ui
def ui():
    # input data
    path = input('请输入文件路径（默认路径为File.c)：')
    level = input('请输入运行等级：')
    return path,level
#choosing
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
        print('no finishing......')



# Counting fuction
def countingKwords(path):
    countkeywrds = 0
    keywrdsList = list()
    with open(path) as fileStream:
        #split str
        strarr = fileStream.read().split()
        #loop traverse str
        for str in strarr:
            #loop traverse keywords
            for kw in keywrds:
                #if contains keyword countkeywrds + 1
                if (str.__contains__(kw)):
                    countkeywrds = countkeywrds + 1
                    #add item
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
 #list of keywords
keywrds = ["auto", "break", "case", "char", "const", "continue", "default"
        , "double", "do", "else", "enum", "extern", "float", "for", "goto", "if"
        , "int", "long", "register", "return", "short", "signed", "sizeof", "static"
        , "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

if __name__ == '__main__':

    path,level=ui()


    chooseingFuction(path, level)





