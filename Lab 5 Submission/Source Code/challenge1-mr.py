"""
part 1 map reduce (bigram, year)

python challenge1-mr.py -r hadoop hdfs:///user/mfeng45/book.txt --output-dir=hdfs:///user/mfeng45/bigramafter1992 --conf-path=mrjob.conf


"""

from mrjob.job import MRJob

class MRBigramAfter1992(MRJob):
    def mapper(self, _, line):            # mapper 
        tokens = line.strip().split('\t') # split into tokens
        bigram = tokens[0]                # extract bigram and year
        year = int(tokens[1])
        yield (bigram, year)              # return the bigram and year

    def reducer(self, bigram, years):
        after1992 = False                 # variables to check if it was after 1992
        before1992 = False
        for year in years:                # for all years 
          if year >= 1992:                # check to see if the year is after or before 1992
            after1992 = True
          if year < 1992:
            before1992 = True
          if after1992 and not before1992: # if so, return the bigram and year 
            yield (bigram, year)

if __name__ == '__main__':
    MRBigramAfter1992.run()