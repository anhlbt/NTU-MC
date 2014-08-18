# -*- coding: utf-8 -*-

import os, io, subprocess, time
import sys; reload(sys); sys.setdefaultencoding('utf-8')

from nltk.tokenize import word_tokenize

import cmn, kor, jpn, vie

chinese = cmn.StanfordNLP()
korean = kor.Postech()
japanese = jpn.Mecab()
vietnamese = vie.Jvntextpro()

lang2lib = {'jpn':japanese, 'cmn':chinese, 
            'vie':vietnamese, 'kor':korean}

def tokenize(text, lang):
    if lang in ['eng', 'ind']:
        return " ".join(word_tokenize(text))
    elif lang in lang2lib.keys():
        return lang2lib[lang].tokenize(text)
    else:
        return " ".join(text.split())