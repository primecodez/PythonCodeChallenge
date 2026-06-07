#Modify the program so it  prints:

"""Movies -> 2700 MB
Minecraft -> 500 MB
Valorant -> 5000 MB
Games -> 5500 MB
Total -> 8205 MB"""


folders = {
    "Movies": {
        "Avengers.mp4": 1500,
        "Batman.mp4": 1200
    },

    "Games": {
        "Minecraft": {
            "panda.dat": 200,
            "onepiece.dat": 300
        },

        "Valorant": {
            "game.exe": 5000
        }
    },

    "Notes.txt": 5
}

def calculate_size(item):
    if isinstance(item, int):
        return item

    if isinstance(item, dict):
        return sum(calculate_size(value) for value in item.values())

    raise TypeError("Invalid file size")

    
def print_sizes(folder, name="Root"):
    print(f"{name} -> {calculate_size(folder)} MB")

    for key, value in folder.items():
        if isinstance(value, dict):
            print_sizes(value, key)

print_sizes(folders)