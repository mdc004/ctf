- **symlink**: they are **pointer** to another file or directory, look like in C, to create s symlink: `ln -s /path/to/original/file /path/to/symlink` *it means that the first file is the original file and the second is the pointer file*
- **`du`** *disk usage*
- [**`find`**](https://www.grymoire.com/Unix/Find.html#uh-0) `[path] [options] [expression]`
  - `-name`
  - `-size` *+1M   # files larger than 1 MB, -100k # files smaller than 100 KB*
  - `-mtime` *-7   # files modified in the last 7 days* or `-atime` *for access time*
  - `-perm` */111 has exe permession*
  - `-print` *display results* or `-ls` *to list the results*
  - `-type x` *d directory, f file*
  - `-maxdepth N` *limit the search to N levels of depth*
  - `-exec` *exec a command on the file: `-exec grep -l "testo_da_cercare" {} +`*
    - `+` Esegue il comando su tutti i file trovati in una sola volta, è più efficiente
    - `\` Esegue il comando specificato per ogni file trovato singolarmente
  - `-user username` 
  - `-group groupname` 
  - ``
  - ``
- **`grep`**
  - `grep picoCTF{ * -r` search *picoCTF* in every file in every directory
  - `file ./-file0* | grep ASCII` *search every file that is a particular type, but use: `find . -type f -exec file {} + | grep ASCII`*
- **`uniq`**
  - `-c` *filter out repeated lines in a sorted file and count the occurrences of each line*
- **`wc`** print newline, word, and byte counts for each file
  - `-l` line count
- **`xargs`** `[options] [command]` take the output of a command and pass its as arguments to another command
- **ZIPS** [Zipception](https://training.olicyber.it/challenges#challenge-9)

  Unzip 3000 times a file:
  
  ```shell
  #!/bin/bash
  for i in {1..3000}
  do
    echo "Estrazione numero $i"
    
    n=$((3001 - i))
    unzip -o "flag$n.zip"
  
    rm -r "flag$n.zip"
  done
  
  ```
## Random command
- `find . -type f -exec file {} + | grep ASCII | cut -d: -f1 | tr -d ' ' | xargs cat ` *trova i file che contengono ASCII text e li stampa. In mezzo toglie gli spazi iniziali e le parti che non sono file name*
- `find . -type f -size 1033c -exec cat {} + | tr -d ' '` *filter files with a 1033 bytes size and print their content*
- `find / -user bandit7 -group bandit6 -size 33c 2> /dev/null -exec cat {} +` *search in ehole the find systsem by user and gruop and delete the errors*
- `cat data.txt | sort | uniq -u` *stampa solo le righe che si ripetono una volta*
- `` **
- `` **
- `` **
