import sys
import string
import random

##モードと長さを引数とする。
def generate(mode,num):
    symbolList = string.punctuation
    ##モードは三種類：-s:strong, -m:medium, -w:weak, -card:カード用
    if mode == "-s":
        ##記号４個モード
        symbol = ''.join([random.choice(symbolList) for i in range(4)])
        password = randString(num - 4)
        ##間に入れる
        for i in range(4):
            password = builtIn_symbol(password, symbol[i])
        return password
    elif mode == "-m":
        ##記号2個モード
        symbol = ''.join([random.choice(symbolList) for i in range(2)])
        password = randString(num - 2)
        ##間に入れる。
        for i in range(2):
            password = builtIn_symbol(password, symbol[i])
        return password
    elif mode == "-w":
        ##記号0個モード
        password = randString(num)
    else:
        ##card mode
        password = ''.join([random.choice(string.digits) for i in range(4)])
    return password

def randString(num):
    # 英数字記号をすべて取得
    char = string.digits + string.ascii_lowercase
    # 英数字からランダムに取得
    return ''.join([random.choice(char) for i in range(num)])

##文字列の間に入れる関数。どこに入れるかはランダム
def builtIn_symbol(string, symbol):
    new = ''
    rand = random.randint(-1, len(string))
    if rand == -1:
        new = symbol + string
    else:
        for i in range(rand):
            new = new + string[i]
        new = new + symbol
        if len(string) - rand != 0:
            for i in range(rand, len(string)):
                new = new + string[i]
    return new


if __name__ == "__main__":
    ##コマンドライン引数を使い、欲しいパスワードを作る。
    try:
        args = sys.argv
        ##モードを選択。
        mode = args[1]
        ##パスワードの長さを設定。
        if mode == "-card":
            number = 6
        else:
            number = args[2][1:]
            number = int(number)
        if int(number) < 6:
            number = str(6)
        password = generate(mode,number)
        print(password)
    except:
        print("Please write right argments!!!")
