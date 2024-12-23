import requests

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)

def fetch_pokemon_data(pokemon_name):
    """Fetch Pokémon data from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data for {pokemon_name}. HTTP Status Code: {response.status_code}")

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    try:
        # Fetch Pokémon data
        data1 = fetch_pokemon_data(pokemon1)
        data2 = fetch_pokemon_data(pokemon2)

        # Extract base stats
        stats1 = {stat['stat']['name']: stat['base_stat'] for stat in data1['stats']}
        stats2 = {stat['stat']['name']: stat['base_stat'] for stat in data2['stats']}

        # Calculate initial stats
        p1_stats = {
            'hp': calculate_hp(stats1['hp']),
            'attack': calculate_stat(stats1['attack']),
            'defense': calculate_stat(stats1['defense']),
            'speed': calculate_stat(stats1['speed'])
        }
        p2_stats = {
            'hp': calculate_hp(stats2['hp']),
            'attack': calculate_stat(stats2['attack']),
            'defense': calculate_stat(stats2['defense']),
            'speed': calculate_stat(stats2['speed'])
        }

        # Initialize battle display
        print(f"A wild battle between {pokemon1.capitalize()} and {pokemon2.capitalize()} begins!")
        print(f"{pokemon1.capitalize()} HP: {p1_stats['hp']}")
        print(f"{pokemon2.capitalize()} HP: {p2_stats['hp']}")

        # Determine first attacker
        if p1_stats['speed'] > p2_stats['speed']:
            attacker, defender = pokemon1, pokemon2
            attacker_stats, defender_stats = p1_stats, p2_stats
        else:
            attacker, defender = pokemon2, pokemon1
            attacker_stats, defender_stats = p2_stats, p1_stats

        # Battle loop
        round_number = 1
        while p1_stats['hp'] > 0 and p2_stats['hp'] > 0:
            print(f"\n--- Round {round_number} ---")
            damage = calculate_damage(attacker_stats, defender_stats)
            defender_stats['hp'] -= damage
            print(f"{attacker.capitalize()} attacks {defender.capitalize()} for {damage} damage!")
            print(f"{defender.capitalize()} HP: {max(0, defender_stats['hp'])}")

            # Check if defender fainted
            if defender_stats['hp'] <= 0:
                print(f"\n{defender.capitalize()} has fainted! {attacker.capitalize()} wins!")
                break

            # Swap roles
            attacker, defender = defender, attacker
            attacker_stats, defender_stats = defender_stats, attacker_stats

            round_number += 1

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    simulate_battle("pikachu", "bulbasaur")
