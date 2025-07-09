import json
import random
from django.utils.text import slugify

# List of clubs
CLUBS = [
    "Arsenal", "Manchester United", "Manchester City", "Chelsea", "Liverpool",
    "Tottenham", "Newcastle", "Aston Villa", "West Ham", "Brighton",
    "Brentford", "Wolves", "Crystal Palace", "Fulham", "Everton",
    "Nottingham Forest", "Bournemouth", "Burnley", "Luton Town", "Sheffield"
]

# Exactly 11 positions per club
POSITIONS = ["GK", "CBL", "CBR", "LB", "RB", "DM", "CM", "AM", "LW", "RW", "ST"]
FORM_CHARS = ['W', 'D', 'L']

# Expanded name pools for uniqueness (20 x 20 = 400 unique combinations)
FIRST_NAMES = [
    "James", "John", "Michael", "David", "Chris", "Ryan", "Daniel", "Tom", "Robert", "Luke",
    "Henry", "George", "Leo", "Nathan", "Sam", "Victor", "Anthony", "Jason", "Oliver", "Elijah"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Davis", "Miller", "Wilson", "Taylor", "Clark",
    "Young", "Lewis", "Walker", "Hall", "Allen", "Wright", "King", "Scott", "Mitchell", "Bennett"
]

# Pre-generate all unique names
name_pool = [f"{first} {last}" for first in FIRST_NAMES for last in LAST_NAMES]
random.shuffle(name_pool)
name_index = 0

def random_name():
    global name_index
    name = name_pool[name_index]
    name_index += 1
    return name

def random_form():
    return ''.join(random.choices(FORM_CHARS, k=5))

def generate_fixtures():
    data = []
    player_count = 0

    for club_name in CLUBS:
        # Create unique owner name per club
        owner_name = f"{random_name()} (Owner of {club_name})"
        owner = {
            "model": "clubs.owner",
            "pk": owner_name,
            "fields": {
                "age": random.randint(45, 75),
                "slug": slugify(owner_name)
            }
        }
        data.append(owner)

        # Create unique manager name per club
        manager_name = f"{random_name()} (Manager of {club_name})"
        manager = {
            "model": "clubs.manager",
            "pk": manager_name,
            "fields": {
                "age": random.randint(35, 65),
                "nationality": "England",
                "matches_played": random.randint(50, 300),
                "slug": slugify(manager_name)
            }
        }
        data.append(manager)

        # Create the club
        club = {
            "model": "clubs.club",
            "pk": club_name,
            "fields": {
                "slug": slugify(club_name),
                "manager": manager_name,
                "owner": owner_name,
                "form": random_form()
            }
        }
        data.append(club)

        # 11 unique players per club (1 per position)
        for position in POSITIONS:
            base_name = random_name()
            player_name = f"{base_name} ({position} of {club_name})"
            player = {
                "model": "clubs.player",
                "pk": player_name,
                "fields": {
                    "age": random.randint(18, 35),
                    "position": position,
                    "avr_rating": round(random.uniform(6.0, 9.0), 1),
                    "club": club_name,
                    "slug": slugify(player_name)
                }
            }
            data.append(player)
            player_count += 1

    # Save to fixture file
    with open("clubs/fixtures/initial_data.json", "w") as f:
        json.dump(data, f, indent=2)

    # Summary printout
    print("✅ Fixture file generated with:")
    print(f"  - {len(CLUBS)} Clubs")
    print(f"  - {len(CLUBS)} Managers")
    print(f"  - {len(CLUBS)} Owners")
    print(f"  - {player_count} Players")

if __name__ == "__main__":
    generate_fixtures()
