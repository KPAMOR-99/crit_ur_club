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

# Expanded and adjusted positions (11 per club)
POSITIONS = ["GK", "CBL", "CBR", "LB", "RB", "DM", "CM", "AM", "LW", "RW", "ST"]
FORM_CHARS = ['W', 'D', 'L']

# Expanded name pool for uniqueness
FIRST_NAMES = ["James", "John", "Michael", "David", "Chris", "Ryan", "Daniel", "Tom", "Robert", "Luke"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Davis", "Miller", "Wilson", "Taylor", "Clark"]

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_form():
    return ''.join(random.choices(FORM_CHARS, k=5))

def generate_fixtures():
    data = []
    player_count = 0

    for club_name in CLUBS:
        # Generate unique owner
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

        # Generate unique manager
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

        # Generate club
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

        # Generate 11 players, 1 per position
        used_names = set()
        for i, position in enumerate(POSITIONS):
            while True:
                base_name = random_name()
                player_name = f"{base_name} ({club_name})"
                if player_name not in used_names:
                    used_names.add(player_name)
                    break

            player_count += 1
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

    # Save fixtures
    with open("clubs/fixtures/initial_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f" Fixture file generated with:")
    print(f"  - {len(CLUBS)} Clubs")
    print(f"  - {len(CLUBS)} Managers")
    print(f"  - {len(CLUBS)} Owners")
    print(f"  - {player_count} Players")

if __name__ == "__main__":
    generate_fixtures()
