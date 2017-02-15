#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys

# 学習済みモデルのロード
model = word2vec.Word2Vec.load("sample.model")

# 入力された単語から近い単語をn個表示する
def s(posi, nega=[], n=10):
    cnt = 1 # 表示した単語の個数カウント用
    # 学習済みモデルからcos距離が最も近い単語n個(topn個)を表示する
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print cnt,'　', r[0],'　', r[1]
        cnt += 1

if __name__ == '__main__':
    word = sys.argv[1]
    word = unicode(word, 'utf-8')
    s([word])

    cnt = 1
    result = model.most_similar(positive = [u'人', u'成長'], negative = [u'給与'], topn = 10)
    for r in result:
        print cnt,'  ', r[0],'  ', r[1]
        cnt +=1
