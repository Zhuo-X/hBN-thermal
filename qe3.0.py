import codecs
import math
import os
i=0
f=[]
list1=[]
line=[]
l=0
w=0
k=0
j=0
x=[]
y=[]#第N列的数字
point=[]
a=[]
c=299792458#光速

########################################################################################
n=2
name= r'C:\Users\XZ\Desktop\热导率程序\0.5phonon\4\bn.'
change=0.005
v=21.766160669567377#体积
atom=8#原子数目
tem=300#温度
lattic=5.016681385
zhi=(12.0098385,12.1343845,12.2589305,12.3834765,12.5080225)
zhiliang=zhi[4]#12.0098385,12.1343845,12.2589305,12.3834765,12.5080225
rate=zhi.index(zhiliang)/4###B10占比
g2=(1-rate)*(1-11.009305/(10.012937*rate+(1-rate)*11.009305))**2+rate*(1-10.012937/(10.012937*rate+(1-rate)*11.009305))**2
#g2=((zhiliang/(14.00674+zhiliang))**2*g2+(14.00674/(14.00674+zhiliang))**2*0)*2
#if rate ==0 or rate ==1:
  #  g2=0
gap=0.02
high=25
high=float(high)
na=6.02214076*1e23#阿伏伽德罗常数
hb=1.0545726663e-34#约化普朗克常数
kb=1.380649e-23#波尔兹曼常数
v=float(v)
v=v*1e-20#单位转换成m^3
n=int(n)
lattic=float(lattic)
change=float(change)
zhiliang=float(zhiliang)
zhiliang=float(zhiliang/(na*1000))#单位换成千克
atom=float(atom)
tem=float(tem)
lattic=1e-10*lattic##埃转换成米
G=21.766160669567377*25*10**-30/(12*math.pi)*g2#21.766160669567377*10**-20/(8)*g2#3D 21.766160669567377*25*10**-30/(12*math.pi)*g2#3D文章2  (21.766160669567377*25*10**-30*KB**4*g2*tem**4)/(4*math.pi*HB**4)
path=name
path=name.split('\\')
path.pop()
path='\\'.join(path)+'\\'+'outdir'
if not os.path.exists(path):
    os.mkdir(path)


#####################################测试用赋值###############################################
'''print('使用前把声子输出文件命名为从0开始*******.n，n=0,1,2,3......')
name=str(input(r'文件的路径（把声子文件拖进来然后把后面的数字去掉）'+'\n'))'''
f0 = codecs.open('{}' '{}'.format(name,i), mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line0 = f0.readline()   # 以行的形式进行读取文件
list0 = []
f1 = codecs.open('{}' '{}'.format(name,i), mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
a0 = line0.split()
wide=len(a0)
while line0:
    a0 = line0.split()#把line转换成一个个的比如a=4  3  1  1 转换后就是a=['4','3','1','1']
    b0 = a0[0]   # 这是选取需要读取的位数
    list0.append(b0)  # 将其添加在列表之中
    line0 = f0.readline()


long=len(list0)
path=name
path=name.split('\\')
path.pop()
path='\\'.join(path)+'\\'+'outdir'
if not os.path.exists(path):
    os.mkdir(path)


####################################输入文件的长宽检测#################################################################
while j <wide:
    a.append('')
    j=j+1


i=-1
j=-1
k=-1
while i < n-1:#读取所有声子文件并且放入f[]中，然后读取所有文件的第一行放入line[]
    i=i+1#文件编号
    f=(codecs.open('{}' '{}'.format(name,i), mode='r', encoding='utf-8'))#读取i个文件存入f[]中
    while j < wide-1:
        j=j+1#行编号
        line=f1.readline() #把每一行存入line
        f=(codecs.open('{}' '{}'.format(name,i), mode='r', encoding='utf-8'))#重新读取进入下一列
        while k<long-1:
            k=k+1#列编号
            line=f.readline() #把每一行存入line
            a = line.split()
            gd=a[j]
            gd=float(gd)
            point.append(gd)
        k=-1
        y.append(point)
        point=[]#point初始化
    f.close()
    j=-1
    f=0#初始化f=[],进入下一个文件



f1.close()
f0.close()
###########################################################文件数据读取以列的形式存入y[]######################################

gd=[]
qunv=[]
answer=0
z=1
x=1
vb=0
while x <=n:
    while z < wide*x:
        while vb<long-1:
            jindu=0
            chusu=(y[z][vb+1]-y[z][vb])
            fenmu=(y[0][vb+1]-y[0][vb])/lattic
            answer=chusu/fenmu
            gd.append(answer)
            vb=vb+1
            answer=0
        qunv.append(gd)
        vb=0
        z=z+1
        gd=[]
    z=z+1
    x=x+1


###############################################计算群速度qunv单位m/s###################################################


gd=[]
tidu=[]
answer=0
j=0
i=0
while j < len(qunv):
    while i<len(qunv[0])-1:
        if qunv[j][i]!=0:
            answer=abs((qunv[j][i+1]-qunv[j][i])/qunv[j][i])
        else:
            answer=abs((qunv[j][i+1]-qunv[j][i])/qunv[j][i+1])
        gd.append(answer)
        i=i+1
        answer=0
    tidu.append(gd)
    i=0
    j=j+1
    gd=[]



###############################################计算梯度###################################################
i=0
j=0
k=0
while k <n:
    f=open(path+'\\'+'tidu'+str(k)+'.out','w')
    j=0 
    while j < len(tidu[0]):
        f.write(str(y[0][j]))
        f.write('   ')
        i=0
        while i<len(tidu)/n:
            a=tidu[int(len(tidu)/n*k+i)][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
        j=j+1
    k=k+1
    f.close()


##########################################输出梯度###############################################
i=0
j=0
k=0
a=0
nn=0
nm=0
while i <len(qunv)-1:
    a=int((i+1)/(len(qunv)/n))+1
    while j<len(qunv[0])-1:         
        if abs((qunv[i][j]-qunv[i][j+1])/(qunv[i][j]+10**-200)) >0.1 and j<len(qunv[0])-3 and j>5:#问题发生在y[x][j+1]上 j=7问题就在8
            cs=j+2#开始交换
            nn=nn+1
            k=int((a-1)*len(qunv)/n)
            if nn>=20:
                break
            lie = i#如果没检测到合适的交换就不换
            while k <a*len(qunv)/n:
                if abs(((y[i+a][j-1]-y[i+a][j+1])-(y[i+a][j]-y[k+a][j+2]))/(y[i+a][j]-y[i+a][j+1]+10**-200))<0.1 and abs((y[i+a][j]-y[k+a][j+3])/y[i+a][j+1])<0.1 :#and i<k
                    lie=int(k)#检测第几列交换
                    k=int(k+len(qunv))    
                    nm=nm+1       
                k=k+1
            j=j+2
            while j<len(qunv[0])-2:
                if abs((qunv[lie][j]-qunv[lie][j+2])/qunv[lie][j]) >0.1:
                    ce=j+3
                    j=j+len(qunv[0])
                    nm=0
                elif j >=len(qunv[0])-3:
                    ce=len(qunv[0])+1
                    j=j+len(qunv[0])
                    nm=0
                j=j+1
            j=-1
            gd=[]
            gd=y[i+a][cs:ce]
            y[i+a][cs:ce]=y[lie+a][cs:ce]
            y[lie+a][cs:ce]=gd
            gd=[]###交换之后重新算群速度
            qunv=[]
            answer=0
            z=1
            x=1
            vb=0
            while x <=n:
                while z < wide*x:
                    while vb<long-1:
                        jindu=0
                        chusu=(y[z][vb+1]-y[z][vb])
                        fenmu=(y[0][vb+1]-y[0][vb])/lattic
                        answer=chusu/fenmu
                        gd.append(answer)
                        vb=vb+1
                        answer=0
                    qunv.append(gd)
                    vb=0
                    z=z+1
                    gd=[]
                z=z+1
                x=x+1
        j=j+1
    i=i+1
    print(i/(len(qunv)-1))
    nn=0
    j=0





###########################################由群速度作为标准交换声子频率的位子#######################################i=0
j=-1
k=0
while k <n:
    f=open(path+'\\'+'bn.'+str(k)+'.','w')
    j=-1  
    while j < len(y[0])-1:
        j=j+1
        i=(wide)*k#
        while i<(k+1)*(wide):
            a=y[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


##########################################频率输出到frequency{n}.out#########################
i=0
j=-1
k=0
while k <n:
    f=open(path+'\\'+'qunv'+str(k)+'.out','w')
    j=-1   
    while j < len(qunv[0])-1:
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=(wide-1)*k#
        while i<(k+1)*(wide-1):
            a=qunv[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


##########################################群速度输出到qunv{n}.out单位m/s###############################################
guodu=[]
i=0
j=0
jian=[]
j=wide-1
delta=[]
gd=0
while j < len(y)-1:#J表示文件的列数
    delta.append(jian)
    j=j+1
    while i < long: 
        l=j%wide
        gd=round(y[l][i]-y[j][i],8) 
        jian.append(gd)#第m个文件和第1个文件的第n列相减
        i=i+1
    i=0
    jian=[]



################################第一个文件第一列和第二个文件第一列相减存入delta[]数量为len(y)-wide ########################

i=0
j=-1
k=0
while k <n-1:
    f=open(path+'\\'+'delta'+str(k)+'.out','w')
    j=-1   
    while j < len(delta[0])-1:###j从-1开始的
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=wide*k#
        i=i+1
        while i<(k+1)*wide:
            a=-delta[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()



##################################################输出delta到delta{n}.out单位为cm^-1############################
i=0
j=0
k=0
while i < len(y):
    if i%wide==0:
        i=i+1
    while j<len(y[0]):
        if y[i][j]==0:
            y[i][j]=y[i][j]+0.0000123
        y[i][j]=y[i][j]*c*100##单位转换从cm^-1到s^-1
        j=j+1
    i=i+1
    j=0


i=0
j=0
while i < len(delta):
    while j<len(delta[0]):
        delta[i][j]=delta[i][j]*c*100##单位转换从cm^-1到s^-1
        j=j+1
    i=i+1
    j=0


####################################避免计算gamma除数为0的情况并且把所有频率的单位转换成s^-1，gammg=0时提供热导为0######################################
i=0
ga=[]
gamma=[]
j=1
k=1
ga=[]
l=0
odu=0
while k<n:
    j=k*wide-wide+1#下一个文件的列在delta中的位子
    while j < wide*k:#wide*k
        while i<long:
            l=j%wide
            fenzi=delta[j][i]####delta中有负号了
            fenmu=2*y[l][i]*(change*k)
            answer=round(fenzi/fenmu,8)
            ga.append(answer)
            i=i+1
        j=j+1
        i=0
        gamma.append(ga)
        ga=[]
    k=k+1#进入下一个文件


##############################################gamma的计算储存到gamma[]中########################################
gammajun=[]
i=j=0
k=0
while i<wide-1:
    while j <len(gamma[0]):
        while k <n-1:
            gd=gamma[i+k*(wide-1)][j]+gd
            k=k+1
        guod=gd/(n-1)
        guodu.append(guod)
        guod=gd=k=0
        j=j+1
    j=0
    gammajun.append(guodu)
    guodu=[]
    i=i+1



############################################求gamma平均值###################################
i=0
j=-1
k=0
while k <n-1:
    f=open(path+'\\'+'gamma'+str(k)+'.out','w')
    j=-1   
    while j < len(gamma[0])-1:
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=(wide-1)*k#
        while i<(k+1)*(wide-1):
            a=gamma[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


###############################################以列的形式输出gamma{n}.out######################################

gd=[]
qunv=[]
answer=0
z=1
x=1
vb=0
while x <=n:
    while z < wide*x:
        while vb<long-1:
            jindu=0
            chusu=(y[z][vb+1]-y[z][vb])
            fenmu=(y[0][vb+1]-y[0][vb])/lattic
            answer=chusu/fenmu
            gd.append(answer)
            vb=vb+1
            answer=0
        qunv.append(gd)
        vb=0
        z=z+1
        gd=[]
    z=z+1
    x=x+1


###############################################计算群速度qunv单位m/s###################################################
i=0
j=-1
k=0
while k <n:
    f=open(path+'\\'+'qunv'+str(k)+'.out','w')
    j=-1   
    while j < len(qunv[0])-1:
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=(wide-1)*k#
        while i<(k+1)*(wide-1):
            a=qunv[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


##########################################群速度输出到qunv{n}.out单位m/s###############################################最后记得输出写到排序后面


i=0
qunvjun=[]####1/qunv**2
while i<len(qunv[0]):
    if qunv[1][i]!=0 and qunv[2][i]!=0:
        gd=(1/qunv[1][i])**2+(1/qunv[2][i])**2#(1/v0^3+1/v1^3+1/v2^3)
        gd=gd/2
        gd=math.sqrt(1/gd)
        qunvjun.append(gd)#1/v
        i=i+1
    else:
        gd=1
        qunvjun.append(gd)
        i=i+1


#############################################平均群速度单位m/s###########################################
debye=[]
i=0
j=0
guod=[]
while j < len(qunv):
    while i <len(qunv[0]):
        gd=2*abs(qunv[j][i])*math.sqrt(math.pi/(v*25*10**-10))
        guod.append(gd)
        i=i+1
    debye.append(guod)
    guod=[]
    j=j+1
    i=0




#############################################德拜频率单位s-1#######################################################
i=0
j=-1
k=0
while k <n:
    f=open(path+'\\'+'debye'+str(k)+'.out','w')
    j=-1   
    while j < len(debye[0])-1:
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=(wide-1)*k#
        while i<(k+1)*(wide-1):
            a=debye[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


########################################德拜频率输出到debye.out#################################
hb=1.0545726663e-34
kb=1.380649e-23
i=1
j=0
k=0
rerong=[]
guodu=[]
while k <n:
    i=wide*k+1
    while i<wide*(k+1):
        while j <len(y[0]):
            if y[i][j]==368744.72334:
                gd=1.3806489999823935e-23
            else :
                gd=(kb* (hb*y[i][j]/(kb*tem))**2)*math.exp(hb*y[i][j]/(kb*tem))/((math.exp(hb*y[i][j]/(kb*tem))-1)**2)
            guodu.append(gd)
            j=j+1
        rerong.append(guodu)
        guodu=[]
        j=0
        i=i+1
    k=k+1



########################################################热熔以列的形式存储##################################################
i=0
j=-1
k=0
while k <n:
    f=open(path+'\\'+'rerong'+str(k)+'.out','w')
    j=-1   
    while j < len(rerong[0])-1:
        j=j+1
        f.write(str(y[0][j]))
        f.write('   ')
        i=(wide-1)*k#
        while i<(k+1)*(wide-1):
            a=rerong[i][j]
            ga=str(a)
            f.write(ga)
            f.write('   ')
            i=i+1
        f.write('\n')    
    k=k+1
    f.close()


#################################################输出rerong{}.out#######################
i=0
j=0
guodu=[]
tao=[]
taoi=[]
while i < wide-1:
    while j<len(qunvjun):
        fenzi=debye[i][j]*zhiliang*abs(qunvjun[j])**2
        fenmu=(gammajun[i][j]**2)*(y[i+1][j]**2)*kb*tem
        if fenmu==0:##gamma=0时（原点出）热导率直接为0
            fenzi = 0    
        else:
            gd=fenzi/fenmu
        if gd==0:
            gd=10**-50
        gd=1/gd
        gd=abs(gd)
        A=G*(1/qunv[1][j]**3+2/qunv[2][j]**3)#*(2*math.pi)**4
        A=abs(A)
        taot=A*y[i][j+1]**4
        taoi.append(taot)
        gd=gd+taot
        gd=1/gd
        guodu.append(gd)
        j=j+1
    tao.append(guodu)
    guodu=[]
    i=i+1
    j=0






########################################################计算声子寿命#########################################
i=0
j=0
f=open(path+'\\'+'tao.out','w')
f.write('单位为s'+'\n')
while j<len(tao[0]):
    f.write(str(y[0][j]))
    f.write('   ')
    while i<len(tao):
        a=tao[i][j]
        ga=str(a)
        f.write(ga)
        f.write('   ')
        i=i+1
    i=0
    j=j+1
    f.write('\n')

f.close()
##########################################输出声子寿命################################

'''tao[1][0]=tao[1][1]
tao[2][0]=tao[2][1]'''
tao[1][0]=tao[2][0]=tao[0][0]=0
redao=0
i=0
j=0
ceshi=[]
guodu=[]
while i<3:#wide-1:
    while j <len(qunv[0]):
        gd=tao[i][j]*rerong[i][j]*(qunv[i][j]**2)*((y[0][i+1]-y[0][i])/lattic)**3/(high)/((2*math.pi)**3)*lattic*10**10
        if j==len(qunv[0])-1:
            gd=0
        guodu.append(gd)
        if qunv[i][j]>=20000:
            gd=0
        if gd >1000:
            gd=0
        redao=redao+gd
        j=j+1
    ceshi.append(guodu)
    guodu=[]
    j=0
    i=i+1

####################################################计算热导率#####################################

f=open(path+'\\'+'redao.out','w')
f.write(str(redao)+'\n')
i=0
j=0
while j<len(ceshi[0]):
    f.write(str(y[0][j]))
    f.write('   ')
    while i<len(ceshi):
        a=ceshi[i][j]
        ga=str(a)
        f.write(ga)
        f.write('   ')
        i=i+1
    i=0
    j=j+1
    f.write('\n')

f.close()

##########################################################单点热导率输出###############################
print('热导率为{}'.format(redao))
print('\n')
aaa=input('“按回车健关闭窗口,输出文件在该程序文件夹内”'+'\n')
