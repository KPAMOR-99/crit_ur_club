import json
import random
from django.utils.text import slugify

# Constants
CLUBS = [
    "Arsenal", "Manchester United", "Manchester City", "Chelsea", "Liverpool",
    "Tottenham Hotspur", "Newcastle United", "Aston Villa", "West Ham United", 
    "Brighton & Hove Albion", "Brentford", "Wolverhampton Wanderers", 
    "Crystal Palace", "Fulham", "Everton", "Nottingham Forest", 
    "Bournemouth", "Burnley", "Luton Town", "Sheffield United"
]

POSITIONS = ["GK", "CB", "LB", "RB", "DM", "CM", "AM", "LW", "RW", "ST", "CF"]
NATIONALITIES = ["England", "Spain", "France", "Germany", "Brazil", "Argentina", 
                "Portugal", "Netherlands", "Italy", "Belgium"]
FORM_CHARS = ['W', 'D', 'L']

# Name generation with football-appropriate names
FIRST_NAMES = {
    "English": ["Harry", "Jack", "Phil", "Jordan", "Kyle", "Marcus", "Declan", "Jude"],
    "Spanish": ["Javier", "Sergio", "David", "Carlos", "Juan", "Pedro", "Diego"],
    "French": ["Kylian", "Antoine", "Paul", "N'Golo", "Olivier", "Hugo"],
    "Brazilian": ["Neymar", "Vinicius", "Casemiro", "Alisson", "Gabriel", "Richarlison"]
}
LAST_NAMES = {
    "English": ["Kane", "Henderson", "Rice", "Bellingham", "Walker", "Shaw"],
    "Spanish": ["Ramos", "Busquets", "Alba", "Torres", "Gavi", "Pedri"],
    "French": ["Mbappé", "Griezmann", "Pogba", "Kanté", "Giroud", "Lloris"],
    "Brazilian": ["Junior", "Silva", "Santos", "Jesus", "Firmino", "Rodrygo"]
}

def random_name(nationality):
    """Generate realistic football names based on nationality"""
    nationality_group = "English" if nationality == "England" else nationality
    first = random.choice(FIRST_NAMES.get(nationality_group, FIRST_NAMES["English"]))
    last = random.choice(LAST_NAMES.get(nationality_group, LAST_NAMES["English"]))
    return f"{first} {last}"

def random_form():
    """Generate recent form string (e.g., WWDLW)"""
    return ''.join(random.choices(FORM_CHARS, weights=[5, 3, 2], k=5))

def generate_players(club, nationality, count=11):
    """Generate realistic squad with balanced positions"""
    players = []
    positions = POSITIONS.copy()
    
    # Ensure at least 1 goalkeeper
    players.append({
        "model": "clubs.player",
        "fields": {
            "name": random_name(nationality) + " (GK)",
            "age": random.randint(18, 35),
            "position": "GK",
            "avr_rating": round(random.uniform(6.0, 7.5), 1),
           # "form": random_form(),
            "club": club["fields"]["name"]
        }
    })
    
    # Generate remaining players with position distribution
    for i in range(count - 1):
        position = random.choice(positions)
        if position == "GK":  # Already have our GK
            position = random.choice([p for p in positions if p != "GK"])
            
        players.append({
            "model": "clubs.player",
            "fields": {
                "name": random_name(nationality) + f" ({position})",
                "age": random.randint(18, 35),
                "position": position,
                "avr_rating": round(random.uniform(6.0, 9.0), 1),
               # "form": random_form(),
                "club": club["fields"]["name"]
            }
        })
    return players

def main():
    fixture = []
    
    for club_name in CLUBS:
        # Generate consistent nationality for club's staff/players
        nationality = random.choice(NATIONALITIES)
        
        # Owner
        owner = {
            "model": "clubs.owner",
            "fields": {
                "name": f"{random_name(nationality)} (Owner)",
                "age": random.randint(45, 75),
               # "nationality": nationality
            }
        }
        fixture.append(owner)
        
        # Manager
        manager = {
            "model": "clubs.manager",
            "fields": {
                "name": random_name(nationality) + " (Manager)",
                "age": random.randint(35, 65),
               
                "nationality": nationality,
                "matches_played": random.randint(50, 500),
                
            }
        }
        fixture.append(manager)
        
        # Club
        club = {
            "model": "clubs.club",
            "fields": {
                "name": club_name,
                "slug": slugify(club_name),
                "manager": manager["fields"]["name"],
                "owner": owner["fields"]["name"],
                "form": random_form()
                
            }
        }
        fixture.append(club)
        
        # Players
        fixture.extend(generate_players(club, nationality))
    
    # Save to JSON
    with open('clubs/fixtures/initial_data.json', 'w') as f:
        json.dump(fixture, f, indent=2)
    
    print(f" Generated fixture with:")
    print(f"- {len(CLUBS)} clubs")
    print(f"- {len(CLUBS)} owners")
    print(f"- {len(CLUBS)} managers")
    print(f"- {len(CLUBS)*11} players")

if __name__ == "__main__":
    main()