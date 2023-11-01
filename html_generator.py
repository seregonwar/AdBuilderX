from kivy.lang import Builder

class EbayHTMLGenerator:
    def generate(self, listing_data, custom_layout=None):
        if custom_layout:
            # Utilizza il layout personalizzato
            layout = Builder.load_string(custom_layout)
            html = self.replace_placeholders(layout, listing_data)
        else:
            # Utilizza un modello HTML predefinito
            html = self.generate_default_html(listing_data)

        return html

    def replace_placeholders(self, layout, listing_data):
        # Associa i dati agli ID dei widget nel layout
        for key, value in listing_data.items():
            if hasattr(layout, 'ids') and key in layout.ids:
                layout.ids[key].text = str(value)
        return layout.to_string()

    def generate_default_html(self, listing_data):
        title = listing_data.get('title', '')
        description = listing_data.get('description', '')
        price = listing_data.get('price', '')

        # Modello HTML predefinito con segnaposto
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}</h1>
            <p>{description}</p>
            <p>Price: ${price}</p>
        </body>
        </html>
        """

        return html_template.format(title=title, description=description, price=price)
