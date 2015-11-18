# Used to classify gender of a given item of data;

class BayesClassifier(object):

    def __init(self, data_file):
        self.data = self.__read_data_file(data_file)

    def __read_data_file(self,data_file):
        F = open(data_file, 'r')
        data = []
        while 1:
            line = F.readlines()
            if not line:
                break
            else:
                data.append([float(i) for i in line.split()])
        return data

    def print_data(self):
        """
        output data read from data_file for check.
        :return: None
        """

    def calculate_expectation(self):
        """
        calculate uij @ y = 1 and y = 0;
        :return:
        """

    def calculate_variation(self):
        """
        calcuate vij @ y = 1 and y = 0;
        :return:
        """

    def gender_classifier(self):
        """
        Realization of the algorithm;
        :return:
        """