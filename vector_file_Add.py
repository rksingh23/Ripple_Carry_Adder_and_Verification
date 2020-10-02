import random
random.seed(14)

s="radix 4 4 4 4 4 4 4 4 1 \nio i i i i i i i i i\nvname A<[3:0]> A<[7:4]> A<[11:8]> A<[15:12]> B<[3:0]> B<[7:4]> B<[11:8]> B<[15:12]> Cin\ntunit ns\nslope 0.005\nvih 1.0\nvil 0.0\n"


f1=open("Add_golden.txt",mode='w')
f2=open("Vector_add_final.vec",mode='w')

f1.write("A(DEC)\t")
f1.write("B(DEC)\t")
f1.write("Cin(DEC)\t")
f1.write("SUM(DEC)\t")
f1.write("A(BIN)\t\t\t")
f1.write("B(BIN)\t\t\t")
f1.write("Cin(BIN)\t")
f1.write("SUM(BIN)\n")

f2.write(s)
f2.write("\n")
t=0

for i in range(0,10):
    a=random.randint(0,2**16)
    f1.write(f"{a}\t")
    b=random.randint(0,2**16)
    f1.write(f"{b}\t")
    cin=random.randint(0,1)
    f1.write(f"{cin}\t\t")
    c=a+b+cin
    f1.write(f"{c}\t\t")
    
    d=str(bin(a));
    fa=d.replace("0b", "");
    if(len(fa)<16):
        fa=(16-len(fa))*'0'+fa
    
    f1.write(f"{fa}")
    f1.write("\t")
    
    
    
    as1=(hex(int(fa[12:16], 2)).upper()).replace("0X","")
    as2=(hex(int(fa[8:12], 2)).upper()).replace("0X","")
    as3=(hex(int(fa[4:8], 2)).upper()).replace("0X","")
    as4=(hex(int(fa[0:4], 2)).upper()).replace("0X","")
    
    d=str(bin(b));
    fb=d.replace("0b", "");
    if(len(fb)<16):
        fb=(16-len(fb))*'0'+fb
    
    f1.write(f"{fb}")
    f1.write("\t")
    
    as1b=(hex(int(fb[12:16], 2)).upper()).replace("0X","")
    as2b=(hex(int(fb[8:12], 2)).upper()).replace("0X","")
    as3b=(hex(int(fb[4:8], 2)).upper()).replace("0X","")
    as4b=(hex(int(fb[0:4], 2)).upper()).replace("0X","")
    
    
    f1.write(f"{cin}")
    f1.write("\t\t")
    
    d=str(bin(c));
    fc=d.replace("0b", "");
    if(len(fc)<17):
        fc=(17-len(fc))*'0'+fc
    
    f1.write(f"{fc}")
    f1.write("\n")
    
    
    f2.write((f'{t} {as1} {as2} {as3} {as4} {as1b} {as2b} {as3b} {as4b} {cin}'))
    f2.write("\n")
    t+=5
f1.close()
f2.close()