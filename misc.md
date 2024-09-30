## Zip
- Files protected by a password: use John the Ripper
  **IGNOTO**
  `sudo apt install john`
  `john --wordlist=/usr/share/wordlists/rockyou.txt`
  ```python                                                                                  
  import zipfile
  import os
  import zlib
  
  def unzip(i):
      with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='utf-8') as wordlist:
          for word in wordlist:
              password = word.strip()
              try:
                  with zipfile.ZipFile(f'{i}.zip', 'r') as zip_ref:
                      zip_ref.setpassword(password.encode('utf-8'))
                      zip_ref.extractall('./')
 
                      if os.path.isfile(f'{i}.zip'):  # Assicurati di specificare il nome corretto
                          print(f"File '{i}.zip' estratto con la password: {password}")
                          return
              except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as e:
                  # Ignora errori dovuti a password errate o file ZIP non validi
                  print(f"Errore con {i}.zip: {e}")
                  continue
              except zlib.error as e:
                  print(f"Errore di decompressione con {i}.zip: {e}")
                  continue
  
  for i in range(100, 0, -1):
      unzip(i)
  ```


