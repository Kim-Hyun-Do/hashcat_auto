# hashcat_auto

It is hashcat module changed by r0b0ts.

It is for fuzzing hash algorithm when user don't know appropriate hash algorithm that fits the hash value.

# Help

```
usage: hashcat_auto.py [-h] [-m modeNumber] [-f hashFile] [-d dictionaryPath]

optional arguments:
  -h, --help            show this help message and exit
  
  -m, --modeNumber      Insert hashcat mode number ex)/path/to/hash_modes.txt
  
  -f, --hashFile        Insert hash ex)/path/hashcat/example400.hash
  
  -d, --dictionaryPath  Insert dictionary ex)/path/hashcat/example.dict
```

# Example

``hashcat -a 0 -m ~/hash_mode -f ~/hash_file -d ~/example.dict``

![123123](https://github.com/user-attachments/assets/fb37f648-e1d6-4ea9-962f-83523dc945cc)
