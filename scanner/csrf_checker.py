import requests
from bs4 import BeautifulSoup

def check_csrf(url):
    """
    Check if a webpage has CSRF protection (hidden anti-CSRF tokens).
    
    :param url: Target URL to test
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to connect to {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    forms = soup.find_all("form")
    if not forms:
        print("[INFO] No forms found on the page.")
        return
    
    print(f"[INFO] Found {len(forms)} form(s) on {url}")
    
    csrf_vulnerable_forms = 0
    for index, form in enumerate(forms, start=1):
        inputs = {i.get("name") for i in form.find_all("input") if i.get("name")}
        
        # Common CSRF token field names
        csrf_tokens = {"csrf_token", "authenticity_token", "_csrf", "token"}

        if not csrf_tokens.intersection(inputs):
            print(f"[WARNING] Form {index} on {url} is missing CSRF protection!")
            csrf_vulnerable_forms += 1
        else:
            print(f"[INFO] Form {index} on {url} has CSRF protection.")

    if csrf_vulnerable_forms == 0:
        print("[INFO] No CSRF vulnerabilities detected.")

# Example usage
if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com/login.php"  # Change to your target
    check_csrf(target_url)
