
## Challenge example
[Zipception](https://training.olicyber.it/challenges#challenge-9)

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
