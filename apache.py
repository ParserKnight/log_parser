



class ApacheLog():

    def __init__(self, file_path=None, output_file=None):

        self.log_path=file_path
        self.pdf_path=output_file

    def load(self):

        #with open(self.log_path, "r") as file:

        results=self.run_analisis()

        return results

    def run_analisis(self,file=None):

        #for line in file:

        #aqui se parsea cada linea del archivo

        #se genera una lista de diccionarios con los datos de cada linea
        # [ {ip,fecha,ubicacion}]

        return [{"ip":"10.10.10.10","ubicacion":"la bolita el mundo", "fecha":"20/10/1972"}]
        #se hace un return de esta lista

        
        

