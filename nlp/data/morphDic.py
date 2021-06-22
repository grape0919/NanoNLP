
from nlp.data.dataImpl import DataImpl


class Morph():
    MORPH_TYPES = ['NNG', 'NNP', 'NNB', 'NNM', 'NR', 'NP',
                   'VV', 'VA', 'VXV', 'VXA', 'VCP', 'VCN',
                   'MDT', 'MDN', 'MAG', 'MAC',
                   'IC',
                   'JKS', 'JKC', 'JKG', 'JKO', 'JKM', 'JKI', 'JKQ', 'JX', 'JC',
                   'EPH', 'EPT', 'EPP',
                   'EFN', 'EFQ', 'EFO', 'EFA', 'EFI', 'EFR', 'ECE', 'ECD', 'ECS', 'ETN', 'ETD',
                   'XPN', 'XPV', 'XSN', 'XSV', 'XSA', 'XSM', 'XSO', 'XR',
                   'SF', 'SP', 'SS', 'SE', 'SO', 'SW',
                   'UN', 'UV', 'UE',
                   'OL', 'OH', 'ON']
                   
    NUM_OF_MORPH_TYPES = len(MORPH_TYPES)

    morph_dic = [] # text|morphIndex
    morph_sen = [] 

    def reset(self):
        self.morph_dic = []

    def morphIndex(self, morph:str):
        return self.morph_dic.index(morph)

    def registMorphDic(self, text:str, morph:str):
        """
        형태소 사전 ("텍스트|형태소") 에 분석된 텍스트와 형태소 등록
        해쉬 맵을 사용하고, INDEX(INT) 를 사용해 메모리 사용량을 줄인다.
        """
        com = "|".join([text, morph])
        if com in self.morph_dic:
            return self.morphIndex(com)
        else :
            self.morph_dic.append(com)
            return self.morphIndex(com)

    