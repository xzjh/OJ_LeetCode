class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		self.capacity = capacity
		self.visited_list = []
		self.kv_dict = {}

	# @return an integer
	def get(self, key):
		if key not in self.kv_dict:
			return -1
		else:
			self.visited_list.remove(key)
			self.visited_list.insert(0, key)
			return self.kv_dict[key]

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		if key in self.kv_dict:
			self.visited_list.remove(key)
		else:
			if len(self.kv_dict) == self.capacity:
				del self.kv_dict[self.visited_list.pop()]
		self.kv_dict[key] = value
		self.visited_list.insert(0, key)