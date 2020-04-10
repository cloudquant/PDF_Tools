import PyPDF2
import optparse
import sys
import os.path

def main():
        
    if len(sys.argv)<4:
        print("[+] Nombre arguments no valid")
        print("[+] Exemple us: python PDFCrypter.py -o nom_fitxer.pdf -p <password>")
    else:
        parser=optparse.OptionParser("usage%prog "+ "-o <OriginFile> -p <Password>")
        parser.add_option('-o', dest='originfile', type='string', help='Fitxer Origen')
        parser.add_option('-p', dest='password',type='string', help='Contrassenya')
        

        (options,args)=parser.parse_args()

        try:
        	pdf_file_handler=open(sys.argv[2],'rb')
        except IOError:
        	print("El fitxer original no existeix o el programa no l'ha pogut trobar")
        	exit(1)

        lector_PDF=PyPDF2.PdfFileReader(pdf_file_handler)

        escriptor_PDF=PyPDF2.PdfFileWriter()

        for number_of_pages in range(lector_PDF.numPages):
        	escriptor_PDF.addPage(lector_PDF.getPage(number_of_pages))

        escriptor_PDF.encrypt(options.password)
        try:
        	resultPdf=open('protected.pdf','wb')
        except IOError:
        	print("El fitxer de sortida no ha pogut ser creat")
        	exit(1)

        escriptor_PDF.write(resultPdf)
        resultPdf.close()
        pdf_file_handler.close()

if __name__=='__main__':

    main()
