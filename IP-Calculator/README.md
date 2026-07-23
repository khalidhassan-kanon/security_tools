# IP Calculator

## 1. Overview

IP Calculator is a Python-based IPv4 subnet calculator built from scratch using bitwise operations. The project performs subnet calculations without relying on Python's built-in `ipaddress` module, providing a deeper understanding of IPv4 addressing, subnetting, binary conversion, and bit manipulation.

---

## 2. Features

* IPv4 Address Validation
* CIDR Prefix Validation
* Subnet Mask Calculation
* Wildcard Mask Calculation
* Network Address Calculation
* Broadcast Address Calculation
* First Usable Host Calculation
* Last Usable Host Calculation
* Usable Host Count
* IP Class Detection
* Private/Public IP Detection
* Unit Tests

---

## 3. Project Structure

```text
IP-Calculator/
│
├── calculator.py
├── ip_utils.py
├── validator.py
├── main.py
├── tests/
│   └── test_calculator.py
├── README.md
└── .gitignore
```

---

## 4. Requirements

* Python 3.12 or newer

---

## 5. Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/IP-Calculator.git
```

Move into the project directory.

```bash
cd IP-Calculator
```

---

## 6. Running the Program

```bash
python3 main.py
```

---

## 7. Running the Tests

```bash
python3 -m unittest discover tests
```

Expected output:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

---

## 8. Example

Input

```text
IP Address   : 192.168.1.10
Prefix Length: 24
```

Output

```text
Subnet Mask       : 255.255.255.0
Wildcard Mask     : 0.0.0.255
Network Address   : 192.168.1.0
Broadcast Address : 192.168.1.255
First Host        : 192.168.1.1
Last Host         : 192.168.1.254
Usable Hosts      : 254
IP Class          : C
IP Type           : Private
```

---

## 9. Bitwise Operations Used

| Operator | Purpose                       |
| -------- | ----------------------------- |
| `&`      | Network Address Calculation   |
| `\|`     | Broadcast Address Calculation |
| `~`      | Wildcard Mask Calculation     |
| `>>`     | Extract Individual Octets     |
| `<<`     | Build 32-bit Integer Values   |

---

## 10. Concepts Demonstrated

* IPv4 Addressing
* CIDR Notation
* Subnetting
* Binary and Decimal Conversion
* Bit Manipulation
* Bitwise Operators
* Modular Programming
* Unit Testing

---

## 11. Limitations

* Supports IPv4 only.
* Command-line interface only.
* Intended for educational purposes.

---

## 12. Future Improvements

* IPv6 Support
* Variable Length Subnet Mask (VLSM)
* Route Summarization
* Interactive Command-Line Interface
* Graphical User Interface

---

## 13. License

This project is released for educational and learning purposes.

---

## 14. Author

Developed by as Project 1 of a hands-on cybersecurity learning roadmap focused on implementing networking concepts through practical software development.
