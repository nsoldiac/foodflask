from nltk.corpus import wordnet as wn

class nico_utilities():

	def __init__(self):
		self.food1 = wn.synset('food.n.01')
		self.food2 = wn.synset('food.n.02')

	def is_food(self,synset):
		temp_list = synset.hypernym_distances()
		temp_item = None
		for i in temp_list:
			if i[0].name() in ['food.n.01', 'food.n.02']: 
				temp_item = 'Yes'
		if temp_item:
			return True
		else:
			return False

	def gimme_synsets(self, word):
		synsets = wn.synsets(word)
		if synsets:
			for n,i in enumerate(synsets):
				if self.is_food(i):
					synsets[n].is_food = True
				else:
					synsets[n].is_food = False

			return synsets
		else:
			return False