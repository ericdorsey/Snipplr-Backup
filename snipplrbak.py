import xmlrpclib
import datetime
import htmlentitydefs
import re
import os

# Unsecape function from: http://effbot.org/zone/re-sub.htm#unescape-html 
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

z = xmlrpclib.ServerProxy('http://snipplr.com/xml-rpc.php')

#Declare some datetime stuff
todayd = datetime.date.today()
tform = str(todayd) + '_snipplrbak.txt'
#USER SPECIFIC: Path where you want the backups to go (ie '/Users/myname/dir/subdir')
path = os.path.join('/Users/username/subdir/snipplrbaks', tform)
myfile = open(path, 'w')

#List to hold dictionary for each snip(ID) 
dlist = []

#The Snippler ID's. z.snippet.list('myAPIkey')
ids = []
#USER SPECIFIC: Replace yourUniqueAPIKeyGoesHere with your API key from Snipplr.com
for i in range(len(z.snippet.list('yourUniqueAPIKeyGoesHere'))):
    ids.append(z.snippet.list('yourUniqueAPIKeyGoesHere')[i]['id'])

#Keys we want the values of:
wanted = ['title', 'source', 'language']

#From PyCookbook, pg 170
def sub_dict(somedict, somekeys, default=None):
    return dict([ (k, somedict.get(k, default)) for k in somekeys ])

#Get the values for keys matching "wanted" from "ids" list
for i in ids:
    newdict = sub_dict(z.snippet.get(i), wanted)
    for k, v in newdict.iteritems():
        newdict[k] = unescape(v)
    dlist.append(newdict)

#Write the information to a file
for index, j in enumerate(dlist):
    myfile.write('Title: ' + dlist[index]['title'] + '\n')
    myfile.write('Language: ' + dlist[index]['language'] + '\n')
    myfile.write('Source: ' + '\n' + dlist[index]['source'] +'\n\n')
myfile.close()

#Log results
format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.now()
parsed = today.strftime(format)
#Result of parsed = Sun Sep 13 13:54:11 2009
parsed = parsed + '\n'
#USER SPECIFIC: Change directory to reflect where you want the backup log to go to.
baklog = '/Users/username/subdir/baklog.txt'
logfile = open(baklog, 'a')
logfile.write(parsed)
logfile.close()

