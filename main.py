import argparse
import logging
from gui import EbayListingGUI
from data import EbayListingData
from html_generator import EbayHTMLGenerator

def configure_logging(log_level):
    logging.basicConfig(level=log_level)

def main():
    parser = argparse.ArgumentParser(description="Crea un annuncio eBay")
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
            logging.error("Dati non validi")
            return

        html = html_generator.generate(listing_data)
        save_html_to_file(html, args.file)

        logging.info("Annuncio eBay creato e salvato in %s", args.file)
    except Exception as e:
        logging.error("Si è verificato un errore: %s", str(e))

def save_html_to_file(html, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html)
    except IOError as e:
        logging.error("Impossibile salvare l'HTML su file: %s", str(e))

if __name__ == "__main__":
    main()
