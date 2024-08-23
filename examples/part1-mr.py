"""
part 1 map reduce (bigram, year)

python part1-mr.py -r hadoop hdfs:///user/mfeng45/book.txt --output-dir=hdfs:///user/mfeng45/bigramafter1992 --conf-path=mrjob.conf


"""

#  ngram TAB year TAB match_count TAB page_count TAB volume_count NEWLINE
from mrjob.job import MRJob


class MRBigramAfter1992(MRJob):
    def mapper(self, _, line):
        tokens = line.strip().split('\t') # split into tokens
        bigram = tokens[0]  # Extract bigram and year
        year = int(tokens[1])
        yield (bigram, year) # return the bigram and year

    def reducer(self, bigram, years):
        after1992 = False         # check if it was after 1992
        before1992 = False
        for year in years:
          if year >= 1992:
            after1992 = True
          if year < 1992:
            before1992 = True
          if after1992 and not before1992:
            yield (bigram, year)

if __name__ == '__main__':
    MRBigramAfter1992.run()