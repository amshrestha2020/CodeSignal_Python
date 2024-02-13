def solution(roads):
    # Create a dictionary to store the ends of each road
    road_ends = {}
    for road in roads:
        city1, city2, road_name = road
        if road_name not in road_ends:
            road_ends[road_name] = {city1, city2}
        else:
            road_ends[road_name].update({city1, city2})

    # Check if any two roads with neighboring names have a common end
    for i in range(len(roads) - 1):
        if len(road_ends[i].intersection(road_ends[i + 1])) > 0:
            return False

    return True
