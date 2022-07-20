import matplotlib.pyplot as plt

class Plotter:

    def __init__(self):
        pass

    def plot(self, results):
        occurrences = {}
        for result in results:
            if result in occurrences:
                occurrences[result] = occurrences[result] + 1
            else:
                occurrences[result] = 1

        xAxis = list(range(1,101))
        yAxis = list(map((lambda x: occurrences[x] if x in occurrences else 0), xAxis))

        plt.bar(xAxis, yAxis)
        plt.ylabel(f'Number of experiments out of {len(results)}')
        plt.xlabel('Number of prisioners who found their numbers')
        plt.grid(True)
        plt.show()