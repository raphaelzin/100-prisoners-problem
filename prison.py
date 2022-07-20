from prisoner import LoopStrategy, Prisoner, RandomStrategy
import random

class Prison:
	def __init__(self, capacity, tries):
		self.capacity = capacity
		self.prisoners = []
		self.tries = tries
		
		l = list(range(capacity))
		random.shuffle(l)
		
		self.boxes = l
		for number in range(capacity):
			self.prisoners.append(Prisoner(number, RandomStrategy()))
	
	def runExperiment(self) -> int:
		failCount = 0
		for prisoner in self.prisoners:
			didFindSelf = prisoner.searchBoxes(self.boxes, self.tries)
			if not didFindSelf:
				failCount += 1
		return failCount
	
	def detectLoops(self):
		visited = set()
		loops = []
		index = 0

		for i in range(self.capacity):
			if i in visited:
				continue
			curr = []
			index = i
			while self.boxes[index] not in visited:
				index = self.boxes[index]
				curr.append(index)
				visited.add(index)
			loops.append(curr)
		return loops