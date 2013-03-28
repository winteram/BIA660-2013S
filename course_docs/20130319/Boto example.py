# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.emr.connection import EmrConnection
from boto.emr.step import StreamingStep
import boto.emr

# <codecell>

### Adding and deleting files from S3

#s3con = S3Connection('<aws access key>', '<aws secret key>')
s3con = S3Connection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')

# <codecell>

b = s3con.create_bucket('winteram-boto-example')
#b = s3con.get_bucket('winteram-boto-example')

# <codecell>

k = Key(b)
k.key = 'mapper.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/WebAnalytics_2013S/BIA660-2013S/course_docs/20130319/mapper.py')
k.close()

# <codecell>

k = Key(b)
k.key = 'reducer.py'
k.set_contents_from_filename('/Users/winteram/Documents/Teaching/WebAnalytics_2013S/BIA660-2013S/course_docs/20130319/reducer.py')
k.close()

# <codecell>

for word in b.list():
    print word

# <codecell>

### Running code with EMR

#emrcon = EmrConnection('<aws access key>', '<aws secret key>')
emrcon = EmrConnection('0CY3BC386720ZYZNWZ02', 'Jv37SHb/XNeqpY8vMrGeclcL6abfKHKd9Eeh5fmy')

# <codecell>

# Using EMR's wordcount example
step = StreamingStep(name='My wordcount example',
	mapper='s3n://elasticmapreduce/samples/wordcount/wordSplitter.py',
	reducer='aggregate', 
	input='s3n://elasticmapreduce/samples/wordcount/input',
	output='s3n://winteram-boto-example/output/wordcount_output')

# <codecell>

jobid = emrcon.run_jobflow(name='Word Count Example', log_uri='s3://winteram-boto-example/logfiles',steps=[step])

# <codecell>

jobid

# <codecell>

status = emrcon.describe_jobflow(jobid)
print status.state

# <codecell>


# <codecell>


