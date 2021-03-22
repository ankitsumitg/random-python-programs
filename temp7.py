
import json

class SatData:
	def __init__(self, filename='sat.json'):    #input file
		with open(filename) as f:  				#open file and save as dictionary
			self.data = json.load(f)   			 #open JSON file
		self.header = [h['name'] for h in self.data['meta']['view']['columns']][8:]
		self.data = self.data['data']    		#list of lists stored in data
	def save_as_csv(self, dbns, filename='output.csv'):
		data_to_write = []
		for item in self.data:
			if (item[8] in dbns):
				data_to_write.append(item[8:])   	#stores entire line
		with open(filename, 'w') as f:
			f.write(','.join(h for h in self.header) + '\n')  #write header
			for item in data_to_write:
				f.write(','.join(str(i) for i in item)+'\n')


sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)