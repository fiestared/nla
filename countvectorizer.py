# -*- coding: utf-8 -

import MeCab
import pandas as pd
import numpy as np
import csv
import sklearn.decomposition
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

def wakati(text):
    tagger = MeCab.Tagger("-Ochasen -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd")
    #text = text.encode("utf-8")
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞", "副詞", "形容動詞"]:
            lemma = node.feature.split(",")[6].decode("utf-8")
            if lemma == u"*":
                lemma = node.surface.decode("utf-8")
            word_list.append(lemma)
        node = node.next
    return u" ".join(word_list[1:-1])

def parse():
    lines = []
    for line in open('enps_comment_raw.csv', 'r'):
        arr = line.split("\n")
        lines.append(arr)
    return lines

wakatis = []
for line in parse():
    wakatis.append(wakati(line[0]))

count_vectorizer = CountVectorizer()
feature_vectors = count_vectorizer.fit_transform(wakatis)  # csr_matrix(疎行列)が返る

# pcaによる主成分分析
dim = 7
data = np.loadtxt("feature_vec_data.csv", delimiter=",")
pca = sklearn.decomposition.PCA(dim)

result = pca.fit_transform(data)
np.savetxt("vec_pca_result.csv", result, delimiter=",")

# 各行の素性ベクトルの表示
#print feature_vectors.toarray()

# csvファイルに配列を書き込む
#f = open('feature_vec_data.csv', 'ab')
#csvWriter = csv.writer(f)
#csvWriter.writerows(feature_vectors.toarray())
#f.close()

# 素性ベクトルに対応する単語の一覧を取得する
# vocabulary = count_vectorizer.get_feature_names()
