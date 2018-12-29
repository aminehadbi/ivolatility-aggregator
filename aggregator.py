import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import csv

symbols = ["ABX", "AEM", "AGI", "AR", "ASR", "BTO", "CAS", "CCO", "CFP", "CG", "CHE.UN", "CNL", "DGC", "DPM", "EDR", "EDV", "ELD", "FM", "FNV", "FR", "FVI", "G", "GUY", "HBM", "IFP", "IMG", "IVN", "K", "KDX", "KL", "LAC", "LIF", "LUN", "MAG", "MDI", "MUX", "MX", "NG", "NGD", "NSU", "NTR", "OGC", "OR", "OSB", "OSK", "PAAS", "PG", "PVG", "RFP", "RUS", "SEA", "SJ", "SMF", "SSL", "SSRM", "SVM", "TECK.B", "THO", "TRQ", "TXG", "U", "UFS", "WFT", "WPM", "WTE", "BCE", "CCA", "QBR.B", "RCI.B", "SJR.B", "T", "ACQ", "ATZ", "CCL.B", "CGX", "CJR.B", "CTC.A", "DHX.B", "DOO", "GC", "GIL", "GOOS", "HBC", "ITP", "LNR", "MG", "MRE", "NFI", "QSR", "TCL.A", "TSGI", "UNS", "WPK", "WPRT", "ZZZ", "BCB", "DOL", "EMP.A", "JWEL", "L", "MFI", "MRU", "NWC", "PBH", "SAP", "SOY", "WN", "AAV", "ALA", "ARX", "BIR", "BNP", "BTE", "CEU", "CFW", "CJ", "CNQ", "CPG", "CR", "CVE", "ECA", "EFX", "ENB", "ENF", "ERF", "ESI", "FRU", "GEI", "GTE", "HSE", "IMO", "IPL", "KEL", "KEY", "KML", "MEG", "MTL", "NVA", "PD", "PEY", "PKI", "PONY", "POU", "PPL", "PSI", "PSK", "PXT", "RRX", "SCL", "SES", "SGY", "SPE", "SU", "TCW", "TOG", "TOU", "TRP", "VET", "VII", "WCP", "AD", "BMO", "BNS", "CF", "CIX", "CM", "CWB", "DC.A", "EFN", "GMP", "GS", "GWO", "HCG", "IAG", "IFC", "IGM", "LB", "MFC", "MIC", "NA", "ONEX", "POW", "PWF", "RY", "SLF", "TD", "TRI", "X", "ACB", "APH", "CSH.UN", "EXE", "GUD", "LEAF", "SIA", "VRX", "WEED", "AC", "AIM", "ARE", "ATA", "BAD", "BBD.B", "BLDP", "CAE", "CHR", "CNR", "CP", "ECI", "FTT", "RBA", "SNC", "STB", "STN", "TFII", "TIH", "WCN", "WJA", "WJX", "AAR.UN", "AIF", "BAM.A", "BPY.UN", "CAR.UN", "CIGI", "CRR.UN", "CUF.UN", "D.UN", "DIR.UN", "DRG.UN", "DRM", "FCR", "GRT.UN", "HR.UN", "NVU.UN", "NWH.UN", "REF.UN", "SRU.UN", "TCN", "BB", "CLS", "DSG", "ENGH", "GIB.A", "KXS", "MAXR", "MNW", "OTEX", "REAL", "SHOP", "SW", "AQN", "ATP", "BEP.UN", "BIP.UN", "BLX", "CPX", "CU", "EMA", "FTS", "H", "INE", "JE", "NPI", "RNW", "SPB", "TA", "XEG", "XFN", "XGD", "XIU", "XSP", "ZCN", "ZEB", "ZSP", "ZUT"]

reader = csv.reader(open('tmx.csv'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]

print(result["ABX"][0])

for symbol in symbols:
    print(symbol)
    print(result[symbol][0])
    if not os.path.exists(result[symbol][0]):
        os.makedirs(result[symbol][0])

    urllib.request.urlretrieve("https://www.ivolatility.com/nchart.j?charts=volatility,options_volume&1=ticker*"+symbol+":TSX,R*4,period*12,all*4,schema*options_big&2=ticker*G:TSX,R*4,period*12,schema*options_big_narrow&add=x:1", result[symbol][0]+"/"+symbol+".gif")
    response = urlopen("https://www.ivolatility.com/options.j?ticker="+symbol+"&R=4&x=19&y=3")
    page_source = response.read()
    soup = BeautifulSoup(page_source, 'lxml')
    tables = soup.findAll("table")
    print(len(tables))
    for table in tables:
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            print("!!!!!!!!!!!!!!!!!")
            for cell in cells:
                print(cell.text)
