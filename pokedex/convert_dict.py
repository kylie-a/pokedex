import json
from typing import Any, Dict

from pokedex import pokemon


def do_weakness_type(new_k: str, pkmn: Dict[str, Any], v: str) -> Dict[str, Any]:
    pkmn[new_k] = [p.lower() for p in v.split("/")]
    return pkmn


def get_next_pkmn(key: str) -> Dict[str, Any]:
    next_key = str(int(key) + 1)
    return pokemon.get(next_key)


def do_evolution(pkmn_id: str, pkmn: Dict[str, Any], evo: str) -> Dict[str, Any]:
    next_key = str(int(pkmn_id) + 1)
    new_key = "evolution"
    next_pkmn = get_next_pkmn(pkmn_id)

    if next_pkmn is not None:
        if evo == "First Evolution" and pokemon[str(int(pkmn_id) + 1)]["Evolution"] == "Second Evolution":
            new_pkmn[new_key] = {"name": next_pkmn["Name"].lower(), "id": next_key}
        elif evo == "Second Evolution" and pokemon[str(int(pkmn_id) + 1)]["Evolution"] == "Third Evolution":
            new_pkmn[new_key] = {"name": next_pkmn["Name"].lower(), "id": next_key}
        else:
            new_pkmn[new_key] = {"name": "", "id": None}
    else:
        new_pkmn[new_key] = {"name": "", "id": None}
    return pkmn


def do_name(name: str, pkmn:  Dict[str, Any]) ->  Dict[str, Any]:
    pkmn["name"] = name.lower()
    return pkmn


if __name__ == '__main__':
    name_to_pokemon = {}
    id_to_pokemon = {}
    for pkmn_id, pkmn in pokemon.items():
        new_pkmn = {"id": pkmn_id}
        for k, v in pkmn.items():
            new_k = k.lower()
            if new_k in {"weakness", "type"}:
                new_pkmn = do_weakness_type(new_k, new_pkmn, v)
            elif new_k == "evolution":
                new_pkmn = do_evolution(pkmn_id, new_pkmn, v)
            elif new_k == "name":
                new_pkmn = do_name(v, new_pkmn)
        id_to_pokemon[pkmn_id] = new_pkmn
        name_to_pokemon[new_pkmn["name"]] = new_pkmn

    with open("pokedex/data/name_to_pokemon.json", "w+") as f:
        json.dump(name_to_pokemon, f)
    with open("pokedex/data/id_to_pokemon.json", "w+") as f:
        json.dump(id_to_pokemon, f)
