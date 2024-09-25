To open an image: `xdg-open file`

Eseguire i classici comandi:
- files
- strings
- exiftool
- head
- [ImageMagick](#imaginemagick) ***Run the command using***: `display`
-  [aperisolve](https://www.aperisolve.com/) *è un insieme di tutti i possibili metodi, fa un'analisi generale*
- QR codes and bar codes:
    - `pyzbar` python library
      `pip install pyzbar`
      ```python
      from PIL import Image
      from pyzbar.pyzbar import decode, ZBarSymbol
    
      img = Image.open('flag.png')
    
      decoded_list = decode(img)
    
      for el in decoded_list:
          print(el)
      ```

> Ricordati di modificare luminosità, contrasto, colori...

### Steganografia
Molte volte si usa nascondere la flag all'interno dell'immagine, utilizzando la tecnica della [[steganografia]].

Di seguito alcuni comandi e strumenti utilizzati per estrarre i file conenuti all'interno di un altro file, che giro strano di file dentro altri file che contengono file?

- `binwalk`
    Di base è possbile usare [binwalk](#binwalk)  senza alcuna opzione per controllare se nel file siano presenti altri contenuti nascosti, in caso positivo con l'opzione `-e`: `binwalk -e nomefile` si possono estrarre, è l'opzione più **conveniente** e **semplice**.
- aperisolve
    Aperisolve è un sito che analizza le immagini mostrando varie informazioni tra cui eventuali file nascosti, è scomodo e funziona male
- `stego-lsb`
    Un tool come [***stego-lsb***](https://github.com/ragibson/Steganography) può estrarre file nascosti dentro altri file

    `stegolsb steglsb -r -i Gab-chan.png -o output_file.zip -n 2`

    Dove:
    - `steglsb` serve a trovare file nascosti nell'ultimo bit rgb delle immagini

    ```
        Command Line Arguments:
        -h, --hide                      To hide data in an image file
        -r, --recover                   To recover data from an image file
        -a, --analyze                   Print how much data can be hidden within an image   [default: False]
        -i, --input TEXT                Path to an bitmap (.bmp or .png) image
        -s, --secret TEXT               Path to a file to hide in the image
        -o, --output TEXT               Path to an output file
        -n, --lsb-count INTEGER         How many LSBs to use  [default: 2]
        -c, --compression INTEGER RANGE
                                        1 (best speed) to 9 (smallest file size)  [default: 1]
        --help                          Show this message and exit.
    ```
- `steghide`
    Steghide is a steganography program that is able to hide data in various kinds of image‐ and audio‐files. The color‐ respectivly sample‐frequencies are not changed thus making the embedding resistant against first‐order statistical tests.

    An exemple from a *picoCTF*: `steghide extract -sf file -p DUEDILIGENCE`
- `stegsolve`
    staganografia: cosa sarebbe? Nascondere cose nelle immagini?

    Passare poi a stegsolve: recarsi nella cartella tools della tools e lanciare il comando:
    ```bash
        java -jar stegsolve.jar
    ```
- Steganos Security Suite
- S-Tools
- OutGuess
- Invisible Secrets 4
- MSU StegoVideo

### Corruzione header 
Se pensi che sia necessario modificare l'header dell'immagine, è necessario capire il tipo di immagine e poi modificare l'header copiandolo da un'immagine in quel formato, per farlo è possibile utilizzare un software quale [HxD]()

## OCR

`sudo apt-get update`

`sudo apt-get install tesseract-ocr`

`pip install pytesseract pillow`

```python
import pytesseract
from PIL import Image
import requests
from io import BytesIO

# Image URL
image_url = 'http://captcha.challs.olicyber.it/your_image_path_here'

# Fetching the image from the URL
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

# Use Tesseract to extract text
text = pytesseract.image_to_string(img)

print(text)
```
