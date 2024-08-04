import subprocess
import argparse


def read_files(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    

def run_hashcat(hash_mode, hash_file, dict_file):
    command = f'hashcat -a 0 -m {hash_mode} {hash_file} {dict_file}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr


if __name__ == "__main__":

    banner = """\u001b[36m
      _   _           _    _             _   
     | | | | ___  ___| | _| |_ __ _ _ __| |_ 
     | |_| |/ _ \/ __| |/ / __/ _` | '__| __|
     |  _  |  __/ (__|   <| || (_| | |  | |_ 
     |_| |_|\___|\___|_|\_\\__\__,_|_|   \__|
                                          
    \u001b[32m - coded with <3 r0b0ts\u001b[0m 
    """
    print(banner)

    parser = argparse.ArgumentParser()
    parser.add_argument("-m","--modeNumber",help="Insert hashcat mode number ex)/path/to/hash_modes.txt",action="store",default=True)
    parser.add_argument("-f","--hashFile",help="Insert hash ex)/path/hashcat/example400.hash",action="store", default=True)
    parser.add_argument("-d","--dictionaryPath",help="Insert dictionary ex)/path/hashcat/example.dict",action="store",default=True)
    args = parser.parse_args()
    
    hash_modes = read_files(args.modeNumber)
    
    for hash_mode in hash_modes:        
        stdout, stderr = run_hashcat(hash_mode, args.hashFile, args.dictionaryPath)
        print(f"Hash Mode: {hash_mode}")
        print("Output:")
        print(stdout)
        if stderr:
            print("Errors:")
            print(stderr)   
