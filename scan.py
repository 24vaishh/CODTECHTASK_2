import requests 
from .web_crawler import crawl_website
from .sql_injection import test_sql_injection
from .xss_detection import test_xss
from .csrf_checker import check_csrf

def run_scan(target_url):
    print(f"Scanning {target_url}...")
    return f"Scan results for {target_url}"

def main(target_url):
    print("===================================")
    print("    Web Application Vulnerability Scanner    ")
    print("===================================")

    print("\n[STEP 1] Crawling website...")
    crawl_website(target_url)

    fields = input("[?] Enter the input field names (comma-separated): ").strip().split(',')

    print("\n[STEP 2] Testing for SQL Injection...")
    test_sql_injection(target_url, fields)

    print("\n[STEP 3] Testing for XSS (Cross-Site Scripting)...")
    test_xss(target_url, fields)

    print("\n[STEP 4] Checking for CSRF Protection...")
    check_csrf(target_url)

    print("\n[✅] Scanning completed!")

if __name__ == "__main__":
    target_url = input("[?] Enter the target URL: ").strip()
    main(target_url)

