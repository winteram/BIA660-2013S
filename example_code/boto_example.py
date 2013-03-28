from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep

### Adding and deleting files from S3

#s3con = S3Connection('<aws access key>', '<aws secret key>')
s3con = S3Connection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')

b = s3con.create_bucket('winteram-boto-example')
#b = s3con.get_bucket('winteram_boto_example')

k = Key(b)
k.key = 'ca-HepPh'
k.set_contents_from_filename('ca-HepPh.txt.gz')
k.close()

k = Key(b)
k.key = 'mapper'
k.set_contents_from_filename('mapper.py')
k.close()

k = Key(b)
k.key = 'reducer'
k.set_contents_from_filename('reducer.py')
k.close()

b.list()

### Running code with EMR

#emrcon = EmrConnection('<aws access key>', '<aws secret key>')
emrcon = EmrConnection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')


# Using EMR's wordcount example
step = StreamingStep(name='My wordcount example',
	mapper='s3n://elasticmapreduce/samples/wordcount/wordSplitter.py',
	reducer='aggregate', 
	input='s3n://elasticmapreduce/samples/wordcount/input',
	output='s3n://winteram_boto_example/output/wordcount_output')


# Running mapper & reducer code from assignment
step = StreamingStep(name='Alcohol and Religion',
	mapper='s3n://winteram_boto_example/mapper.py',
	reducer='s3n://winteram_boto_example/reducer.py', 
	input='s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/3gram/data',
	output='s3n://winteram_boto_example/output/alcohol_religion')

b.list()

# get contents to file
k = Key(b)
k.key = 'alcohol_religion'
k.get_contents_to_filename('ngram_freq.txt')


