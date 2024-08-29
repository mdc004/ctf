# Crypto
Il principale strumento da utilizzare in questo tipo di challenge è Python!!!!!

> Brutto scemo usa chat gpt, ci metti la metà del tempo

> Molte volte la flag non è propriamente cifrata ma semplicemente rappresentata in un encoding diverso tipo `base64` e altre cose simili, usare *Python* oppure usare [CyberChef](https://cyberchef.org/).

Bitwise significa operazioni a livello di bit

- Cifrario di cesare: comando `caesar`, scaricabile con `sudo apt install bsdgames`
- `ord(char)` tipicamente usato per il cifrario di cesare o in generale quando devi traslare le cifre
- moduli ecc. guardare taccuino mate del discreto
- [RSA](#RSA):
  - RsaCtfTool
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
- `b64decode()`
- ```Python
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
> 

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
