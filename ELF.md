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

