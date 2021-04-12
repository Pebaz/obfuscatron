# Obfuscatron

Encrypt data by storing it within a Python script that pretends to just be
"obfuscated"

### Features

Right now, Obfuscatron is able to store data within the following Python syntax:

* Variables
* Class Names
* Function Names
* Type Hint Identifiers

### Installation

```bash
$ pip install obfuscatron
$ pip install "git+https://github.com/Pebaz/obfuscatron"
```

### Usage

```bash
$ obfuscatron FILE.py encode DATAFILE OUTFILE
$ obfuscatron OUTFILE.py decode DATAFILE
```
