from playwright.sync_api import sync_playwright
from urllib.parse import quote_plus


def load_queries():
    with open("queries.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


queries = load_queries()

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for query in queries:

        url = f"https://www.bing.com/search?q={quote_plus(query)}"

        print(f"Visiting: {url}")

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        print(f"Loaded: {query}")

        # Optional delay
        page.wait_for_timeout(3000)

    browser.close()