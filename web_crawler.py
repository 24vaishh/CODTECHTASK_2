import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    """Extracts all forms and input fields from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error if request fails
    except requests.RequestException as e:
        print(f"[ERROR] Failed to connect to {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    forms = soup.find_all("form")
    if not forms:
        print("[INFO] No forms found on the page.")
        return

    print(f"[INFO] Found {len(forms)} form(s) on {url}")

    for index, form in enumerate(forms, start=1):
        action = form.get("action")
        method = form.get("method", "get").upper()
        inputs = [i.get("name") for i in form.find_all("input") if i.get("name")]

        print(f"\n[FORM {index}] {method} {action if action else '[No action]'}")
        print(f"  Fields: {inputs}")

# Example usage
if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com"  # Change to your target URL
    crawl_website(target_url)
