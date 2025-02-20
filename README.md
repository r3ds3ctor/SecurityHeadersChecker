# SecurityHeadersChecker
SecurityHeadersChecker is a Python tool that checks for the presence of security headers and cookie flags on a given URL. This tool is useful for developers and system administrators who want to ensure that their web applications are properly configured to protect against common vulnerabilities.

## Features

- Checks for security headers such as 'Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection', 'Referrer-Policy', and 'Permissions-Policy'.
- Verifies cookie flags like 'Secure', 'HttpOnly', and 'SameSite'.
- Displays results with color coding for better readability.
- Robust error handling.

## Requirements

- Python 3.x
- Libraries: 'requests', 'tqdm', 'colorama'

## Installation

## 1.Clone the repository:
   '''bash
   git clone https://github.com/yourusername/SecurityHeadersChecker.git
   cd SecurityHeadersChecker

## 2.Install Dependencies

'''bash
pip install -r requirements.txt

## 3.Usage
Run the script with Python:
python security_checker.py

## Example Output

<img width="745" alt="Screenshot 2025-02-19 at 8 56 17 PM" src="https://github.com/user-attachments/assets/f95686da-cc57-4cdc-8b17-ed52b4e0db01" />


## Contributions
Contributions are welcome. Please open an issue or submit a pull request if you have any improvements or fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
