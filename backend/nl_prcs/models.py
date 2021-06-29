from konlpy.tag import Okt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import font_manager, rc
from common.models import FileDTO, Reader, Printer
from tqdm.notebook import tqdm
from bs4 import BeautifulSoup
import platform
import matplotlib.pyplot as plt
from urllib.request import urlopen
import urllib
import time


class Service(FileDTO, Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()


    def Wc_Alice_Image(self):
        f = self.f
        r = self.r
        p = self.p

        f.context = './data/'
        f.fname = '09. alice'
        text = r.txt(f)
        # text = open('./data/09. alice.txt', encoding='UTF-8').read()

        f.context = './data/'
        f.fname = '09. alice_mask'
        image = r.img(f)
        # alice_mask = np.array(Image.open('./data/09. alice_mask.png'))
        stopwords = set(STOPWORDS)
        stopwords.add('said')
        path = 'C:/Windows/Fonts/Arial.ttf'
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            ic('Unknown system... sorry~~~~')
        plt.figure(figsize=(8, 8))
        plt.imshow(image, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis('off')
        # plt.show()

        wc = WordCloud(background_color='white', max_words=2000, mask=image,
                       stopwords=stopwords)
        wc = wc.generate(text)
        wc.words_

        plt.figure(figsize=(12, 12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()


    def present_Image(self):
        f = self.f
        r = self.r
        p = self.p

        path = "c:/Windows/Fonts/Arial.ttf"
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            ic('Unknown system... sorry~~~~')
        plt.rcParams['axes.unicode_minus'] = False

        tmp1 = 'https://search.naver.com/search.naver?where=kin'
        html = tmp1 + '&sm=tab_jum&ie=utf8&query={key_word}&start={num}'
        response = urlopen(html.format(num=1, key_word=urllib.parse.quote('여친 선물')))
        soup = BeautifulSoup(response, "html.parser")
        tmp = soup.find_all('dl')
        tmp_list = []
        for line in tmp:
            tmp_list.append(line.text)
        ic(tmp_list)

        present_candi_text = []
        for n in tqdm(range(1, 1000, 10)):
            response = urlopen(html.format(num=n, key_word=urllib.parse.quote('여자 친구 선물')))
            soup = BeautifulSoup(response, "html.parser")
            tmp = soup.find_all('dl')
            for line in tmp:
                present_candi_text.append(line.text)
            time.sleep(0.5)
        ic(present_candi_text)
        ic(len(present_candi_text))

        o = Okt()
        f.context = './data/'
        f.fname = '09. heart.jpg'
        mask = r.jpg(f)
        image_colors = ImageColorGenerator(mask)
        stop_words = ['.', '가', '요', '답변', '...', '을', '수', '에', '질문', '제', '를', '이', '도',
                      '좋', '1', '는', '로', '으로', '2', '것', '은', '다', ',', '니다', '대', '들',
                      '2017', '들', '데', '..', '의', '때', '겠', '고', '게', '네요', '한', '일', '할',
                      '10', '?', '하는', '06', '주', '려고', '인데', '거', '좀', '는데', '~', 'ㅎㅎ',
                      '하나', '이상', '20', '뭐', '까', '있는', '잘', '습니다', '다면', '했', '주려',
                      '지', '있', '못', '후', '중', '줄', '6', '과', '어떤', '기본', '!!',
                      '단어', '선물해', '라고', '중요한', '합', '가요', '....', '보이', '네', '무지']

        # tokens_ko = t.morphs(present_text)
        # tokens_ko = [each_word for each_word in tokens_ko
        #              if each_word not in stop_words]
        # ko = nltk.Text(tokens_ko, name='여자 친구 선물')
        # data = ko.vocab().most_common(200)
        #
        # # for win : font_path='c:/Windows/Fonts/malgun.ttf'
        # wordcloud = WordCloud(font_path='/Library/Fonts/AppleGothic.ttf',
        #                       relative_scaling=0.1, mask=mask,
        #                       background_color='white',
        #                       min_font_size=1,
        #                       max_font_size=100).generate_from_frequencies(dict(data))
        #
        # default_colors = wordcloud.to_array()



if __name__ == '__main__':
    s = Service()
    # s.Wc_Alice_Image()
    s.present_Image()
