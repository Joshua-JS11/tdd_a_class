class Music_list:

    def __init__(self):
        self.music_list = []

    def add_track(self, track_artist:str, track_name:str):
        self.music_list.append(f"{track_artist}: {track_name}")

    def track_list(self):
        return self.music_list