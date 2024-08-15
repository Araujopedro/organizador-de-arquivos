import os
from  tkinter.filedialog import askdirectory

caminho = askdirectory(title="escolha uma pasta")


list_arq= os.listdir(caminho)
print(list_arq)

local= {
    "excel": [".Xlsx"] , 
    "pdf" : [".pdf"], 
    "cvs" : [ ".csv"]
    
}


for arquivo in list_arq:
    nome , extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in local:
        if extensao in local[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")



