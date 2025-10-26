"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import pandas as pd
    import re

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
      lines = f.readlines()

    #Quitar encabezado y líneas vacias
    lines = lines[4:] 
    lines = [line for line in lines if line.strip() != ""]

    
    data = []
    current = ""

    for line in lines:
      if re.match(r"^\s*\d+", line): # Si la línea comienza con un número, inicia otro cluster
        if current:
          data.append(current.strip())
        current = line
      else:
        current += " " + line  #Si no inicia con número, añade línea al cluster 
  
    if current: # Encuentro nuevo cluster pero ya current ya tiene texto > añado el cluster 
      data.append(current.strip()) #cada cluster es un string en la lista data


    rows = []
    for cluster in data:
      match = re.match(r"\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)", cluster, re.DOTALL)
      #match = re.match(r"\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)", cluster)
      if match:
        n_cluster = int(match.group(1))
        cantidad = int(match.group(2))
        porcentaje = float(match.group(3).replace(",", "."))
        palabras = re.sub(r"\s+", " ", match.group(4)).strip().rstrip(".;,")
        rows.append((n_cluster, cantidad, porcentaje, palabras))
   
    df = pd.DataFrame(rows, columns=[
      "cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"
    ])
    return df 

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """


df_rev= pregunta_01()
print(df_rev)
#print(df_rev["principales_palabras_clave"].iloc[0])
print(df_rev.loc[2]["principales_palabras_clave"])