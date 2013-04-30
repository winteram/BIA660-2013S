import numpy as np
from matplotlib import pyplot as plt


N=3
ind=np.arange(N)  #the x locations for the groups
width=0.5  #the width of the bars

fig=plt.figure()
ax=fig.add_subplot(111)

vals=[8.72,13.12,128.12]
colors=['r','b','g']
ax.bar(ind,vals,width,color=colors)

'''microsoft=(55)
rects1=ax.bar(ind,microsoft,width,color='g')

ikea=(57)
rects2=ax.bar(ind+width,ikea,width,color='r')

nestle=(54)
rects3=ax.bar(ind+width+width,nestle,width,color='b')'''

plt.ylim(0,150)


ax.set_ylabel('Number of viewerships (million)')
#ax.set_xlabel('')
ax.set_title('Number of YouTube viewerships')
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ('Super Bowl', 'TV', 'Viral') )
#ax.legend((rects1[0],rects2[0],rects3[0]),('Micorsoft','Ikea','Nestle'))
'''def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2,1.01*height,'%d'%int(height),ha='center',va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.savefig('try.png')'''    
plt.show()

