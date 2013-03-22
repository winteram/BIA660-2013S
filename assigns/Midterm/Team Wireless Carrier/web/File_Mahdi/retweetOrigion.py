import re
import sys
import json
import twitter
import networkx as nx
import os
keywds = ['GalaxyS4']
api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')
someTweets = api.GetSearch('GalaxyS4', per_page=200)
#from recipe__get_rt_origins import get_rt_origins
def get_rt_origins(tweet):
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    rt_origins = []
    retweetCheck=api.GetRetweets(tweet.id)
    if retweetCheck != 'Null':
        rt_origins += [tweet.user.screen_name.lower()]
    try:
        rt_origins += [ mention.strip() for mention in rt_patterns.findall(tweet.text)[0][1].split() ]
    except IndexError, e:
        pass
    return list(set([rto.strip("@").lower() for rto in rt_origins]))



def create_rt_graph(tweets):
    g = nx.DiGraph()
    for tweet in tweets:
        rt_origins = get_rt_origins(tweet)
        if not rt_origins:
            continue
        for rt_origin in rt_origins:
            g.add_edge(rt_origin.encode('ascii', 'ignore'), tweet.source.encode('ascii', 'ignore'),{'tweet_id': tweet.id})
    return g


def write_dot_output(g, out_file):
    
    try:
        nx.drawing.write_dot(g, out_file)
        print >> sys.stderr, 'Data file written to', out_file
    except ImportError, e:
        dot = ['"%s" -> "%s" [tweet_id=%s]' % (n1, n2, g[n1][n2]['tweet_id']) for (n1, n2) in g.edges()]
        f = open(out_file, 'w')
        f.write('''strict digraph { %s }''' % (';\n'.join(dot), ))
        f.close()
        print >> sys.stderr, 'Data file written to: %s' % f.name

g = create_rt_graph(someTweets)
OUT = 'twitter_retweet_graph'
if not os.path.isdir('out'):
    os.mkdir('out')
f = os.path.join(os.getcwd(), 'out', OUT)
write_dot_output(g, f)
print >> sys.stderr, 'Try this on the DOT output: $ dot -Tpng -O%s %s.dot' % (f, f,)
