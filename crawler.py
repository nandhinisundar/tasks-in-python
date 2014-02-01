import re, urllib
textfile = file('depth_1.txt','wt')
print("Enter the URL you wish to crawl..")
print('Usage  - "http://google.com/gmail/signup" <-- With the double quotes')
myurl = input("@> ")
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print(i)  
        for j in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print(j)
                textfile.write(j+'\n')
textfile.close()
