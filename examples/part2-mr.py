#  ngram TAB year TAB match_count TAB page_count TAB volume_count NEWLINE
from mrjob.job import MRJob

class BigramAverageCounter(MRJob):
    def mapper(self, _, line):
        tokens = line.strip().split('\t') # split into tokens
        bigram = tokens[0]  # Extract bigram and occurances 
        match_count = tokens[2]
        volume_count = tokens[4]
        yield (bigram, (int(match_count), int(volume_count))) # return the bigram and year

    def reducer(self, bigram, counts):
        total_count = 0
        total_books = 0
        for count, num_books in counts:
          total_count += count
          total_books += num_books
        average_count = total_count / total_books
        yield(bigram, average_count)
        
            
if __name__ == '__main__':
    BigramAverageCounter.run()
