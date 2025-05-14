from abc import ABC, abstractmethod
import random

class MediaFile(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.is_favorite = False

    def add_to_favorites(self):
        self.is_favorite = True
        print("✅ Added to favorites.")

    def open_file(self):
        print(f"📂 Opening '{self.filename}'...")

    @abstractmethod
    def operate(self):
        pass


class AudioFile(MediaFile):
    def __init__(self, filename, artist, duration):
        super().__init__(filename)
        self.artist = artist
        self.duration = duration
        self.volume = 50

    def set_volume(self, volume):
        self.volume = volume
        print(f"🔊 Volume set to {self.volume}")

    def play(self):
        print(f"🎵  ▶︎ •၊၊||၊|။||||  Now playing '{self.filename}' by {self.artist} [{self.duration} sec] at volume {self.volume}")

    def operate(self):
        self.play()


class VideoFile(MediaFile):
    def __init__(self, filename, resolution, duration):
        super().__init__(filename)
        self.resolution = resolution
        self.duration = duration

    def play(self):
        print(f"🎬 Playing video '{self.filename}' at {self.resolution} resolution [{self.duration} sec]")

    def add_subtitles(self):
        print("💬 Subtitles added.")

    def operate(self):
        self.play()


class ImageFile(MediaFile):
    def __init__(self, filename, width, height):
        super().__init__(filename)
        self.width = width
        self.height = height

    def view(self):
        print(f"🖼️ Viewing image '{self.filename}' ({self.width}x{self.height})")

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        print(f"📏 Image resized to {self.width}x{self.height}.")

    def operate(self):
        self.view()


class HypermediaFile(MediaFile):
    def __init__(self, filename, interactivity_level):
        super().__init__(filename)
        self.interactivity_level = interactivity_level

    def start_interaction(self):
        if self.filename.lower() == "tic-tac-toe":
            print("🎮 Starting Tic-Tac-Toe")
            self.play_tic_tac_toe()
        elif self.filename.lower() == "rock-paper-scissors":
            print("🎮 Starting Rock-Paper-Scissors")
            self.play_rps()
        else:
            print("❌ Invalid game selected.")

    def play_tic_tac_toe(self):
        board = [" "] * 9

        def print_board():
            print("\n")
            for i in range(0, 9, 3):
                print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
                if i < 6:
                    print("---|---|---")
            print()

        def check_win(player):
            wins = [(0,1,2),(3,4,5),(6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8),(2,4,6)]
            return any(all(board[i] == player for i in line) for line in wins)

        current = "X"
        for turn in range(9):
            print_board()
            try:
                move = int(input(f"Player {current}, choose a cell (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("❌ Invalid move. Try again.")
                    continue
            except:
                print("❌ Invalid input. Enter a number between 1 and 9.")
                continue
            board[move] = current
            if check_win(current):
                print_board()
                print(f"🏆 Player {current} wins!")
                return
            current = "O" if current == "X" else "X"
        print_board()
        print("🤝 It's a draw!")

    def play_rps(self):
        options = ['rock', 'paper', 'scissors']
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in options:
            print("❌ Invalid choice.")
            return
        comp = random.choice(options)
        print(f"🧠 Computer chose: {comp}")
        if user == comp:
            print("🤝 It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("🏆 You win!")
        else:
            print("💻 Computer wins!")

    def show_feedback(self):
        return f"✅ Feedback: You just played a game inside '{self.filename}' on {self.interactivity_level} mode!"

    def operate(self):
        self.start_interaction()


def ask_to_favorite(media_file):
    print("\n⭐ Would you like to add this file to favorites?")
    print("Type 'yes' or 'no')")
    choice = input("Your choice: ").lower()
    if choice == 'yes':
        media_file.add_to_favorites()
    elif choice == 'no':
        print("ℹ️ File was not added to favorites.")
    else:
        print("❌ Invalid input. File was not added to favorites.")


def run_program():
    while True:
        print("\n🎉 Welcome to MediaVerse: Media File Simulator!")
        print("Choose a media type:")
        print("1. Audio\n2. Video\n3. Image\n4. Hypermedia\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            filename = input("Enter audio filename: ")
            artist = input("Enter artist: ")
            duration = int(input("Enter duration (in seconds): "))
            audio = AudioFile(filename, artist, duration)
            volume = int(input("Set volume (0–100): "))
            audio.set_volume(volume)
            audio.open_file()
            audio.operate()
            ask_to_favorite(audio)

        elif choice == '2':
            filename = input("Enter video filename: ")
            valid_resolutions = ['1080p', '720p', '2K', '4K']
            print("Available resolutions: 1080p, 720p, 2K, 4K")
            resolution = input("Enter resolution: ")
            if resolution not in valid_resolutions:
                print("❌ Invalid resolution. Please choose from: 1080p, 720p, 2K, 4K")
                continue
            duration = int(input("Enter duration (in seconds): "))
            video = VideoFile(filename, resolution, duration)
            video.open_file()
            video.operate()
            if input("Add subtitles? (yes/no): ").lower() == 'yes':
                video.add_subtitles()
            ask_to_favorite(video)

        elif choice == '3':
            filename = input("Enter image filename: ")
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            image = ImageFile(filename, width, height)
            image.open_file()
            image.operate()
            if input("Resize image? (yes/no): ").lower() == 'yes':
                new_width = int(input("Enter new width: "))
                new_height = int(input("Enter new height: "))
                image.resize(new_width, new_height)
            ask_to_favorite(image)

        elif choice == '4':
            print("📂 Available hypermedia file: Game (Tic-Tac-Toe, Rock-Paper-Scissors)")
            filename = input("Enter hypermedia filename: ")
            if filename.lower() not in ["tic-tac-toe", "rock-paper-scissors"]:
                print("❌ Invalid game. Please choose either 'Tic-Tac-Toe' or 'Rock-Paper-Scissors'.")
                continue
            level = input("Enter interactivity level (Easy/Medium/Hard): ")
            hyper = HypermediaFile(filename, level)
            hyper.open_file()
            hyper.operate()
            print(hyper.show_feedback())
            ask_to_favorite(hyper)

        elif choice == '5':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid input. Please try again.")

if __name__ == "__main__":
    run_program()
