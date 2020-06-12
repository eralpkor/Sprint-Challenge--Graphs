from room import Room
from player import Player
from world import World
from graph import Graph
from stack import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# -----------------------------------------------------------------------------------------
# Traverse maze in a DFT
# def build_path(graph):
#     # stack contains our current path
#     stack = Stack()
#     # List that contains returned path
#     moves = []
#     # to find out if we hit a dead end
#     visited = set()
#     # start traversal with 0 index room
#     stack.push(0)

#     while len(visited) < len(graph):
#         # get the current room id in the stack
#         current_room_id = stack.tail()
#         # mark it as visited
#         visited.add(current_room_id)
#         # Get info on the current room (tuple data)
#         current_room = graph[current_room_id]
#         # dict of possible moves:
#         rooms_dict = current_room[1]
#         # List (array) to track if room has not been visited yet
#         unvisited = []
#         # store unvisited rooms in relation to the current room
#         for direction, room_id in rooms_dict.items():
#             if room_id not in visited:
#                 unvisited.append(room_id)

#         # assign next room
#         # if reached a dead end, back track
#         if len(unvisited) > 0:
#             next_room = unvisited[0]
#             stack.push(next_room)
#         else:
#             stack.pop()
#             next_room = stack.tail()

#         # check the rooms around the current room. if the next move matches
#         # room_id add it to moves and walk
#         for directions, adjacent_id in rooms_dict.items():
#             if adjacent_id == next_room:
#                 moves.append(direction)
            
#     return moves

# traversal_path = build_path(room_graph)

# move the player:
def move_player(direction):
    player.travel(direction) # check players direction options
    # keep adding to traversal path
    traversal_path.append(direction) # n, n, 

# DFT traversal
def DFT_recursive(visited=None, prev=None, move=None):
    current = player.current_room.id # grab the current room (always defaults to 0)
    # grab all possible EXITS for current room from the "test file"
    neighbors = player.current_room.get_exits() 
    reverse = {'w': 'e', 'n': 's', 's': 'n', 'e': 'w'}

    if visited is None:
        visited = {}

    # current room is not in visited, add to visited
    if current not in visited: 
        visited[current] = {}

    # if there is direction (move) add to visited as current node (vertex)
    if move is not None: 
        visited[prev][move] = current

    if prev is not None: # if prev was 'N' reverse must be 'S'
        visited[current][reverse[move]] = prev # add to visited direction

    if len(visited[current]) < len(neighbors): # if visited current has more exits
        for direction in neighbors: # 'n', 's', 'e', 'w' possible exits
            if direction not in visited[current]: # if direction to move not in current room
                move_player(direction) # move player to that direction and add to traversal path
                DFT_recursive(visited, prev=current, move=direction) #

    if len(visited) < len(room_graph): # check with test file
        direction = reverse[move]
        move_player(direction)

DFT_recursive() # invoke function with default (3*None)

# print("TRAVERSAL PATH: ", traversal_path)
# -----------------------------------------------------------------------------------------
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
