# -*- coding: utf-8 -*-
import MeCab
import csv
import sys
from collections import Counter

def morpheme(text,list):
    w = MeCab.Tagger("-Ochasen -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    node = w.parseToNode(text)

    global worktime
    global moneyrating
    global colleague
    global job
    global companyculture
    global social
    global growthtraining
    global score

    #名詞と形容詞と副詞と形容動詞と動詞のみを抽出する
    while node:
        if node.feature.split(",")[0] == "名詞" or node.feature.split(",")[0] == "形容詞" or node.feature.split(",")[0] == "副詞" or node.feature.split(",")[0] == "形容動詞":
            list.append(node.surface)
            if node.surface == "良い":
                score += 1;
        node = node.next

if __name__ == '__main__':

    callist = []
    dictlist = []

    # タグ付け用
    worktime = 0;
    moneyrating = 0;
    colleague = 0;
    job = 0;
    companyculture = 0;
    social = 0;
    growthtraining = 0;

    # ポジネガ判定用
    score = 0;

    #output用のファイルオープン
    f = open(sys.argv[2],'w')
    #rawファイルオープン
    f2 = open(sys.argv[1],'r')
    csvWriter = csv.writer(f)
    line = f2.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

    a = 0
    while line:
        a = a + 1
        print a
        text = line
        morpheme(text,callist)

        # タグとスコアを付与する
        callist.append(worktime)
        callist.append(moneyrating)
        callist.append(colleague)
        callist.append(job)
        callist.append(companyculture)
        callist.append(social)
        callist.append(growthtraining)
        callist.append(score)

        csvWriter.writerow(callist)

        # 次の行の判定のため、グローバル変数値をクリアする
        worktime = 0;
        moneyrating = 0;
        colleague = 0;
        job = 0;
        companyculture = 0;
        social = 0;
        growthtraining = 0;
        score = 0;

        callist = []
        line = f2.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

    for i in dictlist:
        if not i in dictout:
            dictout.append(i)

    f.close()
    f2.close()
