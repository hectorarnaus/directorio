from ftplib import FTP
import io

def imprimir_htaccess(ftp_host, ftp_user, ftp_pass, ruta_remota='.htaccess'):
    try:
        # Conectarse al servidor FTP
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        print(f"✅ Conectado a {ftp_host}")

        # Usar buffer en memoria para capturar el contenido
        buffer = io.BytesIO()
        ftp.retrbinary(f'RETR {ruta_remota}', buffer.write)

        # Mostrar el contenido
        buffer.seek(0)
        contenido = buffer.read().decode('utf-8')
        print("\n📄 Contenido del archivo .htaccess:\n")
        print(contenido)

        ftp.quit()

    except Exception as e:
        print(f"❌ Error al descargar o leer .htaccess: {e}")


imprimir_htaccess(
    ftp_host='156.67.73.254',
    ftp_user='u676378269.hector',
    ftp_pass='bolo9o,Eresgay#Caca',
    ruta_remota='.htaccess'
)
