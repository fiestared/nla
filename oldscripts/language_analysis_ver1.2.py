# -*- coding: utf-8 -*-
import MeCab
import csv
import sys
from collections import Counter

def morpheme(text,list,dict):
    w = MeCab.Tagger("-Ochasen -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    node = w.parseToNode(text)

    #名詞と形容詞と副詞と形容動詞と動詞のみを抽出する
    while node:
        if node.feature.split(",")[0] == "名詞" or node.feature.split(",")[0] == "形容詞" or node.feature.split(",")[0] == "副詞" or node.feature.split(",")[0] == "形容動詞":
            list.append(node.surface)
            dict.append(node.surface)
        node = node.next

if __name__ == '__main__':

    callist = []
    dictlist = []
    dictout = []

    #output用のファイルオープン
    f = open(sys.argv[2],'w')
    #rawファイルオープン
    f2 = open(sys.argv[1],'r')
    csvWriter = csv.writer(f)
    line = f2.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

    #辞書アウトプット用ファイルオープン
    f3 = open("dictionary.csv",'ab')


    a = 0
    while line:
        a = a + 1
        print a
        text = line
        morpheme(text,callist,dictlist)
        csvWriter.writerow(callist)
        callist = []
        line = f2.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')
    for i in dictlist:
        if not i in dictout:
            dictout.append(i)

    counter = Counter(dictlist)
    for word, cnt in counter.most_common():
            f3.write(word)
            f3.write(" ")
            f3.write(str(cnt))
            f3.write('\n')
            print "%s,%s"%(word,cnt)

#    print dictout #重複を削除した辞書化
#    for x in dictout:
#        f3.write(str(x)+',')

    f.close()
    f2.close()
    f3.close()
