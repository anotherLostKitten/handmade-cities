import mdl,math,subprocess
def asg(l,v,i=0):
    l[i]=v
def md(x,y):
    z=x.copy()
    z.update(y)
    return z
class Img:
    def __init__(self,r,c):
        self.c,self.r,self.img,self.zbuf,self.lns,self.ln,self.s,self.oof,self.pgs,self.fxmldr,self.mrlongphongdongwong=c,r,[0]*r*c,[float("-inf")]*r*c,(lambda p,w=0:[[self.ln(r-round(p[i+1]/p[i+3]),round(p[i]/p[i+3]),p[i+2]/p[i+3],r-round(p[i+5]/p[i+7]),round(p[i+4]/p[i+7]),p[i+6]/p[i+7],w)for i in range(0,len(p),8)],self][1]),(lambda rs,cs,zs,rf,cf,zf,v,e=[0,0]:self.ln(rf,cf,zf,rs,cs,zs,v)if(rs>rf if abs(rf-rs)<abs(cf-cs)else cs>cf)else(([asg(e,rs,1),asg(e,2*abs(rf-rs)-abs(cf-cs)),[[self.s(e[1],c,v,zs+(zf-zs)*(cs-c)/(cs-cf)),asg(e,e[1]+1,1),asg(e,e[0]+2*abs(rf-rs)-2*abs(cf-cs))]if 0<e[0]else[self.s(e[1],c,v,zs+(zf-zs)*(cs-c)/(cs-cf)),asg(e,e[0]+2*abs(rf-rs))]for c in range(cs,cf-1 if cs>cf else cf+1,-1 if cs>cf else 1)]]if cs!=cf else self.s(rs,cs,v,zs))if abs(rf-rs)<abs(cf-cs)else([asg(e,cs,1),asg(e,2*abs(cf-cs)-abs(rf-rs)),[[self.s(r,e[1],v,zs+(zf-zs)*(rs-r)/(rs-rf)),asg(e,e[1]+1,1),asg(e,e[0]+2*abs(cf-cs)-2*abs(rf-rs))]if 0<e[0]else[self.s(r,e[1],v,zs+(zf-zs)*(rs-r)/(rs-rf)),0,asg(e,e[0]+2*abs(cf-cs))]for r in range(rs,rf-1 if rs>rf else rf+1,-1 if rs>rf else 1)]])if rs!=rf else self.s(rs,cs,v,zs))),(lambda r,c,v,z:[asg(self.img,v,c+r*self.c),asg(self.zbuf,z,c+r*self.c)]if-1<r<self.r and-1<c<self.c and z>self.zbuf[c+r*self.c]else 0),(lambda:"P3 "+str(self.c)+" "+str(self.r)+" 255\n"+" ".join(str(math.floor(i/65536)%256)+" "+str(math.floor(i/256)%256)+" "+str(i%256) for i in self.img)+"\n"),(lambda p,l,u=None,t=None:[[self.mrlongphongdongwong(p,i,l,u=u,t=t)for i in range(0,len(p.m),12)if p.bfc(i,(0,0,1))>0],self][1]),(lambda x,y,z,a,b,c,d,e,f,t:[[self.ln(round(p[0][0]+(p[2][0]-p[0][0])*(r-p[0][1])/(p[2][1]-p[0][1])),r,p[0][2]+(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1]),round(p[0][0]+(p[1][0]-p[0][0])*(r-p[0][1])/(p[1][1]-p[0][1])),r,p[0][2]+(p[1][2]-p[0][2])*(r-p[0][1])/(p[1][1]-p[0][1]),t)if r<p[1][1]else self.ln(round(p[0][0]+(p[2][0]-p[0][0])*(r-p[0][1])/(p[2][1]-p[0][1])),r,p[0][2]+(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1]),round(p[1][0]+(p[2][0]-p[1][0])*(r-p[1][1])/(p[2][1]-p[1][1])),r,p[1][2]+(p[2][2]-p[1][2])*(r-p[1][1])/(p[2][1]-p[1][1]),t)for r in range(p[0][1],p[2][1])]for p in [sorted([[x,y,z],[a,b,c],[d,e,f]],key=lambda q:q[1])]]),(lambda pogm,i,l,u=None,t=None:[[[[[self.s(s,r,pogm.collapsethelightintoearth([p[0][3][frt]+(p[2][3][frt]-p[0][3][frt])*(r-p[0][1])/(p[2][1]-p[0][1])+((p[1][3][frt]-p[0][3][frt])*(r-p[0][1])/(p[1][1]-p[0][1])-(p[2][3][frt]-p[0][3][frt])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0])for frt in(0,1,2)],l,u if t==None else t.t[round(p[0][4][0]+(p[2][4][0]-p[0][4][0])*(r-p[0][1])/(p[2][1]-p[0][1])+((p[1][4][0]-p[0][4][0])*(r-p[0][1])/(p[1][1]-p[0][1])-(p[2][4][0]-p[0][4][0])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))][round(p[0][4][1]+(p[2][4][1]-p[0][4][1])*(r-p[0][1])/(p[2][1]-p[0][1])+((p[1][4][1]-p[0][4][1])*(r-p[0][1])/(p[1][1]-p[0][1])-(p[2][4][1]-p[0][4][1])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))]),p[0][2]+(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1])+((p[1][2]-p[0][2])*(r-p[0][1])/(p[1][1]-p[0][1])-(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))for s in range(*sorted(xs))]for xs in[[round(p[0][0]+(p[2][0]-p[0][0])*(r-p[0][1])/(p[2][1]-p[0][1])),round(p[0][0]+(p[1][0]-p[0][0])*(r-p[0][1])/(p[1][1]-p[0][1]))]]]if r<p[1][1]else[[self.s(s,r,pogm.collapsethelightintoearth([p[0][3][frt]+(p[2][3][frt]-p[0][3][frt])*(r-p[0][1])/(p[2][1]-p[0][1])+(p[1][3][frt]+(p[2][3][frt]-p[1][3][frt])*(r-p[1][1])/(p[2][1]-p[1][1])-p[0][3][frt]-(p[2][3][frt]-p[0][3][frt])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0])for frt in(0,1,2)],l,u if t==None else t.t[round(p[0][4][0]+(p[2][4][0]-p[0][4][0])*(r-p[0][1])/(p[2][1]-p[0][1])+(p[1][4][0]+(p[2][4][0]-p[1][4][0])*(r-p[1][1])/(p[2][1]-p[1][1])-p[0][4][0]-(p[2][4][0]-p[0][4][0])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))][round(p[0][4][1]+(p[2][4][1]-p[0][4][1])*(r-p[0][1])/(p[2][1]-p[0][1])+(p[1][4][1]+(p[2][4][1]-p[1][4][1])*(r-p[1][1])/(p[2][1]-p[1][1])-p[0][4][1]-(p[2][4][1]-p[0][4][1])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))]),p[0][2]+(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1])-((p[2][2]-p[1][2])*(r-p[1][1])/(p[2][1]-p[1][1])-(p[2][2]-p[0][2])*(r-p[0][1])/(p[2][1]-p[0][1]))*(s-xs[0])/(xs[1]-xs[0]))for s in range(*sorted(xs))]for xs in[[round(p[0][0]+(p[2][0]-p[0][0])*(r-p[0][1])/(p[2][1]-p[0][1])),round(p[1][0]+(p[2][0]-p[1][0])*(r-p[1][1])/(p[2][1]-p[1][1]))]]]for r in range(p[0][1],p[2][1])]for p in[sorted([[r-round(pogm.m[i+4*v+1]),round(pogm.m[i+4*v]),pogm.m[i+4*v+2],pogm.nilrecurring([[sum(uuu[ggg] for uuu in asdf)for ggg in(0,1,2)]for asdf in[[pogm.nermal(j)for j in range(0,len(pogm.m),12)if any(all(abs(pogm.m[j+4*k+pp]-pogm.m[i+v*4+pp])<0.0001 for pp in(0,1,2))for k in(0,1,2))]]][0]),((0,0),(0,200),(200,0))[v]]for v in(0,1,2)],key=lambda q:q[1])]]])
def fwreat(f,txt=None):
    with open(f,'w')as f:f.write(txt)
class Texture:
    def __init__(self,filename):
        [subprocess.Popen(("convert",'-compress','none',filename+"_"+t+".png",t+'.ppm'),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()for t in['a','d','s']]
        a,d,s=open('a.ppm','r'),open('d.ppm','r'),open('s.ppm','r')
        al,dl,sl=a.read().split("\n"),d.read().split("\n"),s.read().split("\n")
        self.r,self.c=[int(i)for i in al[1].split(' ')]
        ai,di,si=[int(i)/256 for i in' '.join(al[3:]).split(' ')if i],[int(i)/256 for i in' '.join(dl[3:]).split(' ')if i],[int(i)/256 for i in' '.join(sl[3:]).split(' ')if i]
        self.t=[[{e:[k[3*(j+self.c*i)+l]for l in(0,1,2)]for e,k in[['a',ai],['d',di],['s',si]]}for j in range(self.c)]for i in range(self.r)]
        a.close()
        d.close()
        s.close()
        [subprocess.Popen(("rm",t+'.ppm'),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()for t in['a','d','s']]
class Etrx:
    def __init__(self,m=[]):
        self.m,self.e,self.oof,self.x,self.idm,self.c,self.hb,self.t,self.bfc,self.nermal,self.dtp,self.crs,self.nilrecurring,self.collapsethelightintoearth,self.limelight=list(m),(lambda s,f:[self.m.append(i)for i in(*s,1,*f,1)]),(lambda:"\n".join(" ".join(("  "if i<10 else" "if i<100 else"")+str(i) for i in self.m[j::4]) for j in range(4))+"\n"),(lambda m:[self,[asg(self.m,e,i)for(i,e)in enumerate([sum(float(m[i%4+k*4])*self.m[i-(i%4)+k]for k in range(4))for i in range(len(self.m))])]][0]),(lambda:[[asg(self.m,1.0 if i==j else 0.0,j+4*i)for j in range(4)for i in range(4)]if self.m else[self.m.append(1.0 if i==j else 0.0)for j in range(4)for i in range(4)],self][1]),(lambda x,y,z,r:[[self.e(*[[x+r*math.cos((t+d)/mx*2*math.pi),y+r*math.sin((t+d)/mx*2*math.pi),z]for d in(0,1)])for t in range(round(mx))]for mx in[40]]),(lambda xyxy,m:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      [[self.e(*[[(lambda a,t:sum(pow(t,3-i)*a[i]for i in range(4)))(Etrx([xyxy[2*i+k]for i in range(4)]).x(m).m,(h+d)/mx)for k in(0,1)]+[0]for d in(0,1)])for h in range(mx)]for mx in[20]]),(lambda p,b,d:[self.m.append(i)for i in(float(p[0]),float(p[1]),float(p[2]),1,float(b[0]),float(b[1]),float(b[2]),1,float(d[0]),float(d[1]),float(d[2]),1)]),(lambda i,lk:self.dtp(lk,self.nermal(i))),(lambda i:self.crs(*[[self.m[i+j+k]-self.m[i+j]for j in(0,1,2)]for k in(4,8)])),(lambda m,pth:sum(m[i]*pth[i]for i in range(len(pth)))),(lambda p,vi:(p[1]*vi[2]-p[2]*vi[1],p[2]*vi[0]-p[0]*vi[2],p[0]*vi[1]-p[1]*vi[0])),(lambda x:[[i/f for i in x]for f in[math.sqrt(self.dtp(x,x))]][0]if self.dtp(x,x)else[0]*3),(lambda i,l,u:[[sum(e*pow(256,i)for i,e in enumerate([round(min(255,l[0][c]*u['a'][c]+sum([(u['d'][c]*max(0,self.dtp(z,Z))+u['s'][c]*pow(max(0,2*z[2]*self.dtp(Z,z)-Z[2]),4))*k['l'][c]for Z in[self.nilrecurring(k['v'])]][0]for k in l[1:])))for c in(2,1,0)]))for z in[self.nilrecurring(i)]][0]][-1]),(lambda u=[1,1,1]:sum(pow(256,i)*round(255*u[2-i])for i in(0,1,2)))


text=Texture("test")

def mesh(filename,pogm):
    with open(filename,"r")as f:[[pogm.t(*[v[int(i[k])-1] for k in(0,2,1)])+(pogm.t(*[v[int(i[k])-1]for k in(0,3,2)])if 3<len(i)else[])for i in[[int(q.split("/")[0])for q in l.split(" ")[1:]]for l in fs if"f "==l[:2]]for v in[[l.split(" ")[1:]for l in fs if"v "==l[:2]]]]for fs in[f.read().split("\n")]][0]
        
(lambda cs,edgm,pogm,terraformer,light,basename,filename:[[[[[[[{"push":(lambda:cs.append(Etrx(cs[-1].m))),"pop":(lambda:cs.pop()),"line":(lambda:[edgm.e([float(i)for i in b['args'][:3]],[float(i)for i in b['args'][3:]]),edgm.x(cs[-1].m),terraformer.lns(edgm.m,pogm.limelight()),edgm.m.clear()]),"circle":(lambda:[edgm.c(*[float(i)for i in b['args']]),edgm.x(cs[-1].m),terraformer.lns(edgm.m,pogm.limelight()),edgm.m.clear()]),"hermite":(lambda:[edgm.hb([float(i)for i in b['args']],(2,-3,0,1,-2,3,0,0,1,-2,1,0,1,-1,0,0)),edgm.x(cs[-1].m),terraformer.lns(edgm.m,pogm.limelight()),edgm.m.clear()]),"bezier":(lambda:[edgm.hb([float(i)for i in b['args']],(-1,3,-3,1,3,-6,3,0,-3,3,0,0,1,0,0,0)),edgm.x(cs[-1].m),terraformer.lns(edgm.m,pogm.limelight()),edgm.m.clear()]),"box":(lambda:[[pogm.t(*ooo)for ooo in[(((o[0],o[1],o[2]),(o[0],o[1]-o[4],o[2]),(o[0]+o[3],o[1],o[2])),((o[0],o[1]-o[4],o[2]),(o[0]+o[3],o[1]-o[4],o[2]),(o[0]+o[3],o[1],o[2])),((o[0],o[1],o[2]-o[5]),(o[0]+o[3],o[1],o[2]-o[5]),(o[0],o[1]-o[4],o[2]-o[5])),((o[0],o[1]-o[4],o[2]-o[5]),(o[0]+o[3],o[1],o[2]-o[5]),(o[0]+o[3],o[1]-o[4],o[2]-o[5])),((o[0]+o[3],o[1],o[2]),(o[0]+o[3],o[1]-o[4],o[2]),(o[0]+o[3],o[1],o[2]-o[5])),((o[0]+o[3],o[1]-o[4],o[2]),(o[0]+o[3],o[1]-o[4],o[2]-o[5]),(o[0]+o[3],o[1],o[2]-o[5])),((o[0],o[1],o[2]),(o[0],o[1],o[2]-o[5]),(o[0],o[1]-o[4],o[2])),((o[0],o[1]-o[4],o[2]),(o[0],o[1],o[2]-o[5]),(o[0],o[1]-o[4],o[2]-o[5])),((o[0],o[1],o[2]-o[5]),(o[0],o[1],o[2]),(o[0]+o[3],o[1],o[2]-o[5])),((o[0],o[1],o[2]),(o[0]+o[3],o[1],o[2]),(o[0]+o[3],o[1],o[2]-o[5])),((o[0],o[1]-o[4],o[2]-o[5]),(o[0]+o[3],o[1]-o[4],o[2]-o[5]),(o[0],o[1]-o[4],o[2])),((o[0],o[1]-o[4],o[2]),(o[0]+o[3],o[1]-o[4],o[2]-o[5]),(o[0]+o[3],o[1]-o[4],o[2])))for o in [[float(oo)for oo in b['args']]]][0]],pogm.x(cs[-1].m),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             terraformer.pgs(pogm,light,t=text,u=(k[1][b['constants']][1]if None!=b['constants']else{'a':[0.2,0.2,0.2],'d':[0.5,0.5,0.5],'s':[0.5,0.5,0.5]})),pogm.m.clear()]),"mesh":(lambda:[mesh(b['cs']+'.obj',pogm),pogm.x(cs[-1].m),terraformer.pgs(pogm,light,t=text,u=(k[1][b['constants']][1]if None!=b['constants']else{'a':[0.2,0.2,0.2],'d':[0.5,0.5,0.5],'s':[0.5,0.5,0.5]})),pogm.m.clear()]),"sphere":(lambda:[[[[(pogm.t(p[i],p[i+1],p[(i+k)%len(p)])if len([p[i],p[i+1],p[(i+k)%len(p)]])==len(set([p[i],p[i+1],p[(i+k)%len(p)]]))else 0,pogm.t(p[(i+1+k)%len(p)],p[(i+k)%len(p)],p[i+1])if len([p[(i+1+k)%len(p)],p[i+1],p[(i+k)%len(p)]])==len(set([p[(i+1+k)%len(p)],p[i+1],p[(i+k)%len(p)]]))else 0)for i in range(len(p))if i%k!=k-1]for p in[[(float(b['args'][0])+float(b['args'][3])*math.cos(math.pi*j/(k-1)),float(b['args'][1])+float(b['args'][3])*math.sin(math.pi*j/(k-1))*math.cos(2*math.pi*i/k),float(b['args'][2])+float(b['args'][3])*math.sin(math.pi*j/(k-1))*math.sin(2*math.pi*i/k))for i in range(k)for j in range(k)]]]for k in[16]],pogm.x(cs[-1].m),terraformer.pgs(pogm,light,k[1][b['constants']][1]if None!=b['constants']else{'a':[0.2,0.2,0.2],'d':[0.5,0.5,0.5],'s':[0.5,0.5,0.5]}),pogm.m.clear()]),"torus":(lambda:[[[[(pogm.t(p[i],p[(i+k)%len(p)],p[i-i%k+(i+1)%k]),pogm.t(p[(i+k)%len(p)],p[(i-i%k+(i+1)%k+k)%len(p)],p[i-i%k+(i+1)%k]))for i in range(len(p))]for p in[[(float(b['args'][0])+(float(b['args'][3])*math.cos(2*math.pi*i/k)+float(b['args'][4]))*math.cos(2*math.pi*j/k),float(b['args'][1])+float(b['args'][3])*math.sin(2*math.pi*i/k),float(b['args'][0])+(float(b['args'][3])*math.cos(2*math.pi*i/k)+float(b['args'][4]))*math.sin(2*math.pi*j/k))for i in range(k)for j in range(k)]]]for k in[20]],pogm.x(cs[-1].m),terraformer.pgs(pogm,light,k[1][b['constants']][1]if None!=b['constants']else{'a':[0.2,0.2,0.2],'d':[0.5,0.5,0.5],'s':[0.5,0.5,0.5]}),pogm.m.clear()]),"scale":(lambda:asg(cs,Etrx((float(b['args'][0])*knobtable[b['knob']][frame],0,0,0,0,float(b['args'][1])*knobtable[b['knob']][frame],0,0,0,0,float(b['args'][2])*knobtable[b['knob']][frame],0,0,0,0,1)).x(cs[-1].m),-1)),"move":(lambda:asg(cs,Etrx((1,0,0,0,0,1,0,0,0,0,1,0,float(b['args'][0])*knobtable[b['knob']][frame],float(b['args'][1])*knobtable[b['knob']][frame],float(b['args'][2])*knobtable[b['knob']][frame],1)).x(cs[-1].m),-1)),"rotate":(lambda:asg(cs,Etrx({"x":(1,0,0,0,0,math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),math.sin(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,0,math.sin(float(b['args'][1])/-180*math.pi*knobtable[b['knob']][frame]),math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,0,0,0,1),"y":(math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,math.sin(float(b['args'][1])/-180*math.pi*knobtable[b['knob']][frame]),0,0,1,0,0,math.sin(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,0,0,0,1),"z":(math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),math.sin(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,0,math.sin(float(b['args'][1])/-180*math.pi*knobtable[b['knob']][frame]),math.cos(float(b['args'][1])/180*math.pi*knobtable[b['knob']][frame]),0,0,0,0,1,0,0,0,0,1)}[b['args'][0]]).x(cs[-1].m),-1)),"display":(lambda:[open("temp.ppm","w+").write(terraformer.oof()),subprocess.Popen(("display","temp.ppm"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(),subprocess.Popen(("rm","temp.ppm"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()]),"save":(lambda:[open("temp2.ppm","w+").write(terraformer.oof()),subprocess.Popen(("convert","temp2.ppm",b['args'][0]),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(),subprocess.Popen(("rm","temp2.ppm"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()]),"clear":(lambda:[[asg(terraformer.img,0,i)for i in range(terraformer.r*terraformer.c)],[asg(terraformer.zbuf,float("-inf"),i)for i in range(terraformer.r*terraformer.c)]]),'constants':(lambda:0),'vary':(lambda:0),'basename':(lambda:asg(basename,b['args'][0])),'frames':(lambda:0)}[b['op']]()for b in k[0]],fwreat("anim/"+basename[0]+"%03d"%frame+".ppm",terraformer.oof()),[asg(terraformer.img,0,i)for i in range(terraformer.r*terraformer.c)],[asg(terraformer.zbuf,float("-inf"),i)for i in range(terraformer.r*terraformer.c)],cs.clear(),cs.append(Etrx().idm())]for frame in range([frames][0])]for knobtable in [(md({None:[1]*int(frames)},{q:[([1]+[ll['args'][2]+(ll['args'][3]-ll['args'][2])*(ll['args'][1]-frame)/(ll['args'][1]-ll['args'][0])for ll in k[0]if ll['op']=='vary'and ll['knob']==q and ll['args'][0]<=frame<=ll['args'][1]])[-1]for frame in range(frames)]for q in k[1].keys()if k[1][q][0]=="knob"}))]]for frames in[round(([1]+[r['args'][0]for r in k[0]if r['op']=='frames'])[-1])]]for k in[mdl.parseFile(filename)]],subprocess.Popen(("convert","-delay", "10", "anim/"+basename[0]+"*.ppm","orb.gif"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(),subprocess.Popen(("rm","anim/"+basename[0]+"*.ppm"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()])([Etrx().idm()],Etrx(),Etrx(),Img(500,500),[[50,50,50],{"l":[255,255,255],"v":(0.5,0.75,1)}],['this'],"face.mdl")
