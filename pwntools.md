## [pwntools](https://docs.pwntools.com/en/stable/intro.html)
pwntools permette di:
- [Tubes](#Tubes): Wrapper I/O per connessioni remote o per binari locali
- [Packing](#Packing): Conversioni tra numeri e bytes in little/big endian
- [ELFs](https://docs.pwntools.com/en/stable/elf/elf.html): Caricare e analizzare ELF direttamente da python
- [Assembly](https://docs.pwntools.com/en/stable/asm.html): Assemblare codice on-the-fly
- [GDB Debug](https://docs.pwntools.com/en/stable/gdb.html): Debuggare programmi con [`gdb`](./ELF.md#GDB)

Pwntools ci permette quindi di scrivere script in python che interagiscono con un servizio in locale o in remoto.

### [Tubes](https://docs.pwntools.com/en/stable/tubes.html)
```python
# Importa la libreria di pwntools
from pwn import *

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "hostname"
    PORT = 1234
    r = remote(HOST, PORT)

    # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    r.send(b"Ciao!")

    # .sendline() è identico a .send(), però appende un newline dopo i dati
    r.sendline(b"Ciao!")

    # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    r.sendafter(b"something", b"Ciao!")

    # solo dopo che viene ricevuta la stringa "something"
    r.sendlineafter(b"something", b"Ciao!")

    # .recv() riceve e ritorna al massimo 1024 bytes dalla socket
    data = r.recv(1024)

    # .recvline() legge dalla socket fino ad un newline
    data = r.recvline()

    # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"
    data = r.recvuntil(b"something")

    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
```

*Esempio di codice*
```python
HOST = "software-17.challs.olicyber.it"
PORT = 13000
r = remote(HOST, PORT)
data = r.recvuntil(b"per iniziare ...")
r.sendline(b"v")
data = r.recvline()

summ = sum(map(int, r.recvline()[1:-2].decode("utf-8").split(", ")))
data = r.recv(1024)
r.sendline(str(summ).encode())
data = r.recvline()
print(data)

r.close()
```

*Esempio 2*
```python
# Connessione al server
HOST = "software-18.challs.olicyber.it"
PORT = 13001
r = remote(HOST, PORT)

# Inizia la comunicazione
data = r.recvuntil(b"per iniziare ...")
r.sendline(b"v")

for i in range(0, 100):
    data = r.recvline().decode("utf-8").split(" ")
    print(data)
    print(r.recvline())
    #print(r.recvuntil(b"Risultato : "))

    # Estrai le informazioni necessarie
    num = int(data[5], 16)
    how = data[8]

    if how == '32-bit\n':
        # Converte il valore in byte string e poi interpreta come 32-bit
        payload = p32(num, endian='little')
    else:  # 64-bit
        payload = p64(num, endian='little')
    
    #r.sendline(payload)
    r.sendafter(b": ", payload)     

print(r.recv(1024))

# Chiudi la connessione
r.close()
```

### [Packing](https://docs.pwntools.com/en/stable/util/packing.html)
Pwntools offre dei wrapper per la libreria `struct` di python (che offre `struct.pack`).

- `p64(num, endianness="little", ...)` Esegue il packing di un integer a $64 bit$
- `p32(num, endianness="little", ...)` Esegue il packing di un integer a $32 bit$
- `u64(data, endianness="little", ...)` Esegue l'unpacking di integer a $64 bit$
- `u32(data, endianness="little", ...)` Esegue l'unpacking di integer a $32 bit$

*Software 18 - Pwntools 2 | non risolta, questo codice non va*
```python
#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():     
    # Connessione al server
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)

    # Inizia la comunicazione
    data = r.recvuntil(b"per iniziare ...")
    r.sendline(b"v")

    for i in range(0, 100):
        # Ricevi e analizza i dati
        data = r.recvline().decode("utf-8").split(" ")
        print(data)

        # Estrai le informazioni necessarie
        num = int(data[5], 16)
        direction = data[6]
        how = data[8]

        # Gestisci i dati in base alla richiesta
        if direction == 'unpacked':
            if how == '32-bit\n':
                # Converti il numero in byte string e poi interpreta come 32-bit
                payload = p32(num, endian='little')
                r.recv(1024)
                r.sendline(payload)
                print('unpacked 32-bit')
            else:  # 64-bit
                payload = p64(num, endian='little')
                r.recv(1024)
                r.sendline(payload)
                print('unpacked 64-bit')
        else:  # packed
            if how == '32-bit\n':
                # Converte il valore in byte string e poi interpreta come 32-bit
                payload = p32(num, endian='little')
                r.recv(1024)
                r.sendline(payload)
                print('packed 32-bit')
            else:  # 64-bit
                payload = p64(num, endian='little')
                r.recv(1024)
                r.sendline(payload)
                print('packed 64-bit')

    # Ricevi e stampa la risposta finale
    print(r.recv(1024))

    # Chiudi la connessione
    r.close()


if __name__ == "__main__":
    main()
```
