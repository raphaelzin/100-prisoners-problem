from abc import ABC, abstractmethod
import random

class Prisoner:
	def __init__(self, number, strategy):
		self.strategy = strategy
		self.number = number
		
	def searchBoxes(self, boxes: list[int], tries: int) -> bool:
		return self.strategy.search(boxes, self.number, tries)

class SearchStrategy(ABC):

	@abstractmethod
	def search(self, boxes: list[int], target: int, tries: int) -> bool:
		pass

class RandomStrategy(SearchStrategy):

	def search(self, boxes: list[int], target: int, tries: int) -> bool:
		options = list(range(len(boxes)))
		for _ in range(tries):
			index = random.choice(options)
			options.remove(index)
			if boxes[index] == target:
				return True
		return False

class LoopStrategy(SearchStrategy):
	
	def search(self, boxes: list[int], target: int, tries: int) -> bool:
		index = target
		for _ in range(tries):
			if boxes[index] == target:
				return True
			index = boxes[index]
		return False