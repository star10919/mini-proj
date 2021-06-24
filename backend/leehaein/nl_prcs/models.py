from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Okt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
from icecream import ic
from leehaein.common.models import FileDTO, Reader, Printer
# import pandas as pd
# from sklearn import preprocessing
# import folium


class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()

    def konlpy_Kkma(self):
        k = Kkma()
        ic(k.sentences('한국어 분석을 시작합니다 재미있어요~~'))
        ic(k.nouns('한국어 분석을 시작합니다 재미있어요~~'))
        ic(k.pos('한국어 분석을 시작합니다 재미있어요~~'))

    def konlpy_Hannanum(self):
        h = Hannanum()
        ic(h.nouns('한국어 분석을 시작합니다 재미있어요~~'))
        ic(h.morphs('한국어 분석을 시작합니다 재미있어요~~'))
        ic(h.pos('한국어 분석을 시작합니다 재미있어요~~'))

    def konlpy_Okt(self):
        o = Okt()
        ic(o.nouns('한국어 분석을 시작합니다 재미있어요~~'))
        ic(o.morphs('한국어 분석을 시작합니다 재미있어요~~'))
        ic(o.pos('한국어 분석을 시작합니다 재미있어요~~'))

    def Wc_Image(self):
        text = open('./data/09. alice.txt').read()
        ic(text)
        alice_mask = np.array(Image.open('./data/09. alice_mask.png'))
        stopwords = set(STOPWORDS)
        stopwords.add('said')
        path = "c:/Windows/Fonts/malgun.ttf"
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')


if __name__ == '__main__':
    s = Service()
    # s.konlpy_Kkma()
    # s.konlpy_Hannanum()
    # s.konlpy_Okt()
    s.Wc_Image()