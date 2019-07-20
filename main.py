



def run(log_path):

    from apache import ApacheLog

    from pdf_type1 import PDFType1

    apache_file=ApacheLog(log_path)

    #apache_file.load()

    results=apache_file.run_analisis()

    pdf=PDFType1("Analisis.pdf",rightMargin=72,leftMargin=72, topMargin=72,bottomMargin=18)

    pdf.build_custom(results)

if __name__=="__main__":
    #aqui va un input (archivo log y la salida del pdf(si se deja vacio en la misma carpeta))
    run("fcb")