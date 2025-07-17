#python 
def isValid(s: str)->bool: 
# ここにコードを書いてください

    #括弧の辞書(dictionary)を作成
    dict = {"(":")","{":"}","[":"]"}

    #格納場所を設置
    box = []

    #文字列sから一文字ずつ調べていく
    for parentheses in s:

        #括弧があればboxに格納
        if parentheses in dict.keys():
            box.append(dict[parentheses])

        #対応する閉じ括弧がなければFalseを返す
        elif parentheses in dict.values():
            if parentheses != box.pop():
                return False
            
    return True

#end
s= '()' 
print(isValid(s))#True 
s= '({)}' 
print(isValid(s))#False 
