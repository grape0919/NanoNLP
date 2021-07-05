
from nlp.data.morphDic import Morph
from nlp.data.dataImpl import DataImpl

class NNnlpInputEntry():
    inputText = ''

    n_letters = 0  # 글자수
    n_eumjeol = 0  # 음절수
    n_morph = 0  # 형태소 수 : 전체 형태소 분석 결과 - 부호 수
    n_word = 0  # 단어 수 : 체언+용언+관형사+부사+감탄사+조사+어근+한글이외
    n_eojeol = 0  # 어절 수 : 띄어쓰기 기준 (이전에는 어절 분석 결과에서 '전체 어절 셀' - '부호 수'로 계량하였음.)
    n_jeol = 0 # 절 수 : VV+VA+VCP+VCN  (=명사절, 관형절, 부사절의 서술어 계량)
    n_sentences = 0 # 문장 수 : . 작은따옴표나 큰따옴표 안에 온점(.)을 포함하고 있는 것(직접인용절) 제외
    n_paragraph = 0 # 문단 수 : 줄 끝에서 엔터를 친 경우

    #######################
    n_real_morph = 0 # 실질 형태소 수 : 체언+용언+관형사+부사+감탄사+어근+한글이외
    n_grammar_morph = 0 # 문법 형태소 수 : VCP+조사+어미+접두사+접미사
    n_josa = 0 # 조사 수
    n_tail = 0 # 어미 수 : 선어말어미+어말어미

    #######################
    MLU_morph = 0.0 # MLU-형태소 : 형태소 수/문장 수
    MLU_word = 0.0 # MLU-단어 : 단어 수/문장 수
    MLU_eojeol = 0.0 # MLU-어절 : 어절 수/문장 수
    MLU_jeol = 0.0 # MLU-절 : 절 수/문장 수

    #######################

    sentenceList = []

    #######################

    all_output = []

    morphDic = Morph()

    def reset(self):
        self.inputText = ''

        self.n_letters = 0  # 글자수
        self.n_lettersIncldSpc = 0  # 글자수 공백포함
        self.n_morph = 0  # 형태소 수 : 전체 형태소 분석 결과 - 부호 수
        self.n_word = 0  # 단어 수 : 체언+용언+관형사+부사+감탄사+조사+어근+한글이외
        self.n_eojeol = 0  # 어절 수 : 띄어쓰기 기준 (이전에는 어절 분석 결과에서 '전체 어절 셀' - '부호 수'로 계량하였음.)
        self.n_jeol = 0 # 절 수 : VV+VA+VCP+VCN  (=명사절, 관형절, 부사절의 서술어 계량)
        self.n_sentences = 0 # 문장 수 : . 작은따옴표나 큰따옴표 안에 온점(.)을 포함하고 있는 것(직접인용절) 제외
        self.n_paragraph = 0 # 문단 수 : 줄 끝에서 엔터를 친 경우

        #######################
        self.n_real_morph = 0 # 실질 형태소 수 : 체언+용언+관형사+부사+감탄사+어근+한글이외
        self.n_grammar_morph = 0 # 문법 형태소 수 : VCP+조사+어미+접두사+접미사
        self.n_josa = 0 # 조사 수
        self.n_tail = 0 # 어미 수 : 선어말어미+어말어미

        #######################
        self.MLU_morph = 0.0 # MLU-형태소 : 형태소 수/문장 수
        self.MLU_word = 0.0 # MLU-단어 : 단어 수/문장 수
        self.MLU_eojeol = 0.0 # MLU-어절 : 어절 수/문장 수
        self.MLU_jeol = 0.0 # MLU-절 : 절 수/문장 수

        #######################
        self.sentenceList = []
        self.all_output = []
        self.morphDic.reset()
    