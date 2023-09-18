import pandas as pd
from tabulate import tabulate
from colorama import Fore, Back, Style


letras = {'A':1000543,'B':1000542,'C':1000532,'D':1000525,'E':1000526,'F':1000527,'G':1000528,'H':1000529,
          'I':1000530,'J':1000531,'K':1000533,'L':1000541,'M':1000534,'N':1000535,'O':1000536,'P':1001185,
          'Q':1001186,'R':1001187,'S':1001188,'T':1001189,'U':1001190,'V':1001191,'W':1001192,'X':1001193,
          'Y':1001194,'Z':1001195,'1':1001196,'2':1001197,'3':1000970,'4':1001262,'5':1000968,'6':1000784,
          '7':1000670,'8':1000682,'9':1000784,'0':1000536,'/':'N/A','*':'N/A','-':'N/A','+':'N/A','.':'N/A',
          '_':'N/A','(':'N/A',')':'N/A','=':'N/A','^':'N/A','&':'N/A','%':'N/A','$':'N/A','#':'N/A','@':'N/A',
          '~':'N/A','|':'N/A','<':'N/A','>':'N/A',',':'N/A','?':'N/A',';':'N/A',':':'N/A',' ':'N/A','\\':'N/A',
          '{':'N/A','}':'N/A','?':'N/A'}

print('********->CALCULAR LETRAS<-********')
while True:
    valor = input("\nColocar datos: ").upper()
    try:
        letra = []
        cantidad = []
        codigo = []
        conteo = dict.fromkeys(valor, 0)

        for caracter in valor:
            conteo[caracter] += 1
        for le, nu in conteo.items():
            cantidad.append(nu)
            letra.append(le.upper())
            codigo.append(letras[le])
            #print('{}: {}'.format(le,nu))

            
        df=pd.DataFrame({"LETRA":letra, "CODIGO":codigo, "CANTIDAD":cantidad})
        headers = ["ID", "LETRA", "CODIGO", "CANTIDAD"]

        filtro = df['CODIGO'] != 'N/A'
        filtro_df = df[filtro]
        print(tabulate(filtro_df, headers, tablefmt="grid"))
        filtro_df.to_excel('compiladoLetra.xlsx', sheet_name='Letra')
        #input()
        

    except:
      print("\nAlgo salio mal!")
    if valor == 0:
        break
