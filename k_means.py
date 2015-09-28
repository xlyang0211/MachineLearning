__author__ = 'seany'
# NOTE
# (In following narration, i is the index of dot (x), j is the index of centroid (u), and c[i] denote the index of
#  centroid x[i] belongs to.)
# 1. get_c is actually get the index of u (centroid) which is the nearest centroid to x[i];
# 2. get_u is actually calculate the updated centroid by computing average position of x[i] which choose u[j] as their
#    nearest centroid;
# 3. the outer iteration can be interpreted as follows:
#    1. while every u[j] is updated, for every x[i], it needs to re-choose the nearest centroid it belongs to;
#    2. then according to x[i] around every centroid u[j], update the centroid;
# 4. How to decide if the algorithm has converge or not?
#    We calculate the J = sum of square of distance between every x[i] and its centroid u[c[i]], if after a iteration,
#    J_new is bigger than J_old (which the value of J in last iteration), we say it converges;

# Special Notice:
# 1.
# One critical problem is that if in certain iteration, for certain u[j], if their is no x[i] take it as its centroid,
# then to update u[j], the formula:
#                             u[j] = sum_of_all_i(1{c[i] = j} * x[i]) / sum_of_all_i(1{c[i] = j})
# How could we solve the problem? in this algorithm, we take use of the scheme of not updating u[j] if the denominator
# of u[j] is 0 (which means there is not c[i] = j); But actually we should choose a reasonable initial value for u[j]
# so that the algorithm can tell the different group of dot clustering apart. E.g. if we choose u to be [[3, 3], [4, 4]]
# then we can not run the algorithm successfully. Here the algorithm manifests a lack of robustness. deep research is
# still pending !!!


import matplotlib.pyplot as plt

class KMEANS:
    def get_c(self, x, u, c):
        for i in xrange(len(x)):
            c_tmp = 0
            distance = float('inf')
            for j in xrange(len(u)):
                if self.get_distance(x[i], u[j]) < distance:
                    distance = self.get_distance(x[i], u[j])
                    c_tmp = j
            c[i] = c_tmp

    def get_u(self, x, u, c):
        for j in xrange(len(u)):
            a = [0, 0]
            b = 0
            for i in xrange(len(x)):
                if c[i] == j:
                    a[0] += x[i][0]
                    a[1] += x[i][1]
                    b += 1
            if b:
                u[j][0] = a[0] / b
                u[j][1] = a[1] / b

    def find_convergence(self, x, u):
        old = float('inf')
        c = [0] * len(x)
        new = self.get_j(x, u, c)
        while new < old:
            # get c;
            self.get_c(x, u, c)
            # get u;
            self.get_u(x, u, c)
            old = new
            new = self.get_j(x, u, c)
        return c

    def get_j(self, x, u, c):
        j = 0
        for i in xrange(len(x)):
            j += self.get_distance(x[i], u[c[i]])
        return j

    def get_distance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


if __name__ == "__main__":
    # unsupervised learning, not labels
    x = [[0.8, 0.8],
         [0.7, 1.1],
         [1.1, 1.3],
         [1.4, 1.05],
         [1.81, 1.5],
         [2.1, 1.89],
         [1.83, 1.91],
         [0.75, 1.09],
         [1.1, 0.6],
         [2.4, 2],
         [1.79, 2.01]]
    # show x in coordinates;
    u = [[1.5, 1.5], [1.55, 1.55]]
    k_means = KMEANS()
    c = k_means.find_convergence(x, u)
    count = 0
    for i in x:
        if c[count] == 0:
            plt.plot(i[0], i[1], "rD", linewidth=16)
        else:
            plt.plot(i[0], i[1], "bs", linewidth=16)
        count += 1
    plt.plot(u[0][0], u[0][1], "ro", label="centroid_0", markersize=16)
    plt.plot(u[1][0], u[1][1], "bo", label="centroid_1", markersize=16)
    l=[0, 2.5, 0, 2.5]
    plt.axis(l)
    plt.show()