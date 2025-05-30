import copy
import heapq
import sys
import time


class City:

    def __init__(self, city_id):
        self.city_id = city_id
        self.name = None
        self.distance = float('inf')
        self.weight = None
        self.adj_list = list()
        self.parent = None
        self.visited = False

    def add_neighbor(self, to_ver):
        self.adj_list.append(to_ver)

    def __lt__(self, other):
        return self.distance < other.distance

    def is_not_visited(self):
        if self.visited is False:
            return True
        return False



class SaveList:

    def __init__(self, city_list, start, end):
        self.city_list = city_list
        self.start = start
        self.end = end


def daikstra(one_list, start, end):
    for one in one_list:
        one.visited = False
        one.key = float('inf')

    queue = []
    visited_list = list()
    start_city = None
    end_city = None
    for one in one_list:
        if one.name == start:
            start_city = one
        if one.name == end:
            end_city = one

    start_city.key = 0
    heapq.heappush(queue, start_city)
    while queue:
        current = heapq.heappop(queue)
        if current.visited: continue

        for edge in current.edge_list:
            if edge.to_city.is_not_visited:
                heapq.heappush(queue, edge.to_city)
                if current.key + edge.cost < edge.to_city.key:
                    edge.to_city.key = current.key + edge.cost
                    edge.to_city.parent = current
        current.visited = True
        visited_list.append(current)
        if current == end_city:
            break

    for one in visited_list:
        if one.city_id == end_city.city_id:
            return one.key


def main():
    answer_list = list()
    case_list = list()
    case_number = int(sys.stdin.readline().rstrip())
    for c_num in range(0, case_number):
        city_list = list()
        city_number = int(sys.stdin.readline())
        for c in range(0, city_number):
            city = City(c)
            city_list.append(city)

        for city_num in range(0, city_number):
            city_name = str(sys.stdin.readline().rstrip('\n'))
            city_name = city_name.lower()
            neigh_number = int(sys.stdin.readline().rstrip('\n'))
            for nei_num in range(0, neigh_number):
                nei_cost = sys.stdin.readline()
                nei_cost = nei_cost.split(" ")
                neighbor = int(nei_cost[0]) - 1
                cost = int(nei_cost[1])
                city_list[city_num].name = city_name
                edge = Edge(city_list[neighbor], cost)
                city_list[city_num].add_neighbor(edge)
        num_paths = int(sys.stdin.readline())
        for n_path in range(0, num_paths):
            one_pair = sys.stdin.readline()
            one_pair = one_pair.split(" ")
            from_city = one_pair[0].rstrip()
            to_city = one_pair[1].rstrip()
            temp_list = copy.deepcopy(city_list)
            answer_list.append(daikstra(temp_list, from_city, to_city))

        skip = sys.stdin.readline()
    count = 0
    for an in answer_list:
        sys.stdout.write("{0}".format(an))
        if count <= case_number:
            sys.stdout.write("\n")
        count+=1

if __name__ == "__main__":
    # s = time.time()
    main()
    # print(time.time() - s)