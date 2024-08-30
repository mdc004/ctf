An **ELF** is an executable file, a binary file, this format is used in [Linux](#linux), it is used for both reverse and pwn challenge.

A binary file can be static or dinamic

To execute a ELF file: `chmod +x nomefile`, more about `chmod` [here](#chmod)
> Se non vanno mettere davanti al nome del file ./ e aggiungere il permesso di esecuzione 

When you have a Binary challenge you have to understand how the program works, before using ghidra you can try this commands:
- `strings` or better `strings file | grep flag`

If you don't find the flag with `strings` try to undestand how the binary work with these commands:
- `file`
- `ldd` - *permette di elencare le shared libraries richieste da un file binario*.
- `ltrace` - dinamic analysis, display **functions** has been **called**. `-e` filter called functions (use one or more `grep`)
- `strace` - static analysis (trace delle syscalls eseguite da un binario). `-f` syscall eseguite dai processi figli
- `objdump` - *displays information about one or more object files* 
  - use the `-d` option to list the section of the ELF 
  - `-h` ti permette di elencare le sezioni di un ELF
- `objcopy`
  - `objcopy --dump-section .text=main_text main out_objcopy` - *This command extracts the .text section from main and saves it to out_objcopy* (provalo, tante volte la flag è nascosta in sezioni tipo commenti o text).
- `readelf`, use the `-h` option
- `checksec`
- [`gdb`](#GDB)

In alternativa è possibile usare [**pwntools**](#pwntools).

> A **stripped file** is a file without symbolic information (and other information not required for execution)

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

## GDB
`gdb ./file`

- `run` esegue il programma
- `break` oppure `b` inserisce un **breakpoint** ad un determinato indirizzo o ad una funzione, *es: `b `*
- `CTRL + C` mette in pausa, `continue` riprende
- `disassemble function_name` permette di disassemblare il contenuto di una funzione mostrando gli offset delle varie istruzioni rispetto all'indirizzo della funzione.
- `info registers` stato registri CPU
- `print`, abbreviabile con `p` stampa risultato espressioni, in particolare: `print/f expr`:
  - `/f`  è il formato con il quale stampare il risultato dell'espressione:
    - `x` per l'esadecimale
    - `f` per i float
    - `d` per i numeri interi con segno
    - `u` per i numeri interi unsigned
  - `expr` può essere un registro, come ad esempio `$rax`, ma può anche essere un'espressione aritmetica come `$rax+0x100`
- `set {type}address = value` cambia il contenuto della memoria, dove `type` indica il tipo della variabile all'indirizzo `address`. Per conoscere l'indirizzo di una variabile usare `p &var` *Per esempio `set {int}0x650000 = 0x42`*
- `x/nfu addr` per ispezionare la memoria, dove:
  - `x` -> Examine
  - `n` -> Numero intero che specifica quanti elementi stampare (opzionale, di default 1)
  - `f` -> Formato con il quale stampare la memoria, per esempio: (opzionale, di default x):
    - `s` per le stringhe
    - `i` per il disassembly
    - `x` per l'esadecimale
    - `f` per i float
    - `d` per i numeri interi con segno
  - `u` -> La dimensione di ogni elemento da stampare, per esempio: (opzionale, di default w):
    - `b` Bytes
    - `h` Halfwords (2 bytes)
    - `w` Words (4 bytes)
    - `g` Giant words (8 bytes)
  - `addr` può essere sia un indirizzo di memoria, come $0x5000000$, sia un registro che contiene un indirizzo, come `$rax`.
    Insieme ad `addr` si possono specificare delle operazioni aritmetiche, ad esempio `$rax+8`

> All'interno del codice sorgente potrebbero essere stati inseririti manualmente dei **brakpoint** per il debugger

## Heap Inspection Security Vulnerability
- [Heap Inspection Security Vulnerability | C Programming Tutorial](https://youtu.be/hHlE2BpxjKU) - by Portfolio Courses
- [The Heap: How do use-after-free exploits work? - bin 0x16](https://youtu.be/ZHghwsTRyzQ) - by LiveOverflow

Quando libero la memoria in realtà non vado a riazzerarla, bensì tolgo solo i vincoli che la bloccavano: 

*prendendo ad esempio [C](#c), la funzione `free()` libera la memoria, tuttavia nel momento in cui io vado a riaccedere a quelle celle di memoria trovo ancora i dati che erano stati lasciati precedentemente*.
