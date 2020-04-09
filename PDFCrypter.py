import PyPDF2
import optparse
import sys
import os.path

def main():
        
    if len(sys.argv)<4:
        print("[+] Numero de argumentos no valido")
        print("[+] Ejemplo de uso: python PDFCrypter.py -o C:\\Carlos\\texto1.pdf -p <password>")
    else:
        parser=optparse.OptionParser("usage%prog "+ "-o <OriginFile> -p <Password>")
        parser.add_option('-o', dest='originfile', type='string', help='Fitxer Origen')
        parser.add_option('-p', dest='password',type='string', help='Contrassenya')
        #parser.add_option('-a', dest='action', type='string', help='Especificar tipus de tractament' )

        (options,args)=parser.parse_args()

        try:
        	pdf_fh=open(sys.argv[2],'rb')
        except IOError:
        	print("El fitxer original no existeix o el programa no l'ha pogut trobar")
        	exit(1)
        pdfReader=PyPDF2.PdfFileReader(pdf_fh)

        pdfWriter=PyPDF2.PdfFileWriter()

        for pageNum in range(pdfReader.numPages):
        	pdfWriter.addPage(pdfReader.getPage(pageNum))

        pdfWriter.encrypt(options.password)
        try:
        	resultPdf=open('protected.pdf','wb')
        except IOError:
        	print("El fitxer de sortida no ha pogut ser creat")
        	exit(1)

        pdfWriter.write(resultPdf)
        resultPdf.close()
        pdf_fh.close()

if __name__=='__main__':

    main()
