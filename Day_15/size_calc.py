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
    """Recursively calculates total size of files in a folder."""

    if isinstance(item, int):
        return item

    if not isinstance(item, dict):
        raise TypeError("Invalid file size")

    total = 0

    for value in item.values():
        total += calculate_size(value)

    return total

print(f"Movies -> {calculate_size(folders['Movies'])}")
print(f"Minecraft -> {calculate_size(folders['Games']['Minecraft'])}")
print(f"Valorant -> {calculate_size(folders['Games']['Valorant'])}")
print(f"Games -> {calculate_size(folders['Games'])}")
print(f"Total size -> {calculate_size(folders)} MB")