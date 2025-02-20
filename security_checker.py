import requests
from tqdm import tqdm
from colorama import Fore, Style, init
import time
import validators

# Initialize colorama for colored output
init(autoreset=True)

# List of important security headers to check
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy"
]

def progress_bar(description, total_steps):
    """Display a progress bar."""
    for _ in tqdm(range(total_steps), desc=Fore.GREEN + description, bar_format='{l_bar}{bar} {n_fmt}/{total_fmt}'):
        time.sleep(0.05)

def check_security_headers(url):
    """Check the presence of security headers for a given URL."""
    try:
        # Validate URL
        if not validators.url(url):
            print(Fore.RED + "[ERROR] Please enter a valid URL.")
            return

        # Set headers to mimic a regular browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        # Display progress bar for checking server
        progress_bar("Checking Server", 20)
        response = requests.get(url, headers=headers, timeout=10)

        # Display progress bar for analyzing headers
        progress_bar("Analyzing Headers", 30)
        print(Fore.CYAN + f"\n[INFO] Checking security headers for: {url}")
        
        missing_headers = []
        # Check each security header
        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(Fore.GREEN + f"[+] {header} is present")
            else:
                print(Fore.RED + f"[-] {header} is missing")
                missing_headers.append(header)

        # Display progress bar for analyzing cookies
        progress_bar("Analyzing Cookies", 20)
        missing_cookies = []
        if "set-cookie" in response.headers:
            cookies = response.headers.get("set-cookie")
            print(Fore.CYAN + "\n[INFO] Checking cookie flags:")
            if "Secure" in cookies:
                print(Fore.GREEN + "[+] Secure flag is set on cookies")
            else:
                print(Fore.RED + "[-] Secure flag is missing on cookies")
                missing_cookies.append("Secure flag")
            
            if "HttpOnly" in cookies:
                print(Fore.GREEN + "[+] HttpOnly flag is set on cookies")
            else:
                print(Fore.RED + "[-] HttpOnly flag is missing on cookies")
                missing_cookies.append("HttpOnly flag")
            
            if "SameSite" in cookies:
                print(Fore.GREEN + "[+] SameSite flag is set on cookies")
            else:
                print(Fore.RED + "[-] SameSite flag is missing on cookies")
                missing_cookies.append("SameSite flag")
        else:
            print(Fore.YELLOW + "[!] No cookies found in the response")
            missing_cookies.extend(["Secure flag", "HttpOnly flag", "SameSite flag"])

        # Print summary of missing headers and cookie flags
        print("\n" + "=" * 40)
        print(Fore.CYAN + "[SUMMARY OF MISSING CONTROLS]")
        
        if missing_headers:
            print(Fore.RED + "\nMissing Security Headers:")
            for header in missing_headers:
                print(Fore.RED + f" - {header}")
        else:
            print(Fore.GREEN + "[+] All security headers are present")
        
        if missing_cookies:
            print(Fore.RED + "\nMissing Cookie Flags:")
            for flag in missing_cookies:
                print(Fore.RED + f" - {flag}")
        else:
            print(Fore.GREEN + "[+] All cookie flags are properly set")

    except requests.exceptions.Timeout:
        print(Fore.RED + "[ERROR] Request timed out. The server may not be responding.")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[ERROR] Failed to connect. Please check the URL or your internet connection.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] An error occurred: {e}")

def main():
    """Main function to take user input and check headers."""
    print(Fore.CYAN + "=== Security Header & Cookie Flag Checker ===")
    url = input(Fore.CYAN + "Enter the URL (e.g., https://example.com): ")

    # Run the security header check
    check_security_headers(url)

if __name__ == "__main__":
    main()
