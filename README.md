# Slavolt Scraper
Send download requests and recieve downloads links from the Slav Art [Divolt](https://divolt.xyz/) server via the command line. 
## Requirements
* Python
* A Divolt account that has joined the slavart server.
* The Divolt account's x-session-token (see below).

To obtain an x-session-token:

1. Log in to [Divolt](https://divolt.xyz/).
2. Open browser DevTools (f12).
3. Click the network tab and then select the 'XHR' filter.
4. Click a request with the domain of 'api.divolt.xyz'.
5. Select the header tab and copy the value of the x-session-token (can be found towards the bottom of the list). If there is no x-session-token select another request.
**Note: Do not log out of divolt once you have obtained your token as it will no longer work (Just close tab).**
## Usage
1. Download slavoltscraper.py and requirements.txt.
2. Install requirements.txt using `pip install -r requirements.txt`.
3. Run scraper using `python3 slavoltscraper.py` and follow prompts as required.
## Acknowledgements
Thanks to the slavart creators and account providers for creating this great service. Donate to them if you can (info provided in the severs #donate channel). 
