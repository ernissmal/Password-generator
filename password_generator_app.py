from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDRaisedButton
from kivy.properties import StringProperty
from kivy.metrics import dp
from password_generator import (
    generate_password,
    generate_memorable_password,
    generate_hex_password,
    generate_base64_password,
    generate_pronounceable_password,
    generate_pin,
    generate_alphanumeric_password
)
from database import save_password, get_passwords

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    MDRaisedButton:
        id: algorithm_spinner
        text: 'Select Algorithm'
        pos_hint: {'center_x': .5}
        on_release: app.menu_algorithms.open()

    MDTextField:
        id: length_input
        hint_text: 'Password Length'
        text: '12'
        size_hint_x: None
        width: 200
        pos_hint: {'center_x': .5}

    MDRaisedButton:
        id: uppercase_spinner
        text: 'Include Uppercase'
        pos_hint: {'center_x': .5}
        on_release: app.menu_uppercase.open()

    MDRaisedButton:
        id: digits_spinner
        text: 'Include Digits'
        pos_hint: {'center_x': .5}
        on_release: app.menu_digits.open()

    MDRaisedButton:
        id: symbols_spinner
        text: 'Include Symbols'
        pos_hint: {'center_x': .5}
        on_release: app.menu_symbols.open()

    MDTextField:
        id: name_input
        hint_text: 'Password Name'
        size_hint_x: None
        width: 200
        pos_hint: {'center_x': .5}

    MDRaisedButton:
        text: 'Generate Password'
        on_press: app.generate_password()
        pos_hint: {'center_x': .5}

    MDTextField:
        id: password_output
        hint_text: 'Generated Password'
        readonly: True
        size_hint_x: None
        width: 200
        pos_hint: {'center_x': .5}

    MDRaisedButton:
        text: 'Save Password'
        on_press: app.save_password()
        pos_hint: {'center_x': .5}

    MDRaisedButton:
        text: 'View Saved Passwords'
        on_press: app.view_passwords()
        pos_hint: {'center_x': .5}

    MDScrollView:
        MDList:
            id: saved_passwords_list
'''

class PasswordGeneratorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.menu_algorithms = MDDropdownMenu(
            caller=self.root.ids.algorithm_spinner,
            items=[
                {"viewclass": "OneLineListItem", "text": "Random Characters", "on_release": lambda x="Random Characters": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "Memorable Words", "on_release": lambda x="Memorable Words": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "Hexadecimal", "on_release": lambda x="Hexadecimal": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "Base64", "on_release": lambda x="Base64": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "Pronounceable", "on_release": lambda x="Pronounceable": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "PIN", "on_release": lambda x="PIN": self.set_item(x, 'algorithm_spinner')},
                {"viewclass": "OneLineListItem", "text": "Alphanumeric", "on_release": lambda x="Alphanumeric": self.set_item(x, 'algorithm_spinner')}
            ],
            width_mult=4
        )

        self.menu_uppercase = MDDropdownMenu(
            caller=self.root.ids.uppercase_spinner,
            items=[
                {"viewclass": "OneLineListItem", "text": "Yes", "on_release": lambda x="Yes": self.set_item(x, 'uppercase_spinner')},
                {"viewclass": "OneLineListItem", "text": "No", "on_release": lambda x="No": self.set_item(x, 'uppercase_spinner')}
            ],
            width_mult=2
        )

        self.menu_digits = MDDropdownMenu(
            caller=self.root.ids.digits_spinner,
            items=[
                {"viewclass": "OneLineListItem", "text": "Yes", "on_release": lambda x="Yes": self.set_item(x, 'digits_spinner')},
                {"viewclass": "OneLineListItem", "text": "No", "on_release": lambda x="No": self.set_item(x, 'digits_spinner')}
            ],
            width_mult=2
        )

        self.menu_symbols = MDDropdownMenu(
            caller=self.root.ids.symbols_spinner,
            items=[
                {"viewclass": "OneLineListItem", "text": "Yes", "on_release": lambda x="Yes": self.set_item(x, 'symbols_spinner')},
                {"viewclass": "OneLineListItem", "text": "No", "on_release": lambda x="No": self.set_item(x, 'symbols_spinner')}
            ],
            width_mult=2
        )

    def set_item(self, text_item, spinner_id):
        self.root.ids[spinner_id].text = text_item
        if spinner_id == 'algorithm_spinner':
            self.menu_algorithms.dismiss()
        elif spinner_id == 'uppercase_spinner':
            self.menu_uppercase.dismiss()
        elif spinner_id == 'digits_spinner':
            self.menu_digits.dismiss()
        elif spinner_id == 'symbols_spinner':
            self.menu_symbols.dismiss()

    def generate_password(self):
        try:
            length = int(self.root.ids.length_input.text)
        except ValueError:
            self.root.ids.password_output.text = "Invalid length."
            return

        algorithm = self.root.ids.algorithm_spinner.text
        include_uppercase = self.root.ids.uppercase_spinner.text == 'Yes'
        include_digits = self.root.ids.digits_spinner.text == 'Yes'
        include_symbols = self.root.ids.symbols_spinner.text == 'Yes'

        try:
            if algorithm == 'Random Characters':
                password = generate_password(length, include_uppercase, include_digits, include_symbols)
            elif algorithm == 'Memorable Words':
                words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
                password = generate_memorable_password(words_list, num_words=length // 4)
            elif algorithm == 'Hexadecimal':
                password = generate_hex_password(length)
            elif algorithm == 'Base64':
                password = generate_base64_password(length)
            elif algorithm == 'Pronounceable':
                password = generate_pronounceable_password(length)
            elif algorithm == 'PIN':
                password = generate_pin(length)
            elif algorithm == 'Alphanumeric':
                password = generate_alphanumeric_password(length)
            else:
                self.root.ids.password_output.text = "Invalid algorithm selected."
                return
        except Exception as e:
            self.root.ids.password_output.text = str(e)
            return

        self.root.ids.password_output.text = password

    def save_password(self):
        name = self.root.ids.name_input.text
        password = self.root.ids.password_output.text
        if not name or not password:
            self.root.ids.password_output.text = "Enter a name and generate a password first."
            return
        save_password(name, password)
        self.root.ids.password_output.text = "Password saved successfully."

    def view_passwords(self):
        self.root.ids.saved_passwords_list.clear_widgets()
        passwords = get_passwords()
        for name, password in passwords:
            self.root.ids.saved_passwords_list.add_widget(OneLineListItem(text=f"{name}: {password}"))

if __name__ == '__main__':
    PasswordGeneratorApp().run()
