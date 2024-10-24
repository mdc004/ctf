# Crypto
Il principale strumento da utilizzare in questo tipo di challenge è Python!!!!!

> Brutto scemo usa chat gpt, ci metti la metà del tempo

> Molte volte la flag non è propriamente cifrata ma semplicemente rappresentata in un encoding diverso tipo `base64` e altre cose simili, usare *Python* oppure usare [CyberChef](https://cyberchef.org/).

Bitwise significa operazioni a livello di bit

- [dcode](https://www.dcode.fr/en): sito che continene una valanga di cifrari e diverse soluzioni per decodificare per partial key, partial plaintext...
- **Cifrario di cesare**: comando `caesar`, scaricabile con `sudo apt install bsdgames` or `tr` for example: `tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt` for a 13 key
- `ord(char)` tipicamente usato per il cifrario di cesare o in generale quando devi traslare le cifre
- moduli ecc. guardare taccuino mate del discreto
- [RSA](#RSA):
  - [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)
    ```bash
    git clone https://github.com/RsaCtfTool/RsaCtfTool
    cd RsaCtfTool
    pip install -r requirements.txt
    ```

    `python RsaCtfTool.py -n <n_value> -e <e_value> --decrypt <cipher_text>`

  - Rsa Decrypt
- xor *risultato sarà uguale a **1** se i due numeri non saranno uguali*. Le sue proprietà sono quella commutativa e date due variabili binarie *x* e *y* : `x ⊕ y ⊕ y = x`.
  --> One Time Pad (OTP) 
  - [Crack OTP with MTP (*python module*)](https://github.com/CameronLonsdale/MTP) (*su kali non sembra andare, parrot ok*)
  - [`xortool`](https://github.com/hellman/xortool)
  - [CyberChef](https://cyberchef.org/)
  - Python
    ```Python
    def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])
    ```
    Se non va applicare all'input: `bytes.fromhex(a)`
  - Sequenza non può, però essere utilizzata per più di una volta, difatti una volta esaurita sarà necessario generarne un'altra, pena attacchi di tipo [crib-drag](#crib-drag).
- `b64decode`
  - comando shell: `cat flag_file_encoded | base64 --decode`
  - libreria di python:
    ```Python
    from base64 import b64decode
    print(b64decode('aGVubG8gOik='))
    ```
- `int.to_bytes(length=1, byteorder='big', *, signed=False)` Return an array of bytes representing an integer.

  Il campo `length` è sempre meglio metterlo ad un numero alto tipo $256$, tanto i dati che ci interessano sono rappresentati alla fine.
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/index.html)
  [Documento Introduttivo](https://training.olicyber.it/api/file/13563f96-8ffa-4a10-a60b-b2d1aa6f53a9/pycryptodome_basics.pdf)
  ```Python
  from Crypto.Cipher import DES
  from Crypto.Util.Padding import pad
  from Crypto.Random import get_random_bytes
  
  '''
  Cipher = DES
  Mode of operation = CBC
  key.hex() = '073b15e07531c240'
  plaintext = 'La lunghezza di questa frase non è divisibile per 8'
  Padding scheme = x923
  '''
  
  key = bytes.fromhex('073b15e07531c240')
  
  iv = get_random_bytes(8)
  
  cipher = DES.new(key, DES.MODE_CBC, iv)
  
  plaintext = 'La lunghezza di questa frase non è divisibile per 8'.encode('utf-8')
  
  padded_text = pad(plaintext, DES.block_size, style='x923')
  
  ciphertext = cipher.encrypt(padded_text)
  
  final_ciphertext = ciphertext
  
  print(f"IV (esadecimale): {iv.hex()}")
  print(final_ciphertext.hex())
  ```
  ```Python
  from Crypto.Cipher import AES
  from Crypto.Util.Padding import pad
  from Crypto.Random import get_random_bytes
  
  '''
  Cipher = AES256
  Mode of operation = CFB
  plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
  Padding scheme = pkcs7 (block size = 16)
  Segment size = 24
  '''
  
  key = get_random_bytes(32)

  iv = get_random_bytes(16)

  segment_size = 24

  cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=segment_size)

  plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'.encode('utf-8')

  padded_text = pad(plaintext, AES.block_size, style='pkcs7')

  ciphertext = cipher.encrypt(padded_text)

  print(f"Chiave (esadecimale): {key.hex()}")
  print(f"IV (esadecimale): {iv.hex()}")
  print(f"Testo cifrato (esadecimale): {ciphertext.hex()}")
  ```
  ```Python
  from Crypto.Cipher import ChaCha20
  
  '''
  Cipher = ChaCha20
  key.hex() = 'fc47efc894be23567bc1937c3bf25841822560a2fabfb33c1fce679f8167c080'
  ciphertext.hex() = '1c4cde7013a806a3c25129d8b3be3d7f441c3396c77abdeb4268bc04'
  Nonce = cipher.nonce.hex() = '08af973d24bab25a'
  '''
  
  key = bytes.fromhex('fc47efc894be23567bc1937c3bf25841822560a2fabfb33c1fce679f8167c080')
  nonce = bytes.fromhex('08af973d24bab25a')
  ciphertext = bytes.fromhex('1c4cde7013a806a3c25129d8b3be3d7f441c3396c77abdeb4268bc04')
  
  cipher = ChaCha20.new(key=key, nonce=nonce)
  
  plaintext = cipher.decrypt(ciphertext)
  
  plaintext_ascii = plaintext.decode('ascii')
  
  print(plaintext_ascii)
  ```
## Euclid's Algorithm
```python
def gcd(a,b):
```
## RSA
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

Salve! Questo è un tutorial su RSA.

Riprendiamo ciò che hai visto a lezione.
RSA è uno schema basato sull'aritmetica modulare.

Ho scelto due piccoli numeri primi. p = 19, q = 17.
Il loro prodotto sarà il modulo (n) che utilizzeremo per fare tutte le operazioni del caso.
n = ? 323
Corretto!

Ora, a noi interessa fare potenze modulo n: questo ci permetterà di cifrare e decifrare i nostri messaggi.
Prima di tutto scegli un numero, che sarà il nostro messaggio da cifrare.
m = ? 55

ϕ(n) è la funzione di Eulero: corrisponde al numero di invertibili modulo n, ossia a
quanti interi tra 1 ed n-1 sono coprimi con n. Nel caso in cui n = pq, ϕ(n) = (p-1)(q-1).
ϕ(n) = ? 288
Corretto!

Infatti in questo caso gli invertibili modulo n sono:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 205, 206, 207, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 286, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322], len == 288.

Nota come calcolare ϕ(n) sia possibile solo grazie alla conoscenza dei fattori di n.
Sì, in questo caso siamo anche riusciti ad elencare esplicitamente tutti gli invertibili, ma
in generale p,q sono numeri molto molto grandi e l'unico modo (efficiente) è ricorrere alla formula.

La sicurezza di RSA è fondata proprio su questo fatto: impedire a tutti i costi ad un attaccante
di fattorizzare il modulo e dunque di recuperare ϕ(n).
Per questo motivo il modulo (n) è parte della chiave pubblica, mentre la sua fattorizzazione è privata.

Torniamo a noi: potenze modulo n. Abbiamo la base m = 55, scegli un esponente.
e = ? 13

Ottimo! Cifra ora il messaggio scelto con l'esponente pubblico scelto: c = m^e (mod n).

Nota: in Python qualcosa come c = m**e % n non va bene. Questo perché quella riga di codice calcola
dapprima tutto m**e (che spesso diventa enorme), per poi effettuare la riduzione modulo n.
Ci sono algoritmi più efficienti: se la curiosità ti infervora, prova a cercare "esponenziazione modulare".
Altrimenti, un'occhiata veloce alla documentazione relativa alla funzione pow() potrebbe esserti d'aiuto..
c = ? 225
Corretto!

Ottimo! Hai cifrato con successo il tuo messaggio. Ora vediamo come decifrarlo.

Naturalmente, vorremmo "effettuare la radice e-esima del nostro cifrato".
Questa, come potrai ormai immaginare, non corrisponde alla radice e-esima nei numeri reali.

Viene in nostro soccorso il Teorema di Eulero:
    Dati a,n interi coprimi, allora a^ϕ(n) = 1 (mod n).

Quindi in realtà, come hai potuto vedere nelle slides, fare la radice e-esima negli interi modulo n
corrisponde ad elevare il cifrato all'inverso modulare (rispetto a ϕ(n)) dell'esponente utilizzato!

Questo è il motivo per cui GCD(e, ϕ(n)) dev'essere uguale a 1. Altrimenti non è possibile invertirlo!
L'inverso dell'esponente pubblico si chiama esponente privato. Anche lui dev'essere mantenuto segreto!
d = ? 133
Corretto!


Ottimo! Infatti pow(c,d,n) == m = True

Da qui in avanti la strada che porta ad un'implementazione sicura di RSA è lunga e tortuosa: ci sarebbero moltissime
altre cose da dire, dettagli a cui stare attenti, casi limite da evitare. Sicuramente, ora sei in possesso delle basi
che ti servono per affrontare challenge un attimino più complesse di questa. Good job! :) flag{RSA_n0n_f4_p1u_C0s1_p4Ur4}

## *crib drag*
La lunghezza della chiave *k* deve essere uguale alla lunghezza del messaggio *m*, nel momento in cui si va ad effettuare la cifratura il risultato dell'operazione *c*, sarà della stessa lunghezza di *k* e *m*.

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
