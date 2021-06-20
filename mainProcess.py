
from nlp.nlp import posTagger
from nlp.data.inputData import NNnlpInputEntry


class MainProcess:

    inputData = NNnlpInputEntry()

    def analyze(self, inputText:str):
        self.inputText = inputText
        sents = posTagger.splitSentence(self.inputText)
        for s in sents:
            analyzed = posTagger.pos(s)

            for tag in analyzed:
                print(tag)

    