# Ens formata la instruccio que nosaltres volguem enviar
# calculant el seu checksum.

def instruccio(cmd):
    chksum=0
    for c in cmd:
        chksum+=ord(c)
    chksum=chksum%256
    c="%(#)02X" % {"#": chksum}
    cmd="#"+c+";"+cmd+"\r"
    return cmd

# Funcio que reb la proxima trama
def rebre_instruccio(ser):
    c = ser.read()
    while c != '#':
          c = ser.read()
    
    inst = ''
    chk = ''
    chksum = 0
    while c != '\r':
	      # Calculam el checksum de la trama
          if chk != '':
             chksum+=ord(c)

          # Llegim el checksum de la propia trama rebuda
          if c == ';':
             chk = inst[1:3]
	  
          inst += c
          c = ser.read()
    
    # Comprovam que el checksum que hem rebut i el que hem
    # calculat són iguals!
    c_chksum = chksum % 256
    r_chksum = int("0x"+chk,16)   
    
    if c_chksum != r_chksum:
       print inst,"  [CHECKSUM_ERROR]"  
       return
     
    #print "Rebuda instruccio => ",inst, " amb el checksum ",chk," %(#)02x" % {"#": chksum}
    return inst

# Funcio per autentificar-se contra el Hermes

def autenticar(ser, passwd):
    try:
       ser.write(instruccio(ASK_PASSWD+passwd))
    except:
       print "Error al enviar la comanda!"
       return False
    else:
       r = rebre_instruccio(ser)
       if r[4:] == "AA1":
          return True
       else:  
          return False

def numero_serie(ser):
    try:
       ser.write(instruccio(ASK_NSERIE))
    except:
       print "Error al enviar la comanda!"
    
    r = rebre_instruccio(ser)
    return r[6:]
    
def firmware_version(ser):
    try:
       ser.write(instruccio(ASK_VFIRMW))
    except:
       print "Error al enviar la comanda!"
    
    r = rebre_instruccio(ser)
    return r[6:]
    
def num_registres(ser):
    try:
       ser.write(instruccio(ASK_NREGSD))
    except:
       print "Error al enviar la comanda!"
       return
       
    r = rebre_instruccio(ser)
    if r[4:6] == 'A0':
       num_regs = int("0x"+r[6:],16)-1
    else:
       num_regs = -1
       
    return num_regs

def demana_data(ser):
    try:
       ser.write(instruccio(ASK_DATEHO))
    except:
       print "Error al enviar la comanda!"
       return
    
    r = rebre_instruccio(ser)
    if r[4:6] == 'A2':
       d_any = r[6:8]
       d_mes = r[8:10]
       d_dia = r[10:12]
       retval = "%(dia)s/%(mes)s/%(any)s" % {"dia": d_dia, "mes": d_mes, "any": d_any}  
    else:
       retval = ""

    return retval
    
def adjustar_data(ser, data_hora):
    try:
       ser.write(instruccio(ADJ_DATEHO+data_hora))
    except:
       print "Error al enviar la comanda!"
       return
    
    r = rebre_instruccio(ser)
    
    
# Ens interpreta la resposta de la peticio de baixar-se les dades del
# datalogger.

def interpreta_log(inst):
    txt_valors=''
    valors = inst[27:]
    
    ret_vals = {}
    ret_vals["data"] = "%(dia)s/%(mes)s/%(any)s" % {"dia": inst[18:20], "mes": inst[16:18], "any": inst[14:16]}
    ret_vals["hora"] = "%(hora)s:%(min)s:%(seg)s" % {"hora": inst[20:22], "min": inst[22:24], "seg": inst[24:26]}
    ret_vals["valors"] = []
    
    for v in valors.split(';'):
        ret_vals['valors'].append("%(val)s" % {"val": v[1:]})
    
    return ret_vals

# Funció per generar una linia de text a partir de les dades del log

def linia_log(l_valors):
    txt_valors = ''
    for v in l_valors['valors']:
        txt_valors += "%(val)s\t" % {"val": v}
    
    linia="%(data)s\t%(hora)s\t%(valors)s" % \
          {"data": l_valors['data'], "hora": l_valors['hora'], "valors": txt_valors}
       
    return linia    
