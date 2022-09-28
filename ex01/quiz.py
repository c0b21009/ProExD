import random
import time
def syutudai(quiz):
    qa = random.choice(quiz)
    print("問題：\n"+qa["q"])
    return qa["a"]

def kaito(ansList):
    ans = input("答えるんだ：")
    if ans in ansList:
        print("正解")
    else:
        print("不正解")
        
if __name__ == "__main__":
    a = random.randint(0,2)
    quizList = [{"q":"サザエさんの旦那の名前は？", "a":["ますお","マスオ"]},
                {"q":"カツオの妹の名前は？", "a":["わかめ","ワカメ"]},
                {"q":"タラオはカツオから見てどんな関係？", "a":["おい","甥","甥っ子","おいっこ"]}]
    st = time.time()
    ans_lst = syutudai(quizList)
    kaito(ans_lst)
    ed = time.time()
    print(ed-st)
   
    
    
    
        