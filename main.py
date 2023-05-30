# Distrito Federal (DF): 4  intervalos | JDP a JKR, OVM a OVV, OZW a PBZ, REC, a REV
# Goiás            (GO): 10 intervalos | KAV a KFC, NFC a NGZ, NJX a NLU, NVO a NWR, OGH a OHA, OMI a OOF, PQA a PRZ, QTN a QTS, RBK a RCN, SBW a SDS
# Minas Gerais     (MG): 12 intervalos | GKJ a HOK, NXX a NYG, OLO a OMH, OOV a ORC, OWH a OXK, PUA a PZZ, QMQ a QQZ, QUA a QUZ, QWR a QXZ, RFA a RGD, RMD a RNZ, RTA a RVZ
df = [["JDP", "JKR"], ["OVM", "OVV"], ["OZW", "PBZ"], ["REC", "REV"]]
go = [["KAV", "KFC"], ["NFC", "NGZ"], ["NJX", "NLU"], ["NVO", "NWR"], ["OGH", "OHA"], ["OMI", "OOF"], ["PQA", "PRZ"], ["QTN", "QTS"], ["RBK", "RCN"], ["SBW", "SDS"]]
mg = [["GKJ", "HOK"], ["NXX", "NYG"], ["OLO", "OMH"], ["OOV", "ORC"], ["OWH", "OXK"], ["PUA", "PZZ"], ["QMQ", "QQZ"], ["QUA", "QUZ"], ["QWR", "QXZ"], ["RFA", "RGD"], ["RMD", "RNZ"], ["RTA", "RVZ"]]

def findState(plate):
    if(isDF(plate[:3])):
        print("O veículo é do Distrito Federal.")
    elif(isGO(plate[:3])):
        print("O veículo é de Goiás.")
    elif(isMG(plate[:3])):
        print("O veículo é de Minas Gerais.")
    else:
        print("O veículo não é de nenhum dos estados de teste.")
        
def isDF(plate):
    for i in range(len(df)):
        if (plate >= df[i][0] and plate <= df[i][1]):
            return True       
def isGO(plate):
    for i in range(len(go)):
        if (plate >= go[i][0] and plate <= go[i][1]):
            return True
def isMG(plate):
    for i in range(len(mg)):
        if (plate >= mg[i][0] and plate <= mg[i][1]):
            return True
        
def plateAuth(plate):
    return (len(plate) == 7 and plate[:3].isalpha() and plate[3].isnumeric() and plate[4].isalpha() and plate[5:7].isnumeric())

plate = str(input("Insira uma Placa de Teste (Modelo Mercosul: LLL-NLNN)\n"))
while (not plateAuth(plate)):
    plate = str(input("Placa inválida. Insira uma Placa de Teste (Modelo Mercosul: LLL-NLNN)\n"))
findState(plate)