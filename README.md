# PhillyLease Sniper - Proof of Concept
**CIS 3296 Software Design - Fall 2026**  
**Author:** Gavin Montross

## Project Overview
This repository contains the Proof of Concept (PoC) data-ingestion pipeline for the **PhillyLease Sniper** project. 

Modern local property management websites (such as OffCampusPhilly or Temple's official off-campus housing portal) utilize Single Page Application (SPA) architectures. These sites inject property listing data via JavaScript milliseconds after the initial page load. Standard HTTP scraping libraries (like `requests`) only capture the static HTML scaffolding and fail to see the actual property cards.

This PoC demonstrates a functional workaround by utilizing a headless browser engine to fully render the DOM before extraction.

## How It Works
1. **Playwright** launches a headless (invisible) Chromium browser instance.
2. The browser navigates to the target property aggregator and waits 4 seconds for the external database to inject the property cards into the DOM via JavaScript.
3. The fully rendered HTML is extracted and passed to **BeautifulSoup4**.
4. Specific text nodes containing pricing, amenities, and Philadelphia street addresses are isolated and printed to the terminal, proving the data pipeline is ready for backend JSON serialization.

## System Requirements
* Python 3.9 or newer
* macOS, Windows, or Linux operating system

## Installation Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone [YOUR_REPO_LINK_HERE]
   cd [YOUR_REPO_DIRECTORY]
