
from konlpy.tag import Kkma
import re
import time

class posTagger:

    kkma = Kkma()

    @classmethod
    def pos(self, input:str) -> list:
        result = self.kkma.pos(input)
        return result

    @classmethod
    def splitSentence(self, inputText:str) -> list:
        ''' inputText to list of sentence. '''
        # return re.split('\.[\s]', inputText)  # 0.07초
        try :  
            result = []
            p = re.compile(r'(.*?)([?!.]\s*|$)')
            for s in p.finditer(inputText.replace('\n',' ').strip()):
                # print('!@#!@# s :', s)
                temp = str(s.group(1) + s.group(2)).strip()
                if len(temp) > 0:
                    result.append(temp)
            # result = p.findall(inputText.replace('\n',' ').strip())
            # result = [re.split(r'(.*?)(([?!.])\s*)|$', inputText.replace('\n',' ').strip())] #if s and s[-1] != "."]
            # if len(result) == 0:
            #     result = [inputText.strip()]
            return result # 0.03초
        except IndexError:
            print()

    @classmethod
    def splitEojeol(self, inputText:str) -> list:
        return re.split('[\s]+', inputText)

    @classmethod
    def splitParagraph(self, inputText:str) -> list:
        ''' inputText to list of sentence. '''
        paragraphs = re.split('[\n]+ [\w]', inputText)
        return paragraphs


if __name__ == '__main__':
    input = '''나는 학생으로서 학교생활을 하며 교칙에 묶여서 생활하는 것에'''
# 또 ‘우리가 왜 이런 교칙을 지켜야하는가?’에 대한 의문이 생겼다. 실제로 우리가 다니는 학교에는 수많은 교칙들이 있다.
# 대표적인 예로 ‘두발에 대한 규정’, ‘교복착용 및 단정한 모습’등이 있다. 문제가 되는 교칙들을 줄여나가는 노력이 이어지고 있지만 실제로 폐지한 곳은 많지 않다.
# (노컷 뉴스)실제 대전에 있는 한 고등학교에서는 학생들이 자발적으로 교칙에 대하여 폐지를 요구하였지만 받아들여지지 않았다.
# 나는 이렇게 학교에서 인권을 침해하고 있다고 생각한다. 또 인권을 침해하는 교칙과 제도가 폐지되어야한다고 생각한다. 첫 번째, ‘두발 규정‘과 ’교복착용 및 단정한 모습‘이라는 교칙의 인권침해와 폐지되어야 하는 이유에 대하여 소개하여 보겠다.
# 이 두 교칙에 대하여 인권침해의 소지가 있다는 논란은 많이 있었다. 하지만 교칙들은 현재도 남아있다.
# 교칙들이 인권을 침해한다는 증거로는 세계 인권 선언에 “제23조 내가 원하는 일을 자유롭게 할 수 있다.”(네이버 지식백과)라는 조항에 완전히 어긋난다.
# 이 조항을 보면 말 그대로 인간들은 자신이 원하는 일을 자유로이 할 수 있다. 학생들도 마찬가지이다. 하지만 교칙들은 학생들은 틀 안에 가두고 자신의 생각과 마음을 표출하지 못하도록 하고 있다고 생각한다.
# 또 학생들의 개성과 취향을 존중해 주지 못한다. (노컷뉴스)그리고 이러한 교칙들로 인해 한 기사에서는 ’지난해 대전청소년인권네트워크 조사에서 대전지역 고등학생의 54%가 \'인권이 침해당하고 있다\'고 응답한 바 있다.‘라고 한다.
# 두 번째, 내신제도로 인한 인권침해이다. 우리나라의 내신제도는 학생들을 교실 안에만 가두어 정확한 목적을 알지  못한 채 그저 공부만 하도록 강요하고 있다.
# 그리고 학생들은 그저 수동적으로 수업만을 들을 뿐 능동적으로 질문을 하거나 자신의 생각을 표현할 기회가 거의 없다. 선생님들 또한 자신이 진정으로 가르치고 싶은 것은 제쳐두고 국가나 시에서 원하는 교육을 시켜주어야 한다.
# 실제 내신제도에 대하여 비판을 하는 책에서는 선생님인 작가와 그의 동료는 수업을 할 때마다 죄책감을 느낀다고 한다. 이러한 문제점들 또한 세계인권 선언 “19조 생각하고 표현하는 것은 자유이다.”라는 것에 어긋난다.
# (네이버 지식백과)그러므로 우리나라의 내신은 학생들이 경쟁에서 벗어나 자신의 생각을 자유롭게 표현하고 선생님들은 자신이 진정 가르치고 싶은 것들을 가르칠 수 있도록 폐지되어야 한다고 생각된다.
# 학생들의 인권을 침해하는 ‘두발규정’과 ‘교복착용과 단정한 모습’, 학생과 선생님의 인권을 침해하는 ‘내신제도’는 수정되거나 폐지되어야 마땅하다.
# 이러한 교칙과 제도의 폐지를 통하여 학생들은 자신의 개성과 생각을 마음껏 드러내며 자신의 목적을 찾아내고 선생님들은 자신이 원하는 수업을 학생들에게 가르치며 진정한 스승이 될 수 있을 것이다'''

    start = time.time()
    print(posTagger.splitSentence(input))
    # print(posTagger.splitEojeol(input))
    
    # for i in range(10000):
    #     for r in posTagger.splitSentence(input):
    #         result = posTagger.pos(r)
    #         print(result)
    #         print(type(result))
    print()
    print('time : ', time.time() - start)