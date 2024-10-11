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

In alternativa è possibile usare [**pwntools**](./pwntools.md).

> A **stripped file** is a file without symbolic information (and other information not required for execution)

## GCC
This is a quick guide to the main options of `gcc`

Preprocessor > Compiler > *Assembler* > Linker

*Assembler phase is not a main phase*

- `-o` option change output filename, by default: `a.out`
- `-Wall` option enabling all the commonly used warning messages
- `-ansi` the compiler will enforce the rules and features defined by the ANSI standard
- `-std=cX (X=89,90,95,11,18)` specifies the C language standard to use for compiling your code add `-pedantic` to enforce strict adherence to the specified C language standard 
- `-E` option in GCC tells the compiler to preprocess the source code and output the result to standard output `gcc -E prog1.c > prog1.i` or `gcc -E prog1.c -o prog1.i`
- `-S` option in GCC tells the compiler to compile the source code into assembly language (x86-64 assembly language) `gcc -S prog1.c -o prog1.s`
- `-o` option in GCC tells the compiler to compile the source code into an object file, without linking it into an executable `gcc -c prog1.c -o prog1.o`

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
- `x/nfu addr` per ispezionare la memoria (ex. `x/x 0x0000b7c2`, `x/11i 0x7c00`), dove:
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
