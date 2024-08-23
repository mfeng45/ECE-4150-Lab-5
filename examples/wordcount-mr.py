"""
use this line in Hadoop to run wordcount mapreduce program:
number of occurances

python wordcount-mr.py -r hadoop hdfs:///user/mfeng45/book.txt --output-dir=hdfs:///user/mfeng45/wordcountoutput --conf-path=mrjob.conf

"""

from mrjob.job import MRJob

class MRmyjob(MRJob):
	def mapper(self, _, line):
		wordlist = line.split()
		for word in wordlist:
			yield word,1

	def reducer(self, key, list_of_values):
		yield key,sum(list_of_values)

if __name__ == '__main__':
    MRmyjob.run()




