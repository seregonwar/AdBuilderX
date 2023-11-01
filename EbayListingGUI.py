import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class EbayListingGUI(BoxLayout):
    def __init__(self, data_handler, html_generator, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # Widgets
        self.add_widget(Label(text='Nome utente:'))
        self.username_input = TextInput()
        self.add_widget(self.username_input)

        self.add_widget(Label(text='Titolo annuncio:'))
        self.title_input = TextInput()
        self.add_widget(self.title_input)

        # ... altri widget per descrizione, prezzo, immagini

        self.submit_button = Button(text='Crea annuncio', on_press=self.submit)
        self.add_widget(self.submit_button)

        # Data Handler and HTML Generator
        self.data_handler = data_handler
        self.html_generator = html_generator

    def submit(self, btn):
        # Recupera i dati dalla GUI
        username = self.username_input.text
        title = self.title_input.text
        # Recupera altri dati da altri widget

        # Crea un dizionario con i dati
        listing_data = {
            'username': username,
            'title': title,
            # Aggiungi altri dati
        }

        # Invia i dati al gestore dei dati per la validazione
        is_valid = self.data_handler.validate(listing_data)

        if is_valid:
            # Genera l'HTML utilizzando il generatore HTML
            html = self.html_generator.generate(listing_data)
            # Salva l'HTML su un file o fa qualsiasi altra operazione necessaria
            # ...

            print("Annuncio eBay creato!")
        else:
            print("Dati non validi")

class EbayListingApp(App):
    def __init__(self, data_handler, html_generator, **kwargs):
        super().__init__(**kwargs)
        self.data_handler = data_handler
        self.html_generator = html_generator

    def build(self):
        return EbayListingGUI(self.data_handler, self.html_generator)

if __name__ == '__main__':
    # Inizializza il gestore dei dati e il generatore HTML
    data_handler = EbayListingData()
    html_generator = EbayHTMLGenerator()

    app = EbayListingApp(data_handler, html_generator)
    app.run()
