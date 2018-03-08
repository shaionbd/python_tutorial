import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.color = {1: 'r', -1: 'g'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)

    #for training
    def fit(self, data):
        self.data = data

        # { |w|: [w,b]}
        opt_dict = {}
        transforms = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        all_data = []

        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)

        # find w, b
        step_size = [self.max_feature_value*.1,
                     self.max_feature_value*.01,
                     # point of expense:
                     self.max_feature_value*.001]
        # extremly expensive
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value*10

        for step in step_size:
            w = np.array([latest_optimum, latest_optimum])

            # convex
            optimized = False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple), self.max_feature_value*b_range_multiple, step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        # week link in the SVM fundamentally
                        # SMO attemps to fix this a bit
                        # yi(xi.w+b) >= 1
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi*(np.dot(w_t, xi)+b) >= 1:
                                    found_option = False
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                if w[0] < 0:
                    optimized = True
                    print("Optimized a step")
                else:
                    # w = [5,5]
                    # step = 1
                    # w-step = [4,4]
                    w = w-step
            norms = sorted([n for n in opt_dict])
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]

            latest_optimum = opt_choice[0][0]+step*2

    #for predict
    def predict(self, features):
        # sign(x.w+b)
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        return classification


data_dict = {-1: np.array([[1,7], [3,4], [7,9]]), 1: np.array([[2,4],[5,1],[6,9]])}