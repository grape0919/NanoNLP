
from nlp.data.dataImpl import DataImpl


class Morph():
    MORPH_TYPES = ['NNG', 'NNP', 'NNB', 'NNM', 'NR', 'NP',
                   'VV', 'VA', 'VX', 'VXV', 'VXA', 'VCP', 'VCN',
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
    _morph_cnt = {} # morphIndex|cnt
    morph_sen = {} # morph index:sen index list
    sen_morphs = {}

    def __init__(self):
        self.reset()

    def reset(self):
        self.morph_dic = []
        self._morph_cnt = {}
        self.morph_sen = {}
        self._sen_morphs = {}

    def morph_typeIndex(self, morph):
        return self.MORPH_TYPES.index(morph)

    def text_morphIndex(self, text:str, morph:str):
        text_morph = "|".join([text, morph])
        try:
            index = self.morph_dic.index(text_morph)
        except ValueError:
            self.morph_dic.append(text_morph)
            index = self.morph_dic.index(text_morph)

        return index

    def registMorphDic(self, text:str, morph:str):
        """
        형태소 사전 ("텍스트|형태소") 에 분석된 텍스트와 형태소 등록
        해쉬 맵을 사용하고, INDEX(INT) 를 사용해 메모리 사용량을 줄인다.
        """
        mtype_index = self.morph_typeIndex(morph)
        if mtype_index in self._morph_cnt:
            cnt = self._morph_cnt.get(mtype_index)
            cnt += 1
            self._morph_cnt.update({mtype_index:cnt})
        else :
            self._morph_cnt.update({mtype_index:1})

        return self.text_morphIndex(text, morph)

    def whereRUFrom(self, senIndex:int, morph:str):
        m_index = self.MORPH_TYPES.index(morph)
        if m_index in self.morph_sen:
            senList:list = self.morph_sen.get(m_index)
            if not senIndex in senList:
                senList.append(senIndex)
                self.morph_sen.update({m_index:senList})
                          
        else : 
            senList = []
            senList.append(senIndex)
            self.morph_sen.update({m_index: senList})

    def set_sen_morphs(self, i, morph_list:list):
        self._sen_morphs.update({i: morph_list})

    def get_sen_morphs(self, i) -> list:
        return self._sen_morphs.get(i)

    def get_morph(self, i:int) -> str:
        return self.morph_dic[i]

    def get_morph_cnt(self, morph):
        cnt = self._morph_cnt.get(self.morph_typeIndex(morph))
        if cnt:
            return self._morph_cnt.get(self.morph_typeIndex(morph))
        else :
            return 0