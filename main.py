import argparse
import logging
from EbayListingGUI import EbayListingGUI
from EbayListingData import EbayListingData
from html_generator import EbayHTMLGenerator
from html_generator import EbayHTMLGenerator
html_generator = EbayHTMLGenerator()

def configure_logging(log_level):
    logging.basicConfig(level=log_level)

def main():
    parser = argparse.ArgumentParser(description="Create an eBay listing")
    parser.add_argument("--file", default="ebay_listing.html", help="Nome del file HTML di destinazione")
    parser.add_argument("--log-level", default="INFO", help="Livello di registrazione (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    args = parser.parse_args()

    configure_logging(args.log_level)

    gui = EbayListingGUI()
    data = EbayListingData()
    html_generator = EbayHTMLGenerator()

    try:
        gui.run()
        listing_data = gui.get_listing_data()

        is_valid = data.validate(listing_data)
        if not is_valid:
            logging.error("Invalid data")
            return

        html = html_generator.generate(listing_data)
        save_html_to_file(html, args.file)

        logging.info("eBay listing created and saved to %s", args.file)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))

def save_html_to_file(html, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html)
    except IOError as e:
        logging.error("Unable to save HTML to file: %s", str(e))

if __name__ == "__main__":
    main()