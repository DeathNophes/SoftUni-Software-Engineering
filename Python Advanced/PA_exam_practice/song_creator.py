def add_songs(*args):
    result = ""
    my_songs = {}

    for song_name, lyrics in args:
        if song_name not in my_songs.keys():
            my_songs[song_name] = []
        if lyrics:
            for line in lyrics:
                my_songs[song_name].append(line)

    for song, lyrics_list in my_songs.items():
        result += f"- {song}\n"
        for line in lyrics_list:
            result += f"{line}\n"

    return result
