import PyPDF2
import optparse
import sys
import os.path

def main():
        
    if len(sys.argv)<4:
        print("[+] Nombre arguments no valid")
        print("[+] Exemple us: python PDF_DeCrypter.py -o nom_fitxer.pdf -f <passwords file>")
    else:
        parser=optparse.OptionParser("usage%prog "+ "-o <OriginFile> -f <Passwords File>")
        parser.add_option('-o', dest='originfile', type='string', help='Fitxer Origen')
        parser.add_option('-f', dest='passwordsfile',type='string', help='Fitxer amb contrassenyes')
        

        (options,args)=parser.parse_args()

        try:
        	pdf_file_handler=open(options.originfile,'rb')
        except IOError:
        	print("El fitxer original no existeix o el programa no l'ha pogut trobar")
        	exit(1)
        try:
            pwd_file_handler=open(options.passwordsfile,'r')
        except IOError:
            print("El fitxer amb les contrassenyes no existeix o el programa no l'ha pogut trobar")
            exit(1)

        lector_PDF=PyPDF2.PdfFileReader(pdf_file_handler)

        if lector_PDF.isEncrypted:
            print(" Iniciant procès per a trobar el password. Esperi, si us plau...")
            for password in pwd_file_handler:
                if lector_PDF.decrypt(password.strip())==1:
                    print("[+] Fitxer xifrat amb el password: "+password.strip())
                    pdf_file_handler.close()
                    pwd_file_handler.close()
                    exit(1)
        print("Ho sento. El password no s'ha trobat al fitxer de contrassenyes. Estic desolat.")
        pdf_file_handler.close()
        pwd_file_handler.close()
       
if __name__=='__main__':

    main()