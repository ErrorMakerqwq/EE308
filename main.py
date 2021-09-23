'''
@Project ：pythonProject1 
@File    ：main.py
@Author  ：ErrorMaker
@Date    ：2021/9/21 22:21 
'''

#选择器
def chooseingFuction(path,level):
    #level1
    if(level=='1'):
        countingKwords(path)
    #level2
    elif(level=='2'):
        keywordsList = countingKwords(path)
        couterSClist = countingswtichStructure(keywordsList)
        print('case num: ',end='')
        for i in range(0, len(couterSClist)):
            print(couterSClist[i]," ",end='')
    else:
        print('还没写完')




# Counting fuction
def countingKwords(path):
    countKeywords = 0
    keywordsList = list()
    with open(path) as fileStream:
        strarr = fileStream.read().split()
        for str in strarr:
            for kw in keywords:
                if (str.__contains__(kw)):
                    countKeywords = countKeywords + 1
                    keywordsList.append(kw)
                    break
    print('total num:', countKeywords)
    return  keywordsList

# Counting swtich structure
def countingswtichStructure(keywordsList):
    counterSwitch = 0
    couterSClist = []
    i = 0;
    # find "swtich"
    for i in range(len(keywordsList)):
        counter2 = 0
        if (keywordsList[i] == "switch"):

            counterSwitch = counterSwitch + 1

            for j in range(i + 1, len(keywordsList)):
                if (keywordsList[j] == "case"):
                    counter2 = counter2 + 1

                elif (keywordsList[j] == 'switch'):

                    break

            couterSClist.append(counter2)
    print('switch num:', counterSwitch)
    return couterSClist

# Counting if-else and if-elseif-else structure
#def countingEifStructure(keywordsList):

if __name__ == '__main__':
    #输入用户数据
    path=input('请输入文件路径（默认路径为File.c)：')
    level=input('请输入运行等级：')

    #关键字表
    keywords = ["auto", "break", "case", "char", "const", "continue", "default"
        , "double", "do", "else", "enum", "extern", "float", "for", "goto", "if"
        , "int", "long", "register", "return", "short", "signed", "sizeof", "static"
        , "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

    chooseingFuction(path, level)




