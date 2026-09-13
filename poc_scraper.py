from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_real_leases():
    print("Launching headless Chromium browser to render JavaScript...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to OffCampusPhilly...")
        page.goto("https://www.offcampusphilly.com/properties-1", timeout=60000)
        
        print("Waiting for database to inject property cards...")
        # Wait 4 seconds to ensure Wix finishes loading the database items
        page.wait_for_timeout(4000)
        
        # Grab the fully rendered HTML now that the JS has executed
        html_content = page.content()
        browser.close()

    # Pass the fully rendered HTML to BeautifulSoup
    print("\n--- ISOLATING REAL PROPERTIES ---")
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Grab all text elements
    text_blocks = soup.find_all(['h2', 'h3', 'h4', 'span', 'p'])
    
    extracted = set()
    for block in text_blocks:
        text = block.get_text().strip()
        
        # Filter for actual addresses and prices (ignoring random menu words)
        if ("St" in text or "Ave" in text or "Unit" in text or "$" in text):
            # Exclude long paragraphs and those sidebar filters we saw earlier
            if 6 < len(text) < 35 and "-" not in text and text not in extracted:
                print(f"Data Point Extracted: {text}")
                extracted.add(text)

if __name__ == "__main__":
    fetch_real_leases()