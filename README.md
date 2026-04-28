# Password Generator Server (Python)

A simple HTTP-based password generator built using Python. This project creates strong, customizable passwords via a local web server.

## Features

* Generate random secure passwords
* Customize password length
* Enable/disable:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Lightweight (no external libraries required)

##  Technologies Used

* Python 3
* Built-in modules:

  * `http.server`
  * `random`
  * `string`

##  Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/password-generator-server.git
   cd password-manager
   ```

2. Run the server:

   ```bash
   python Password_Manager.py
   ```

3. Open your browser:

   ```
   http://localhost:8000
   ```

##  Usage

You can customize password generation using URL parameters.

###  Basic Usage

```
http://localhost:8000/12
```

➡️ Generates a 12-character password

###  Advanced Usage

```
http://localhost:8000/16?upper=1&lower=1&numbers=1&specials=0
```

###  Parameters

| Parameter  | Description                | Values |
| ---------- | -------------------------- | ------ |
| `upper`    | Include uppercase letters  | 1 / 0  |
| `lower`    | Include lowercase letters  | 1 / 0  |
| `numbers`  | Include digits             | 1 / 0  |
| `specials` | Include special characters | 1 / 0  |

##  Example

```
http://localhost:8000/10?upper=1&lower=0&numbers=1&specials=0
```

➡️ Generates a 10-character password with:

* Uppercase letters ✅
* Numbers ✅
* Lowercase ❌
* Special characters ❌

##  Notes

* Server runs locally on port `8000`
* Not intended for production use (no encryption or authentication)
* For learning and demonstration purposes only

##  License

This project is open-source and free to use.
