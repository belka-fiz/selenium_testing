# Selenium practice

This repo is made for practice exercises for [Test automation using Selenium and Python course](https://stepik.org/course/575)

## Contents
### Module 1

- Running the first script
- Basic practice of choosing elements:
  - By id
  - By css selectors
  - By XPATH
  - etc.

### Module 2
- Multiple-choice elements
- Getting an attribute from an element
- Executing JS script

### Module 3
- Introduction to Git(like pushing this to the remote)
- Something about test frameworks - coming soon

### Module 4 - coming soon

- Page Object pattern
- first real tests 

---
## Installation
### Linux/Mac:
Assuming Python3 is already installed
```shell
git clone https://github.com/belka-fiz/selenium_testing.git
cd selenium_testing
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Windows
IDK:) use WSL and the script above)))

## Running
Run from the repo root, replacing `module_name` and `script_name` with the desired ones:
```shell
python3 module_name/script_name.py
```