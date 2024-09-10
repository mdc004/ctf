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
- Ports Scanning:
  - nmap
  - rustscan
- traceroute
- ping
- netcat
- telnet
- ssh
- metasploit
- nessus
- Spyse
- OpenVAS
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
