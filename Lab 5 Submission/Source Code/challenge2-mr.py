"""
part 2 map reduce (bigram, average)

python challenge2-mr.py -r hadoop hdfs:///user/mfeng45/book.txt --output-dir=hdfs:///user/mfeng45/average --conf-path=mrjob.conf


"""

from mrjob.job import MRJob

class BigramAverageCounter(MRJob):
    def mapper(self, _, line):                                # mapper      
        tokens = line.strip().split('\t')                     # split into tokens
        bigram = tokens[0]                                    # extract bigram and occurances 
        match_count = tokens[2]
        volume_count = tokens[4]
        yield (bigram, (int(match_count), int(volume_count))) # return the bigram, match_count, and volume_count

    def reducer(self, bigram, counts):                        # reducer 
        total_count = 0                                       # get occurances 
        total_books = 0
        for count, num_books in counts:                       # get the average 
          total_count += count
          total_books += num_books
        average_count = total_count / total_books
        yield(bigram, average_count)                          # return average 
        
            
if __name__ == '__main__':
    BigramAverageCounter.run()
