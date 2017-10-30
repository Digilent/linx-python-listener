# linx-python-listener

LINX https server listener using python 2.7

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Python 2.X (2.7.9)
openssl

### Installing

Clone this repository

```
git clone https://github.com/Digilent/linx-python-listener.git
```

Move to project directory

```
cd linx-python-listener
```

Generate the server key

```
openssl genrsa -des3 -out server.key 1024
```

Generate the Certificate Signing Request (CSR)

```
openssl req -new -key server.key -out server.csr
```

Generate the certificate

```
openssl x509 -req -days 1024 -in server.csr -signkey server.key -out server.crt
```

Create the pem file

```
cat server.crt server.key > server.pem
```

Run the server

```
python linx-server.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details