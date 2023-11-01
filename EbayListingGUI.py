import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooser

class EbayListingGUI(BoxLayout):
    def __init__(self, data_handler, html_generator, **kwargs):
        super().__init__(**kwargs)
        self.data_handler = data_handler
        self.html_generator = html_generator

    def submit(self):
        username = self.ids.username_input.text
        title = self.ids.title_input.text

        listing_data = {
            'username': username,
            'title': title,
            # Add other data
        }

        is_valid, error_message = self.data_handler.validate(listing_data)

        if is_valid:
            html = self.html_generator.generate(listing_data)
            print("eBay Listing Created!")
        else:
            print("Validation Error: {}".format(error_message))

class EbayListingApp(App):
    def __init__(self, data_handler, html_generator, **kwargs):
        super().__init__(**kwargs)
        self.data_handler = data_handler
        self.html_generator = html_generator
        self.custom_layout = None  # Store the loaded custom layout here

    def build(self):
        layout = EbayListingGUI(self.data_handler, self.html_generator)
        menu = self.create_settings_menu(layout)
        layout.add_widget(menu)
        return layout

    def create_settings_menu(self, layout):
        menu = DropDown()
        load_layout_button = Button(text='Load Layout')
        load_layout_button.bind(on_release=self.load_custom_layout)
        menu.add_widget(load_layout_button)

        settings_button = Spinner(text='Settings', values=['Load Layout'])
        settings_button.bind(on_release=menu.open)
        menu.bind(on_select=self.menu_option_selected)

        return settings_button

    def load_custom_layout(self, instance):
        file_chooser = FileChooser(on_selection=self.load_selected_layout)
        file_chooser.popup()

    def load_selected_layout(self, selected_file):
        if selected_file:
            # Implement logic to load the selected layout file
            # For example: self.custom_layout = load_layout(selected_file)
            # You may need to handle errors and provide user feedback

          def menu_option_selected(self, instance, value):
           if value == 'Load Layout':
            self.load_custom_layout(instance)
        else:
            # Handle other settings options if needed
            pass

if __name__ == '__main__':
    Builder.load_file('layout.kv')
    data_handler = EbayListingData()
    html_generator = EbayHTMLGenerator()
    app = EbayListingApp(data_handler, html_generator)
    app.run()
