"""
python match/e1.py
Match function examples
"""

inp = input("Enter your Favourite anime name and Best character in the specified sequence only:")
x,y = inp.upper().split("AND")

x=x.strip()
y=y.strip()

List_ofFavouriteAnime = []
List_ofFavouriteAnime.append(x)
List_ofFavouriteAnime.append(y)

user_response = int(input("Choose your option from 1 or 2:"))
match(user_response):
    case 1:
        print(f"Anime Name:{x} ,Best Character:{y}")

    case 2:
        print("Don't have any favourite character??No problem!")

