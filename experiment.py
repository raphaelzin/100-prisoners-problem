
from prison import Prison
from plotter import Plotter

experimentCount = 10000
experimentFailCount = 0
foundOwnNumberCount = []

for _ in range(experimentCount):
	prison = Prison(100, 50)
	
	p_failures = prison.runExperiment()
	if p_failures != 0:
		experimentFailCount += 1
	foundOwnNumberCount.append(100-p_failures)

failure_rate = (experimentFailCount/experimentCount)
print(f"{experimentFailCount} failures out of {experimentCount} ({100*failure_rate:.1f}%). Success of {(1-failure_rate)*100:.1f}%")    
plt = Plotter()
plt.plot(foundOwnNumberCount)

