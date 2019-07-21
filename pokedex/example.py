import argparse
import json

import tabulate

with open("pokedex/data/id_to_pokemon.json", "r") as f:
    pokemon_by_id = json.load(f)

with open("pokedex/data/name_to_pokemon.json", "r") as f:
    pokemon_by_name = json.load(f)


def search(input, name=True) -> dict:
    if name:
        return pokemon_by_name.get(input.lower(), f"no pokemon for name: {input}")
    return pokemon_by_id.get(input, f"no pokemon for id: {input}")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="search input")
    parser.add_argument("--name", help="search by name instead of ID", action="store_true")

    args = parser.parse_args()
    pokemon = search(args.input, args.name)
    heaers = ["id", "name", "type", "weakness", "evolution"]
    table = tabulate.tabulate([[v for v in pokemon.values()]], headers=heaers)
    print(table)


if __name__ == '__main__':
    run()
