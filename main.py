from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivymd.app import MDApp
from kivy.uix.image import Image
import random
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton

Window.clearcolor = (0, 1, 1, 1)

KV = '''
ScreenManager:
    HomeScreen:
    MainScreen:

<HomeScreen>:
    name: 'home'
    welcome_label: welcome_label

    FloatLayout:
        Image:
            source: 'background.jpg'  # Set your game background image here
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)  # Full screen
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20

            MDLabel:
                id: welcome_label
                text: "FUN TIME"
                halign: 'center'
                font_style: 'H3'
                bold: True
                italic: True

            MDFillRoundFlatButton:
                text:"Let's Play"
                size_hint_x: 0.3
                _default_md_bg_color: (0/255,99/255,255/255,1)
                bold: True
                pos_hint: {"center_x": 0.8}
                on_release: app.go_next()

<MainScreen>:
    name: 'main'
    result_label: result_label
    score_label: score_label
    player_image: player_image
    computer_image: computer_image

    # Background Image
    FloatLayout:
        Image:
            source: 'game_background.jpg'  # Set your game background image here
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)  # Full screen
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20

            MDRaisedButton:
                text: "Back"
                pos_hint: {"center_x": 0.09}
                _default_md_bg_color: (62/255,182/255,214/255,1)
                on_release: app.go_back()

            MDRaisedButton:
                text: "Reset"
                pos_hint: {"center_x": 0.9}
                _default_md_bg_color: (62/255,182/255,214/255,1)
                on_release: app.reset()

            # Score Label at the top
            MDLabel:
                id: score_label
                text: "Player: 0  |  Computer: 0"
                halign: 'center'
                font_style: 'H6'

            # Images for player and computer choices
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 20
                size_hint_y: None
                height: dp(150)
                padding: dp(10)

                Image:
                    id: player_image
                    source: 'game_background.jpg'  # Initial placeholder image
                    allow_stretch: True

                Image:
                    id: computer_image
                    source: 'game_background.jpg'  # Initial placeholder image
                    allow_stretch: True

            # Result Label in the middle
            MDLabel:
                id: result_label
                text: "Make Your Move!"
                halign: 'center'
                font_style: 'H4'

            # Buttons at the bottom
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: 10
                size_hint_y: None
                height: dp(60)
                padding: dp(10)
                pos_hint: {"center_x": 0.5, "y": 0.05}  # Position the buttons at the bottom

                MDFillRoundFlatButton:
                    text: "Stone"
                    on_release: app.player_move("stone")
                    _default_md_bg_color: (165/255,54/255,255/255,1)
                    size_hint_x: 1  # Buttons take equal space
                MDFillRoundFlatButton:
                    text: "Paper"
                    on_release: app.player_move("paper")
                    _default_md_bg_color: (165/255,54/255,255/255,1)
                    size_hint_x: 1
                MDFillRoundFlatButton:
                    text: "Scissors"
                    on_release: app.player_move("scissors")
                    _default_md_bg_color: (165/255,54/255,255/255,1)
                    size_hint_x: 1
'''

class HomeScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class Smart_Kids_GAME(MDApp):
    player_score = 0
    computer_score = 0
    images = {
        "stone": "stone.png",
        "paper": "paper.png",
        "scissors": "scissors.png"
    }

    images_com = {
        "stone": "stone.png",
        "paper": "paper.png",
        "scissors": "scissors.png"
    }

    def build(self):
        return Builder.load_string(KV)

    def player_move(self, move):
        computer_move = random.choice(["stone", "paper", "scissors"])
        result = self.determine_winner(move, computer_move)
        self.update_score(result)

        # Update images for player and computer
        self.root.get_screen('main').ids.player_image.source = self.images[move]
        self.root.get_screen('main').ids.computer_image.source = self.images_com[computer_move]

        # Update result text
        self.root.get_screen('main').ids.result_label.text = f"{result}!"
        self.root.get_screen('main').ids.score_label.text = f"Player: {self.player_score}  |  Computer: {self.computer_score}"

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie"
        elif (player == "stone" and computer == "scissors") or \
             (player == "paper" and computer == "stone") or \
             (player == "scissors" and computer == "paper"):
            return "You win"
        else:
            return "You lose"

    def update_score(self, result):
        if result == "You win":
            self.player_score += 1
        elif result == "You lose":
            self.computer_score += 1

    def go_next(self):
        # Set the transition type and duration
        self.root.transition = SwapTransition(duration=0.5)
        # Switch to the main screen
        self.root.current = 'main'
        
    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.root.get_screen('main').ids.score_label.text = f"Player: 0  |  Computer: 0"
        self.root.get_screen('main').ids.result_label.text = " "
        self.root.get_screen('main').ids.player_image.source = 'game_background.jpg'
        self.root.get_screen('main').ids.computer_image.source = 'game_background.jpg'

    def go_back(self):
        self.root.transition = SwapTransition(duration=0.5)
        self.root.current = 'home'

if __name__ == '__main__':
    Smart_Kids_GAME().run()
