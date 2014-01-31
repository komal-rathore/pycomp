#Program for replaceing multiple space with Single space
f = open('filespace.txt', 'r')
st=f.read()
print "Read String ",st
ws=open("filewithoutspaceFor3.txt",'w')

print "After Remove Space"

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

