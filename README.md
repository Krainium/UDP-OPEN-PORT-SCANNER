# 🔎 UDP Open Ports Checker

A multithreaded **Python UDP port scanner** that attempts to identify open UDP ports on a target IP address.

The script scans **all UDP ports (1–65536)** and sends a small DNS-style request to each port. If the target responds, the port is considered open and is recorded.

The results are displayed in the terminal and saved to a file for later review.

---

# ✨ Features

* 🔍 Scans **all UDP ports (1–65536)**
* ⚡ **Multithreaded scanning**
* 📊 Terminal **progress bar** using `tqdm`
* 🎨 **Colored output** using `termcolor`
* 🖥️ ASCII banners using `pyfiglet`
* 💾 Automatically saves discovered open ports
* 📁 Creates a results folder automatically
* 🧵 Uses Python **threading** for faster scanning

---

# 🧰 Requirements

* Python **3.7+**

### Python Modules

Built-in modules:

* `socket`
* `threading`
* `os`

External modules:

* `tqdm`
* `pyfiglet`
* `termcolor`

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/krainium/udp-open-ports-checker.git
cd udp-open-ports-checker
```

Install dependencies:

```
pip install tqdm pyfiglet termcolor
```

Or install using a requirements file.

Create `requirements.txt`:

```
tqdm
pyfiglet
termcolor
```

Install with:

```
pip install -r requirements.txt
```

---

# 🚀 Usage

Run the script:

```
python udp-port-scanner.py
```

You will be prompted to enter the **target IP address**:

```
Enter the target IP address:
```

Example:

```
Enter the target IP address: 192.168.1.1
```

The scanner will begin checking UDP ports.

---

# 📂 Output

Open ports are saved to:

```
opened-ports/open.txt
```

Example file content:

```
Target-IP: 192.168.1.1

Port 53 is opened!
Port 161 is opened!
Port 123 is opened!
```

---

# 🖥 Example Terminal Output

```
UDP OPEN PORTS CHECKER VERSION 1
SCRIPT MADE BY KRAINIUM

Scanning:  50%|███████████████████ | 32000/65536 ports

Port 53 is open
Port 161 is open

Port scan complete
```

---

# ⚠️ Disclaimer

This tool is intended for:

* Educational purposes
* Network diagnostics
* Security testing on systems **you own or have permission to test**

Unauthorized scanning of networks or servers may violate laws or policies.

---

# 📂 Project Structure

```
udp-open-ports-checker/
│
├── udp-port-scanner.py
├── requirements.txt
├── opened-ports/
│   └── open.txt
└── README.md
```

---

# 👨‍💻 Author

Krainium
GitHub: https://github.com/krainium

---

# 📜 License

MIT License
