🔍 Advanced-NSLookup (Python)

This project is a custom implementation of the classic `nslookup` tool, written in **Python from scratch** using only sockets and the DNS protocol format.
It demonstrates how DNS queries and responses work at a low level without relying on external libraries.

 🚀 Features

* Build raw DNS queries (A, AAAA records implemented).
* Send queries directly to a DNS server (default: Google DNS `8.8.8.8`).
* Parse DNS responses manually (IPv4 and IPv6 addresses).
* Learn how `nslookup` works internally at the packet level.

 📂 Project Structure

advanced-nslookup/
│
├── nslookup.py   # main source code
├── README.md     # project documentation
```

⚙️ How It Works

1. **Build Query**

   * Construct DNS packet manually using `struct.pack`.
   * Encode the domain name into DNS label format.
   * Set query type (A = IPv4, AAAA = IPv6).

2. **Send Query**

   * Open a UDP socket.
   * Send the query to the DNS server on port `53`.

3. **Parse Response**

   * Extract headers and answer sections.
   * Decode IPv4/IPv6 addresses from raw binary format.

▶️ Usage
 1. Clone the Project

```bash
git clone https://github.com/mrsraghvi/nslookup.git
cd advanced-nslookup
```

2. Run the Script

```bash
python nslookup.py
```

3. Example Output

```
Enter domain: google.com
Fetching A (IPv4) Records...
A Record: 142.250.183.174
A Record: 142.250.183.142

Fetching AAAA (IPv6) Records...
AAAA Record: 2404:6800:4007:80c::200e
```

---

🔧 Requirements

* Python 3.x
* No external dependencies (uses only `socket`, `struct`, `random`)

---

📖 Learning Outcomes

* Understand DNS protocol structure (headers, questions, answers).
* Learn how queries like `A` (IPv4) and `AAAA` (IPv6) are processed.
* Hands-on practice with **raw sockets** and **binary data parsing**.

---

🛠️ Future Enhancements

* Add support for more record types:

  * MX (Mail Exchange)
  * CNAME (Canonical Name)
  * NS (Name Servers)
  * TXT (Text Records)
  * PTR (Reverse DNS)
* Implement command-line arguments:

  ```bash
  python nslookup.py google.com --type=MX
  ```
* Provide verbose debugging (show raw packets).

📜 License

This project is open-source under the **MIT License**.
Feel free to use and modify for learning purposes.
