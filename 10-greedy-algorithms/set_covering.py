# Greedy algorithm for set covering problem

def greedy_set_cover(states_needed, stations):
    """
    Returns a set of stations that covers all the states using a greedy approach.
    """
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        if best_station is None:
            break  # No station covers any remaining state
        final_stations.add(best_station)
        states_needed -= states_covered
    return final_stations


def main():
    # States that need to be covered
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # Stations and the states they cover
    stations = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }

    result = greedy_set_cover(states_needed, stations)
    print("Stations to cover all states:", result)


if __name__ == "__main__":
    main()