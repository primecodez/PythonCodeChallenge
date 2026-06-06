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

    if isinstance(item,int):
        return item

    total = 0

    for value in item.values():
        total += calculate_size(value)

    return total

print(f"Total size : {calculate_size(folders)} MB")