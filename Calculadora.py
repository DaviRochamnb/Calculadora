
class Numero():
    #Atributos
    valor = '0'
    base  = 10
    hexadecimal={ 0: '0',
                  1: '1',
                  2: '2',
                  3: '3',
                  4: '4',
                  5: '5',
                  6: '6',
                  7: '7',
                  8: '8',
                  9: '9',
                 10: 'A',
                 11: 'B',
                 12: 'C',
                 13: 'D',
                 14: 'E',
                 15: 'F'}
    
    #Métodos
    def get_valor (self):
        return self.valor
    
    def get_base (self):
        return self.base
    
    def set_valor (self, valor='0', base=10):
        self.valor = valor
        self.base  = base
    
    #Inicialmente será criado uma função para
    #converter o valor de qualquer base para
    #decimal.
    def converter_decimal(self):
        valor = list(self.valor)
        valor.reverse()
        hexadecimal = list(self.hexadecimal.items())
        hexadecimal = [hexa[1] for hexa in hexadecimal]
        #print(hexadecimal)
        valor = [hexadecimal.index(p) for p in valor]
        #print(valor)
        saida = 0
        for potencia in range(len(valor)):
            saida = (int(valor[potencia])*(self.base**potencia))+saida
        self.valor = str(saida)
        self.base  = 10
    
    def converter_base (self, base):
        self.converter_decimal()
        # Convertendo para uma base qualquer
        valor = int(self.valor)
        saida = ''
        while valor >= base:
            saida = (self.hexadecimal[valor % base]) +saida
            valor = valor // base
        saida = str(self.hexadecimal[valor]) + saida
        self.valor = saida
        self.base  = base
    
    def completar_zeros (self, qtd):
        self.valor = self.valor.zfill(qtd)

class Ip():
    #Atributos
    ip   = [Numero() for _ in range(4)]
    mask = [Numero() for _ in range(4)]
    rede = [Numero() for _ in range(4)]
    bcas = [Numero() for _ in range(4)]

    
    
    #Métodos
    def get_ip(self, base):
        ip = []
        for octeto in self.ip:
            valor = Numero()
            valor.set_valor(octeto.get_valor(), 2)
            valor.converter_base(base)
            if base == 2:
                valor.completar_zeros(8)
            elif base == 16:
                valor.completar_zeros(2)
            ip.append(valor.get_valor())
        return ip
    
    def get_mask(self, base):
        mask = []
        for octeto in self.mask:
            valor = Numero()
            valor.set_valor(octeto.get_valor(), 2)
            valor.converter_base(base)
            if base == 2:
                valor.completar_zeros(8)
            elif base == 16:
                valor.completar_zeros(2)
            mask.append(valor.get_valor())
        return mask
    
    def get_rede(self, base):
        rede = []
        for octeto in self.rede:
            valor = Numero()
            valor.set_valor(octeto.get_valor(), 2)
            valor.converter_base(base)
            if base == 2:
                valor.completar_zeros(8)
            elif base == 16:
                valor.completar_zeros(2)
            rede.append(valor.get_valor())
        return rede

    def get_bcast(self, base):
        bcas = []
        for octeto in self.bcas:
            valor = Numero()
            valor.set_valor(octeto.get_valor(), 2)
            valor.converter_base(base)
            if base == 2:
                valor.completar_zeros(8)
            elif base == 16:
                valor.completar_zeros(2)
            bcas.append(valor.get_valor())
        return bcas
    
    def get_qtd_hosts(self):
        total_hosts = 1
        for octeto in range(4):
            oct_rede = Numero()
            oct_rede.set_valor(self.rede[octeto].get_valor(), 2)
            oct_rede.converter_base(10)
            oct_rede = int(oct_rede.get_valor())
            oct_bcas = Numero()
            oct_bcas.set_valor(self.bcas[octeto].get_valor(), 2)
            oct_bcas.converter_base(10)
            oct_bcas = int(oct_bcas.get_valor())
            intervalo = oct_bcas - oct_rede
            if intervalo > 1:
                total_hosts *= (intervalo + 1)
        return total_hosts - 2
 
    def validar_octetos(self, lista_octetos, base):
        validar = True
        if len(lista_octetos) != 4:
            validar = False
        for str_octeto in lista_octetos:
            octeto = Numero()
            octeto.set_valor(str_octeto, base)
            octeto.converter_decimal()
            #print(str_octeto, base, validar)
            if int(octeto.get_valor()) > 255 or \
                int(octeto.get_valor()) < 0:
                validar = False
        return validar
    
    def validar_mask(self, mask, base):
        validar = True
        ultimovalor = False
        lista_valores = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        for str_octeto in mask:
            octeto = Numero()
            octeto.set_valor(str_octeto, base)
            octeto.converter_decimal()
            if ultimovalor and int(str_octeto) != 0:
                validar = False
            if int(str_octeto) != 255:
                ultimovalor = True
            if not (int(octeto.get_valor()) in lista_valores):
                validar = False
        return validar
    
    def set_ip(self, ip=[], base=10):
        if not self.validar_octetos(ip, base):
            print('IP incorreto!')
            return False
        else:
            self.ip = []
            for pos in range(4):
                self.ip.append(Numero())
                self.ip[-1].set_valor(ip[pos], base)
                self.ip[-1].converter_base(2)
                self.ip[-1].completar_zeros(8)
            return True
        
    def set_mask(self, mask=[], base=10):
        if not self.validar_mask(mask, base):
            print('Máscara incorreta!')
            return False
        else:
            self.mask = []
            for pos in range(4):
                self.mask.append(Numero())
                self.mask[-1].set_valor(mask[pos], base)
                self.mask[-1].converter_base(2)
                self.mask[-1].completar_zeros(8)
            return True
    
    def set_end_rede(self):
        self.rede = []
        for octeto in range(4):
            self.rede.append(Numero())
            binario = ''
            self.ip[octeto].converter_base(2)
            self.ip[octeto].completar_zeros(8)
            self.mask[octeto].converter_base(2)
            self.mask[octeto].completar_zeros(8)
            for pos in range(8):
                binario += str(int(bool(int(self.ip[octeto].get_valor()[pos])) and \
                                   bool(int(self.mask[octeto].get_valor()[pos]))))
            self.rede[-1].set_valor(binario, 2)
                
    def set_end_bcast(self):
        self.bcas = []
        for octeto in range(4):
            self.bcas.append(Numero())
            binario = ''
            self.ip[octeto].converter_base(2)
            self.ip[octeto].completar_zeros(8)
            self.mask[octeto].converter_base(2)
            self.mask[octeto].completar_zeros(8)
            for pos in range(8):
                binario += str(int(bool(int(self.ip[octeto].get_valor()[pos])) or \
                                    not(bool(int(self.mask[octeto].get_valor()[pos])))))
            self.bcas[-1].set_valor(binario, 2)    