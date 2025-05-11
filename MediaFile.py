from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self, filename, filesize):
        self.filename = filename
        self.filesize = filesize

    def get_size(self):
        return self.filesize

    def open_file(self):
        print(f"Opening file: {self.filename}")

    @abstractmethod
    def operate(self):
        pass

class AudioFile(MediaFile):
    def __init__(self, filename, filesize, artist, duration):
        super().__init__(filename, filesize)
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing audio file '{self.filename}' by {self.artist}.")

    def set_volume(self, volume):
        print(f"Volume set to {volume}.")

    def operate(self):
        self.play()

class VideoFile(MediaFile):
    def __init__(self, filename, filesize, resolution, duration):
        super().__init__(filename, filesize)
        self.resolution = resolution
        self.duration = duration

    def play(self):
        print(f"Playing video file '{self.filename}' at {self.resolution} resolution.")

    def add_subtitles(self):
        print("Subtitles added to video.")

    def operate(self):
        self.play()

class ImageFile(MediaFile):
    def __init__(self, filename, filesize, width, height):
        super().__init__(filename, filesize)
        self.width = width
        self.height = height

    def view(self):
        print(f"Viewing image '{self.filename}' with size {self.width}x{self.height}.")

    def resize(self):
        print("Image has been resized.")

    def operate(self):
        self.view()

class HypermediaFile(MediaFile):
    def __init__(self, filename, filesize, interactivity_level, user_inputs):
        super().__init__(filename, filesize)
        self.interactivity_level = interactivity_level
        self.user_inputs = user_inputs

    def start_interaction(self):
        print(f"Starting interaction at {self.interactivity_level} level.")

    def show_feedback(self):
        return "Feedback shown based on user input."

    def operate(self):
        self.start_interaction()

if __name__ == "__main__":
    audio = AudioFile("song.mp3", 5000, "Doja Cat", 210)
    video = VideoFile("vlog.mp4", 200000, "4K", 900)
    image = ImageFile("meme.jpg", 1024, "1080", "720")
    hypermedia = HypermediaFile("game.html", 15000, "High", ["click", "hover"])

    audio.operate()
    audio.set_volume(80)

    video.operate()
    video.add_subtitles()

    image.operate()
    image.resize()

    hypermedia.operate()
    print(hypermedia.show_feedback())
