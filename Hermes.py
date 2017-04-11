# -*- coding: iso-8859-1 -*-

############################################################################
# Funcions per tractar les trames del Hermes

# Ens formata la instruccio que nosaltres volguem enviar
# calculant el seu checksum.


def instruccio(cmd):
    chksum=0
    for c in cmd:
        chksum+=ord(c)
    chksum=chksum%256
    c="%(#)02x" % {"#": chksum}
    cmd="#"+c+";"+cmd+"\r"
    return cmd

# Funcio que reb la proxima trama

def rebre_instruccio(ser):
    c = ser.read()
    while c != '#':
          c = ser.read()
    
    inst = ''
    while c != '\r':
          inst += c
          c = ser.read()
    
    return inst

# Funcio per autentificar-se contra el Hermes

def autenticar(ser, passwd):
    try:
       ser.write(instruccio("55"+passwd))
    except:
       print "Error al enviar la comanda!"

    r = rebre_instruccio(ser)
    if r[4:] == "AA1":
       return True
    else:  
       return False

def numero_serie(ser):
    try:
       ser.write(instruccio('52'))
    except:
       print "Error al enviar la comanda!"
    
    r = rebre_instruccio(ser)
    return r[6:]
    
def firmware_version(ser):
    try:
       ser.write(instruccio('54'))
    except:
       print "Error al enviar la comanda!"
    
    r = rebre_instruccio(ser)
    return r[6:]
    
def num_registres(ser):
    try:
       ser.write(instruccio('5F'))
    except:
       print "Error al enviar la comanda!"
    
    r = rebre_instruccio(ser)
    num_regs = int("0x"+r[6:],16)-1
       
    return num_regs
    
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

# Funcio per generar una linia de text a partir de les dades del log

def linia_log(l_valors):
    txt_valors = ''
    for v in l_valors['valors']:
        txt_valors += "%(val)s\t" % {"val": v}
    
    linia="%(data)s\t%(hora)s\t%(valors)s" % \
          {"data": l_valors['data'], "hora": l_valors['hora'], "valors": txt_valors}
       
    return linia    
