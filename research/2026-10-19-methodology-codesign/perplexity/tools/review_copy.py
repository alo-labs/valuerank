import sys
src=open(sys.argv[1]).read().split('\n'); name=sys.argv[3]
out=[]
for line in src:
    if line.startswith('Revision history'):
        out.append(f'Revision history: omitted from this review copy (not normative); it is in {name} in the same folder of the repository.'); continue
    if len(line)>20000:
        pieces=line.split('; '); cur=''; chunks=[]
        for p in pieces:
            cand=(cur+'; '+p) if cur else p
            if len(cand)>15000 and cur: chunks.append(cur+';'); cur=p
            else: cur=cand
        chunks.append(cur); out.extend(chunks); continue
    out.append(line)
open(sys.argv[2],'w').write('\n'.join(out))
