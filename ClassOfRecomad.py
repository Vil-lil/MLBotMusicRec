from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
class RecommendationsInterface:

    def ProcessingRequest(self, x: list):

        '''input: massage in list
            output: dict values
            Функция принимает в себя массив и переберает его.
            '''

        new_dataset = {
            'рок': 0,
            'поп': 0,
            'классика': 0,
            'реп': 0,
            'металл': 0,
            'инди': 0,
            'тренируюсь': 0,
            'засыпаю': 0,
            'просыпаюсь': 0,
            'в_дороге': 0,
            'работаю': 0,
            'бодрое': 0,
            'грустное': 0,
            'спокойно': 0
        }

        for i in x:
            if i == 'рок':
                new_dataset['рок'] = 1
            if i == 'поп':
                new_dataset['поп'] = 1
            if i == 'классика':
                new_dataset['классика'] = 1
            if i == 'реп':
                new_dataset['реп'] = 1
            if i == 'металл':
                new_dataset['металл'] = 1
            if i == 'инди':
                new_dataset['инди'] = 1
            if i == 'тренируюсь':
                new_dataset['тренируюсь'] = 1
            if i == 'засыпаю':
                new_dataset['засыпаю'] = 1
            if i == 'просыпаюсь':
                new_dataset['просыпаюсь'] = 1
            if i == 'в дороге':
                new_dataset['в_дороге'] = 1
            if i == 'работаю':
                new_dataset['работаю'] = 1
            if i == 'бодрое':
                new_dataset['бодрое'] = 1
            if i == 'грустное':
                new_dataset['грустное'] = 1
            if i == 'спокойно':
                new_dataset['спокойно'] = 1

        print(new_dataset)

        return np.array(list(new_dataset.values()))

    def LinkProcessing(self, LinkString: str) -> str:

        Link = ''

        for i in LinkString:

            if ( i not in ('[', ']', "'") ):

                Link += i

        return Link

    def NewMlModel(self, PreferenceList: list):

        '''
        :param PreferenceList: ["рок", "негативное" ......]
        :return: "https://.........yandexmusic.com"
        '''

        DATASET = pd.read_excel('TTBB2.xlsx')#название таблицы закину позже
        MODEL = DecisionTreeClassifier()

        ModelParameters = DATASET.drop("SONGS",axis=1)
        ModelPifstobz = DATASET["SONGS"]

        print(ModelPifstobz)

        MODEL.fit(ModelParameters, ModelPifstobz)

        print("**************************************MODEL IS FIT**************************************")
        print(PreferenceList)
        print(np.array(self.ProcessingRequest(PreferenceList)).reshape(1, -1))
        return self.LinkProcessing(MODEL.predict(self.ProcessingRequest(PreferenceList).reshape(1,-1)))

    def TESTLINKPROCESSING(self, LINK, LINK_TRUE):

        if (self.LinkProcessing(LINK) == LINK_TRUE):

            print('''
                The test was successful,\n
                the method works as it should
            ''')

            return True



