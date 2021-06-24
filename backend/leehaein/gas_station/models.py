from leehaein.common.models import FileDTO
from leehaein.common.models import Printer, Reader, Scraper
import numpy as np
import pandas as pd
import folium
from selenium import webdriver
from glob import glob
import re

'''
셀프 주유소는 정말 저렴할까?
4-1 Selenium 사용하기
4-2 서울시 구별 주유소 가격 정보 열기
4-5 구별 주유 가격에 대한 데이터의 정리
4-6 서울시 주유 가격 상하위 10개 주유소 지도에 표기하기

<class 'pandas.core.frame.DataFrame'>
Int64Index: 537 entries, 0 to 45
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   지역      537 non-null    object
 1   상호      537 non-null    object
 2   주소      537 non-null    object
 3   상표      537 non-null    object
 4   전화번호    537 non-null    object
 5   셀프여부    537 non-null    object
 6   고급휘발유   537 non-null    object
 7   휘발유     537 non-null    object
 8   경유      537 non-null    object
 9   실내등유    537 non-null    object
dtypes: object(10)
memory usage: 46.1+ KB
****************************************************************************************************
      지역      상호                     주소      상표  ... 고급휘발유   휘발유    경유 실내등유
0  서울특별시  오렌지주유소   서울 강동구 성안로 102 (성내동)   SK에너지  ...     -  1554  1354  997
1  서울특별시  구천면주유소  서울 강동구 구천면로 357 (암사동)  현대오일뱅크  ...     -  1556  1355    -
[2 rows x 10 columns]
       지역       상호                     주소     상표  ... 고급휘발유   휘발유    경유  실내등유
44  서울특별시    오천주유소  서울 강남구 봉은사로 503 (삼성동)  SK에너지  ...  2293  2107  1909  1232
45  서울특별시  뉴서울(강남)   서울 강남구 언주로 716 (논현동)  SK에너지  ...  2420  2120  1920  1330
[2 rows x 10 columns]
'''


class Service():

    def __init__(self):
        self.file = FileDTO()
        self.reader = Reader()
        self.printer = Printer()
        self.scraper = Scraper()

    def get_url(self):
        file = self.file
        reader = self.reader
        printer = self.printer
        scraper = self.scraper
        file.url = 'http://www.opinet.co.kr/searRgSelect.do'
        driver = scraper.driver()
        print(driver.get(file.url))

        gu_list_raw = driver.find_element_by_xpath("""//*[@id="coolbeat"]""")
        gu_list = gu_list_raw.find_elements_by_tag_name("option")
        gu_names = [option.get_attribute("value") for option in gu_list]
        gu_names.remove("")
        print(gu_names)


    def gas_station_price_info(self):
        print(glob('./data/지역_위치별*xls'))   #안됨
        file = self.file
        reader = self.reader
        printer = self.printer
        station_files = glob('./data/지역_위치별*xls')    #glob 사용 이유: * 사용하려고
        tmp_raw = []
        for i in station_files:
            t = pd.read_excel(i, header=2)
            tmp_raw.append(t)
        station_raw = pd.concat(tmp_raw)
        station_raw.info()


        print('*' * 100)
        print(station_raw.head(2))
        print(station_raw.tail(2))

        stations = pd.DataFrame({'Oil_store':station_raw['상호'],
                                 '주소':station_raw['주소'],
                                 '가격':station_raw['휘발유'],
                                 '셀프':station_raw['셀프여부'],
                                 '상표':station_raw['상표']})

        print(stations.head())
        stations['구'] = [ i.split()[1] for i in stations['주소']]  #2번째(파이썬에서는 1)가 주소임
        stations['구'].unique()  #unique는 중복된 거 제거해라(하나의 값만 추출)
        # print(stations[stations['구']=='서울특별시'])
        # 12 SK네트웍스(주)효진주유소 1 서울특별시 성동구 통일로 129~~~
        stations[stations['구'] == '서울특별시'] = '성동구'
        stations['구'].unique()
        # print(stations[stations['구'] == '특별시'])
        # 10 서현주유소 서울 특별시 도봉구 방학로 142~~~~
        stations[stations['구'] == '특별시'] = '도봉구'
        stations['구'].unique()
        print(stations[stations['가격'] == '-'])
        # 18
        # 33
        # 12
        # 13
        stations = stations[stations['가격'] != '-']  #    != : 'not='
        # print(stations[stations['가격'] == '성동구'])
        # 12      성동구 성동구 성동구 성동구 성동구 성동구
        p = re.compile('^[0-9]+$')
        temp_stations = []
        for i in stations:
            if temp_stations['가격'] != p.match():     # ^시작 $끝
                temp_stations.append(stations['가격'][i])
        stations['가격'] = [float(i) for i in stations['가격']]
        stations.reset_index(inplace=True)
        del stations['index']
        printer.dframe(stations)


if __name__ == '__main__':
    s = Service()
    s.get_url()
    s.gas_station_price_info()