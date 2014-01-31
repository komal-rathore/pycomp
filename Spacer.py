#Program for replaceing multiple space with Single space
#this file is source file
f = open('filespace.txt', 'r')
# Read Contents of target files
st=f.read()
print "Read String ",st

#this file is target file
ws=open("filewithoutspaceFor3.txt",'w')

print "After Remove Space"

#Write content of target file with replacing multiple single space into single one
for x in range(0,len(st)):
    if st[x]==" " and x+1 < len(st):
        if st[x+1]==" ":
            
        else:
            ws.write(st[x])
    else:
        ws.write(st[x])
'''
tr=" koma  l"
for i in range(0,len(tr)):
    if tr[i]==" ":
        print "Do NOTHING:",tr[i]
        
#ws.write(st.replace('  ',''))
'''
ws.close()
f.close()

