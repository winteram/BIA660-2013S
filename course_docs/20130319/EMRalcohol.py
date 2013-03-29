from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto.emr

### Adding and deleting files from S3
#s3con = S3Connection('<aws access key>', '<aws secret key>')
s3con = S3Connection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')
b = s3con.get_bucket('bia660-winter')

k = Key(b)
k.key = 'mapper.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/WebAnalytics_2013S/BIA660-2013S/course_docs/20130319/mapper.py')
k.close()

k = Key(b)
k.key = 'reducer.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/WebAnalytics_2013S/BIA660-2013S/course_docs/20130319/reducer.py')
k.close()


### Running code with EMR
#emrcon = EmrConnection('<aws access key>', '<aws secret key>')
emrcon = EmrConnection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')

step = StreamingStep(name='Alcohol Step',
	mapper='s3n://bia660-winter/mapper.py',
	reducer='s3n://bia660-winter/reducer.py', 
	input='s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/3gram/data',
	output='s3n://bia660-winter/output/alcohol_religion')

jobid = emrcon.run_jobflow(name='Alcohol Religion 7', log_uri='s3://bia660-winter/logfiles',steps=[step],num_instances=4)
print "Job created: %s" % jobid

status = emrcon.describe_jobflow(jobid)
print status.state



