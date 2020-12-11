from openpyxl import load_workbook
from .models import Localidades,Empresas,Equipo
import sys

def handle_uploaded_file(f):
    wb = load_workbook(filename = f)    
    print(wb.sheetnames)
    ws = wb['Hoja1']
    for row in ws.iter_rows(min_row=2, max_col=17):
        
        q = Localidades(nombre=row[7].value)
        try:            
            q.save()
        except:
            print("localidad creada 1")
        
        q = Localidades(nombre=row[8].value)
        try:            
            q.save()
        except:
            print("localidad creada 2")        
        
        q = Empresas(nombre=row[16].value)
        try:            
            q.save()
        except:
            print("Empresa creada")        

        try: 
            id_loc1 = Localidades.objects.filter(nombre=row[7].value)[0]
            id_loc2 = Localidades.objects.filter(nombre=row[8].value)[0]
            empresa1 = Empresas.objects.filter(nombre=row[16].value)[0]
            
            q = Equipo(codm=row[0].value,nro_lote=int(row[1].value),observaciones=row[2].value,nro_tarea=int(row[3].value),nro_cuenta=int(row[4].value),nya_cliente=row[5].value or "",domicilio=row[6].value,localidad_contable=id_loc1,localidad_retiro=id_loc2,codigo_postal=row[9].value,tel1 = row[10].value or "",tel2 = row[11].value or "",tel3 = row[12].value or "",tel4 = row[13].value or "",email = row[14].value or "",base_nro_serie = row[15].value,empresa = empresa1,recuperado = False)
            q.save()
        except:
           print("Error?")

        print("----------------------------------------------------------------")
    
    

    
#handle_uploaded_file("/media/anarko/1tero/src/mios/logistica/xls/GESTION_DE_LLAMADAS_BASE_58709_AL_28-11.xlsx")