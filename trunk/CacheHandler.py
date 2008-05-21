import traceback
class CacheHandler:
	def getFromCache(self,name):
		return None
	def saveToCache(self,name, toSave):
		return 0

class FileCacheHandler(CacheHandler):
	def getFileName(self, name):
		import os
		import sys
		return os.path.join(sys.path[0],name) +".vp"
		
		
	def saveToCache(self, name, toSave):
		try:
			import pickle
			fh=open(self.getFileName(name), "w")
			pickle.dump(toSave, fh)
			fh.close()
		except:
			traceback.print_exc()
			try:
				fh.close()
			except:
				pass
			return None
			
	def getFromCache(self,name):
		try:
			import pickle
			fh=open(self.getFileName(name), "r")
			a=pickle.load(fh)
			fh.close()
			if (a!=None): print "Cache hit."
			return a
		except:
			traceback.print_exc()
			try:
				fh.close()
			except:
				pass
			return None

class MemoryCacheHandler(CacheHandler):
	def __init__(self):
		self.cache={}
		
	def saveToCache(self,name, toSave):
		self.cache[name]=toSave
		
	def getFromCache(self, name):
		try:
			if (self.cache[name]!=None): print "Cache hit."
			return self.cache[name]
		except:
			traceback.print_exc()
			return None
	
