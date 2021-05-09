def clear(a):
    for i in range(len(a)):
        a[i] = a[i].strip()
    return a
        
def toNumber(a):
    for i in range(len(a)):
        a[i] = eval(a[i])
    return a
        
def tinhdiem_trungbinh(score,rate):
    s=0
    for i in range(len(score)):
        s += score[i]* rate[i]
    return round(s,2)
def xeploaihocsinh(x,y,z):
        
    for i in range(len(x)):
        if z < x[i] :
            return y[i]
            break


class BANGDIEM:
    
    def __init__(self, duongdan_input, duongdan_output):
        self.duongdan_input = duongdan_input
        self.duongdan_output = duongdan_output
        
    def load_dulieu(self):
        self.f = open(self.duongdan_input)
        self.f.close()
        
    def tinhdiem_trungbinh(self): # phuong thuc load va xu ly data        
        
        
        tn = [0.05,0.1,0.15,0.7]
        xh = [0.05,0.1,0,1,0.15,0.6]

        dic = {}
        self.f = open(self.duongdan_input)
        header = self.f.readline()
        header = clear(header.split(';'))

        for line in self.f:
            a = clear( line.split(';'))
            
            dic[a[0]] = {}
            for i in range(1, len(a)):
                diem = toNumber(a[i].split(','))          
              
                if len(diem)== 4:
                    tb = tinhdiem_trungbinh(diem,tn)
        
                else:
        
                    tb = tinhdiem_trungbinh(diem,xh)

                dic[a[0]][header[i]] = tb

        #print(dic)

        return dic
        self.f.close()
    
    def print_dtb_dictionary(self):
        print(self.tinhdiem_trungbinh())
         
    def luudiem_trungbinh(self):
        self.f = open(self.duongdan_input)
        
        def clear(a):
            for i in range(len(a)):
                a[i] = a[i].strip()
            return a        
        
        header = self.f.readline()
        header = clear(header.split(';'))
        g = open(self.duongdan_output,'w')
        g.write(';\t'.join(header)+'\n')

        for k in self.tinhdiem_trungbinh():
            a = [k] + list((self.tinhdiem_trungbinh())[k].values())
    
   
            g.write(';\t'.join([str(v) for v in a]) + '\n')

        g.close()


class DANHGIA(BANGDIEM):
    def __init__(self, duongdan_input, duongdan_output,duongdan_danhgia):
        super().__init__(duongdan_input, duongdan_output)
        self.duongdan_danhgia = duongdan_danhgia
        
    def xeploai_hocsinh(self):
        

        dic_classification = {}
        
        for k in self.tinhdiem_trungbinh():
            a = [k] + list((self.tinhdiem_trungbinh())[k].values())
    
           
            dic_classification[a[0]] = {}
        
            
            dtb_chuan = ((a[1] +a[5] + a[6])*2 + (a[2]+a[3]+a[4]+a[7]+a[8])*1)/11
            dtb_chuan = round(dtb_chuan,2)
            
            
            list_xl =[]
            x= [6,6.5,8,9,10]
            y = ['Tb','Tb Kha','Kha','Gioi','Xs']

            list_xl = xeploaihocsinh(x,y,dtb_chuan)
              
            dic_classification[a[0]] = list_xl

        print(dic_classification)
        return dic_classification

    def xeploai_thidaihoc_hocsinh(self):

        dic_rank = {}
        
        for k in self.tinhdiem_trungbinh():
            a = [k] + list((self.tinhdiem_trungbinh())[k].values())    
           
            dic_rank[a[0]] = {}
            diem_kA  = a[1] + a[2] + a[3]
            diem_kA1 = a[1] + a[2] + a[6]
            diem_kB  = a[1] + a[3] + a[4]
            list_ktn =[diem_kA, diem_kA1,diem_kB]
            diem_kC  = a[5] + a[7] + a[8]
            diem_kD  = a[1] + a[5] + 2*a[6]
            list_rank = []
            tn= [12,18,24,40]
            c= [12,15,21,40]
            d= [20,24,32,40]
            loai = [4,3,2,1]
            
            for i in list_ktn:
                list_ktn = xeploaihocsinh(tn,loai,i)
                list_rank.append(list_ktn)
            listkC =xeploaihocsinh(c,loai,diem_kC)
            list_rank.append(listkC)
            listkD =xeploaihocsinh(d,loai,diem_kD)
            list_rank.append(listkD)            

            dic_rank[a[0]] = list_rank
            
        
        
        
        return (dic_rank)
    def print_screen_xeploaidh(self):
        print('XEP LOAI THI DAI HOC: ',self.xeploai_thidaihoc_hocsinh())
                                
    
    def luu_danhgia_hs(self):
        
        h = open(self.duongdan_danhgia,'w')
        
        h.write('“Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, "xeploai_D” \n')

        for k in self.xeploai_thidaihoc_hocsinh():
     
            a = (self.xeploai_thidaihoc_hocsinh())[k]
            h.write(k + "; " + self.xeploai_hocsinh()[k] + ' ; '+ '; '.join([str(v) for v in a]) + '\n')
            

        h.close()
        

 
class TUNHIEN(DANHGIA):
    def __init__(self, duongdan_input, duongdan_output,duongdan_danhgia):
        super().__init__(duongdan_input, duongdan_output,duongdan_danhgia)
        
    def danhgia_khoitunhien(self):
        danhgia_khoitunhien=self.xeploai_thidaihoc_hocsinh()
        dic_tunhien = {}
        for k in self.xeploai_thidaihoc_hocsinh():
            value =self.xeploai_thidaihoc_hocsinh()[k]
            value = value[0:3]           
            dic_tunhien[k] = value
        print('Xep loai khoi TUNHIEN: ',dic_tunhien)   
        return dic_tunhien
        
class XAHOI(DANHGIA):
    def __init__(self, duongdan_input, duongdan_output,duongdan_danhgia):
        super().__init__(duongdan_input, duongdan_output,duongdan_danhgia)

    def danhgia_khoixahoi(self):
        danhgia_khoixahoi=self.xeploai_thidaihoc_hocsinh()
        dic_xahoi = {}
        for k in self.xeploai_thidaihoc_hocsinh():
            value =self.xeploai_thidaihoc_hocsinh()[k]
            value = value[3]           
            dic_xahoi[k] = value
        print('Xep loai khoi XAHOI: ',dic_xahoi)     
        return dic_xahoi          
##
        
class COBAN(DANHGIA):
    def __init__(self, duongdan_input, duongdan_output,duongdan_danhgia):
        super().__init__(duongdan_input, duongdan_output,duongdan_danhgia)
        
    def danhgia_khoicoban(self):
        danhgia_khoicoban=self.xeploai_thidaihoc_hocsinh()
        dic_coban = {}
        for k in self.xeploai_thidaihoc_hocsinh():
            value =self.xeploai_thidaihoc_hocsinh()[k]
            value = value[4]           
            dic_coban[k] = value
        print('Xep loai khoi COBAN: ',dic_coban)     
        return dic_coban


if __name__ == '__main__':
    
    bangdiem = BANGDIEM("diemchitiet_OOP.txt", "diem_trungbinh_OOP.txt")
    bangdiem.tinhdiem_trungbinh()
    bangdiem.print_dtb_dictionary()

    danhgia = DANHGIA("diemchitiet_OOP.txt", "diem_trungbinh_OOP.txt", "danhgiahocsinh_OOP.txt")
    danhgia.xeploai_hocsinh()
    danhgia.xeploai_thidaihoc_hocsinh()
    #danhgia.luu_danhgia_hs()
    danhgia.print_screen_xeploaidh()

    TUNHIEN = TUNHIEN("diemchitiet_OOP.txt", "diem_trungbinh_OOP.txt", "danhgiahocsinh_OOP.txt")
    TUNHIEN.danhgia_khoitunhien()

    XAHOI = XAHOI("diemchitiet_OOP.txt", "diem_trungbinh_OOP.txt", "danhgiahocsinh_OOP.txt")
    XAHOI.danhgia_khoixahoi()

    COBAN = COBAN("diemchitiet_OOP.txt", "diem_trungbinh_OOP.txt", "danhgiahocsinh_OOP.txt")
    COBAN.danhgia_khoicoban()


