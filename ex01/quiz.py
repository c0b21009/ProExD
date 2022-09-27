import random
import datetime
if __name__ == "__main__":
    a = random.randint(0,2)
    quizList = ["サザエさんの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    ansList = [["ますお","マスオ"],["わかめ","ワカメ"],["おい","甥","甥っ子","おいっこ"]]
    print("問題：\n"+quizList[a])
    st = datetime.datetime.now
    ans = input('答えるんだ：')
    ed = datetime.datetime.now
    if ans in ansList[a]:
        print('正解！！！')
    else:
        print('出直してこい')
   
    
    
    
        