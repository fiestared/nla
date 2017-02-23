# -*- coding: utf-8 -*-
import MeCab
import csv
import sys
from collections import Counter

def morpheme(text,list):
    w = MeCab.Tagger("-Ochasen -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    node = w.parseToNode(text)

    #単語のタグとスコア判定用
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

            # 単語に対してポジネガスコアを計算する
            fposiscore = open('tagdictionary/posiscore.csv','r')
            fposiscoreline = fposiscore.readline()

            fnegascore = open('tagdictionary/negascore.csv','r')
            fnegascoreline = fnegascore.readline()

            while fposiscoreline:
                if node.surface == fposiscoreline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    score += 1
                fposiscoreline = fposiscore.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            while fnegascoreline:
                if node.surface == fnegascoreline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    score -= 1
                fnegascoreline = fnegascore.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:worktime
            fworktimetag = open('tagdictionary/worktime.csv','r')
            fworktimetagline = fworktimetag.readline()

            while fworktimetagline:
                if node.surface == fworktimetagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    worktime += 1
                fworktimetagline = fworktimetag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:moneyrating
            fmoneyratingtag = open('tagdictionary/moneyrating.csv','r')
            fmoneyratingtagline = fmoneyratingtag.readline()

            while fmoneyratingtagline:
                if node.surface == fmoneyratingtagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    moneyrating += 1
                fmoneyratingtagline = fmoneyratingtag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:colleague
            fcolleaguetag = open('tagdictionary/colleague.csv','r')
            fcolleaguetagline = fcolleaguetag.readline()

            while fcolleaguetagline:
                if node.surface == fcolleaguetagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    colleague += 1
                fcolleaguetagline = fcolleaguetag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:job
            fjobtag = open('tagdictionary/job.csv','r')
            fjobtagline = fjobtag.readline()

            while fjobtagline:
                if node.surface == fjobtagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    job += 1
                fjobtagline = fjobtag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:companyculture
            fcompanyculturetag = open('tagdictionary/companyculture.csv','r')
            fcompanyculturetagline = fcompanyculturetag.readline()

            while fcompanyculturetagline:
                if node.surface == fcompanyculturetagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    companyculture += 1
                fcompanyculturetagline = fcompanyculturetag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:social
            fsocialtag = open('tagdictionary/social.csv','r')
            fsocialtagline = fsocialtag.readline()

            while fsocialtagline:
                if node.surface == fsocialtagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    social += 1
                fsocialtagline = fsocialtag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

            # 単語のタグを判定する:growthtraining
            fgrowthtrainingtag = open('tagdictionary/growthtraining.csv','r')
            fgrowthtrainingtagline = fgrowthtrainingtag.readline()

            while fgrowthtrainingtagline:
                if node.surface == fgrowthtrainingtagline.replace(('\r'or'\n\r'or'\r\n'),'\n').rstrip("\n"):
                    growthtraining += 1
                fgrowthtrainingtagline = fgrowthtrainingtag.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

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
    csvWriter = csv.writer(f)

    #rawファイルオープン
    f2 = open(sys.argv[1],'r')
    line = f2.readline().replace(('\r'or'\n\r'or'\r\n'),'\n')

    a = 0
    while line:
        a = a + 1
        print a
        text = line
        morpheme(text,callist)

        # タグとスコアを付与する
        callist.append(a)
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
