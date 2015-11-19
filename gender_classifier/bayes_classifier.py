# Used to classify gender of a given item of data;
from math import sqrt
from math import pi, exp

class BayesClassifier(object):

    def __init__(self, data_file, test_data_file):
        self.data_title, self.data = self.__read_data_file(data_file)
        self.test_data = self.__read_test_data(test_data_file)
        self.u_male = []
        self.u_female = []
        self.v_male = []
        self.v_female = []

    def __read_data_file(self,data_file):
        F = open(data_file, 'r')
        title = []
        data = []
        count = 0
        while 1:
            line = F.readline()
            if not line:
                break
            else:
                if count == 0:
                    title = line.split()
                else:
                    data.append(line.split()[0:1] + [float(i) for i in line.split()[1:]])
                count += 1
        F.close()
        return title, data

    def print_data(self):
        """
        output data read from data_file for check.
        :return: None
        """
        num = len(self.data_title)
        format = "%20s%20s%20s%20s"
        print("%20s%20s%20s%20s" % tuple(self.data_title))
        for data in self.data:
            print format % tuple([str(i) for i in data])

    def calculate_expectation(self):
        """
        calculate uij @ y = 1 and y = 0;
        :return:
        """
        # calculate expectation:
        num_features = len(self.data[0]) - 1
        self.u_male = [0] * num_features
        self.u_female = [0] * num_features
        male_count = 0
        female_count = 0
        for data in self.data:
            if data[0] == "male":
                male_count += 1
            else:
                female_count += 1
            for i in xrange(num_features):
                if data[0] == "male":
                    self.u_male[i] += data[i + 1]
                else:
                    self.u_female[i] += data[i + 1]
        print "male count is: ", male_count
        print "female count is: ", female_count
        self.u_male = [ i / male_count for i in self.u_male]
        self.u_female = [i / female_count for i in self.u_female]

    def calculate_variation(self):
        """
        calcuate vij @ y = 1 and y = 0;
        :return:
        """
        num_features = len(self.data[0]) - 1
        self.v_male = [0] * num_features
        self.v_female = [0] * num_features
        male_count = 0
        female_count = 0
        for data in self.data:
            for i in xrange(num_features):
                if data[0] == "male":
                    male_count += 1
                    self.v_male[i] += (data[i + 1] - self.u_male[i]) ** 2
                else:
                    female_count += 1
                    self.v_female[i] += (data[i + 1] - self.u_female[i]) ** 2
        self.v_male = [sqrt(i / male_count) for i in self.v_male]
        self.v_female = [sqrt(i / female_count) for i in self.v_female]

    def gender_classifier(self):
        """
        Realization of the algorithm;
        :return:
        """
        # calculate expectation and variable:
        self.calculate_expectation()
        self.calculate_variation()
        print "u_male is: ", self.u_male
        print "u_female is: ", self.u_female
        print "v_male is: ", self.v_male
        print "v_female is: ", self.v_female
        num_test_data = len(self.test_data)
        result_male = [0] * num_test_data
        result_female = [0] * num_test_data
        result = []
        for i in xrange(num_test_data):
            test_data = self.test_data[i]
            m_numerator = 1
            f_numerator = 1
            num_features = len(test_data)
            for j in xrange(num_features):
                m_numerator *= self.gaussian(self.u_male[j], self.v_male[j], test_data[j])
                f_numerator *= self.gaussian(self.u_female[j], self.v_female[j], test_data[j])
            result_male[i] = m_numerator / (m_numerator + f_numerator)
            result_female[i] = f_numerator / (m_numerator + f_numerator)
            if result_male[i] > result_female[i]:
                result.append('male')
            else:
                result.append('female')
        print result_male
        print result_female
        return result

    def gaussian(self, u, v, x):
        return 1 / (2 * pi * v) * exp(-(x - u) ** 2 / (2 * v ** 2))

    def __read_test_data(self, test_data_file):
        test_data = []
        F = open(test_data_file, 'r')
        while 1:
            line = F.readline()
            if not line:
                break
            else:
                test_data.append([float(i) for i in line.split()])
        F.close()
        return test_data


if __name__ == "__main__":
    bayes_classifier = BayesClassifier('./data_set', './test_data')
    bayes_classifier.print_data()
    print bayes_classifier.gender_classifier()

