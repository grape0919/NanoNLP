class Morph():

    CHECKBOX_INDEX = ['체언', '용언', '감탄사',
                  '관형사', '부사',
                  '조사', '어미',
                  '선어말어미',
                  '어말어미',
                  '종결어미',
                  '연결어미,전성어미',
                  '접두사', '접미사', '어근']

    
    체언 = ['NNG', 'NNP', 'NNB', 'NNM', 'NR','NP']
    용언 = ['VV', 'VA', 'VXV', 'VXA', 'VCP', 'VCN']
    관형사 = ['MDT', 'MDN']
    부사 = ['MAG', 'MAC']
    감탄사 = ['IC']
    조사 = ['JKS', 'JKC', 'JKG', 'JKO', 'JKM', 'JKI', 'JKQ', 'JX', 'JC']
    선어말어미 = ['EPH', 'EPT', 'EPP']
    종결어미 = ['EFN', 'EFQ', 'EFO', 'EFA', 'EFI', 'EFR']
    연결어미 = ['ECE', 'ECD', 'ECS']
    전성어미 = ['ETN', 'ETD']
    어말어미 = 종결어미 + 연결어미 + 전성어미
    어미 = 선어말어미 + 어말어미
    접두사 = ['XPN', 'XPV']
    접미사 = ['XSN', 'XSV', 'XSA', 'XSM', 'XSO']
    어근 = ['XR']
    부호 = ['SF', 'SP', 'SS', 'SE', 'SO', 'SW']
    분석불능 = ['UN', 'UV', 'UE']
    한글이외 = ['OL', 'OH', 'NR']
    

    CHECKBOX_MAPPING = {0:체언, 1:용언, 2:감탄사,
                  3:관형사, 4:부사,
                  5:조사, 6:어미,
                  7:선어말어미,
                  8:어말어미,
                  9:종결어미,
                  10:연결어미 + 전성어미,
                  11:접두사, 12:접미사, 13:어근}

    @classmethod
    def get_checkbox_morph_list(self, checkbox_index:int):
        return Morph.CHECKBOX_MAPPING[checkbox_index]
