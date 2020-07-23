
import csv
import shutil
import time, glob
import operator
import datetime
date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
sites=[]

s1=".css"
s2=".png"
s3=".ttf"
s4=".svg"
s5=".woff2"
s6=".gif"
s7=".js"
s8=".jpg"
s9=".woff"
s10="demandware"
#merging multiple objects from logs bucket

outfilename="merge.txt"
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('C:/Users/Young_Thug/Downloads/logs/logs/*'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)


#csv from the objects with the total counts

with open('merge.txt') as fh:
    for line in fh:

        # reading each word
        a=line.split()

        for word in a:

            if(word=='"GET'):
                p=a[a.index(word)-len(a)+1]
                q=a[a.index(word)-len(a)+3]
                if((s1 not in p) and (s2 not in p) and (s3 not in p) and (s4 not in p) and (s5 not in p) and (s6 not in p) and (s7 not in p) and (s8 not in p) and (s9 not in p) and (s10 not in p)):
                    if ("?" in p):
                        p=p[:p.index("?")]
                    sites.append((p,q))
P=dict((x,(sites.count((x,y))),y) for (x,y) in set(sites))
R=dict(sorted(P.items(), key=operator.itemgetter(1),reverse=True))
#print(R)


with open('visited_sites_'+date_string+'.csv','w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in R.items():
       writer.writerow([key,value])

File = open('visited_sites_'+date_string+'.csv')

#reading the File with the help of csv.reader()
Reader = csv.reader(File)

#storing the values contained in the Reader into Data
Data = list(Reader)






file = open('visited_sites_'+date_string+'.csv', 'w+')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(Data)
