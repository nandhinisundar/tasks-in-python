laptop=['hp','dell']
laptop.insert(1,'apple')
top=laptop[0];
print(laptop)
dict={'@':01,'&':02,'$':03}
print(dict['$'])
for i in dict:
	print(i)
class Queue:
	    def __init__(self):
	        self.items = []
	
	    def isEmpty(self):
	        return self.items == []
	
	    def enqueue(self, item):
	        self.items.insert(0,item)
	
	    def dequeue(self):
	        return self.items.pop()
	
	    def size(self):
	        return len(self.items)

q=Queue()
q.isEmpty()
q.enqueue('duck')
q.enqueue('cat')
q.dequeue()
q=Queue()
q.isEmpty()
q.enqueue('three')
q.enqueue('dog')
q.enqueue(True)
