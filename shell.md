- **symlink**: they are **pointer** to another file or directory, look like in C, to create s symlink: `ln -s /path/to/original/file /path/to/symlink` *it means that the first file is the original file and the second is the pointer file*
- `grep picoCTF{ * -r` search *picoCTF* in every file in every directory

## Zips
- [Zipception](https://training.olicyber.it/challenges#challenge-9)

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
