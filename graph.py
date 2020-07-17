# from queue import Queue

# class Graph():
#     def __init__(self, player):
#         self.rooms = {}
#         self.player = player
#         self.traversal_path = []

#     # Add a room (add vertex) to graph
#     def add_room(self, room_id, exits):
#         if room_id not in self.rooms:
#             self.rooms[room_id] = [{}, ()] # create empty 
#             # loop over exist list from room.py
#             for exit in exits:
#                 self.rooms[room_id][0][exit] = '?'
#             # if room id is 0 

'''
* Fill out a list with traversal that will visit all rooms at least once

* Commands:
    - player.current_room.id: This will give us the current room id

    - player.current_room.get_exits(): Will return a list of possible moves we can make

    - player.travel(direction, [boolean: will display room info to us]): This will allow us to move / traverse rooms

* Create an array with a valid move set: We can achieve this with the player.current_room.get_exits()

* Graph Class
    - Will need a vertices attr that is a dict (complete)
        - the keys will be a room id
        - the values will be a dict, this will hold n,s,e,w whose values will be the room id for the possible move
    - The vertex will be the current room ID
    - The edges will be the rooms that the room ID connects to
    - some function: We will need the player instance passed to us so that we have a way to move around the player
    - We need a BFT fn for us to move around and traverse the map
'''

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # if vertex passed to us is going to be a room id
        if vertex not in self.vertices:
            self.vertices[vertex] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    def add_edges(self, vertex, key, value):
        self.vertices[vertex][key] = value
        '''
        Add an edge to the vertex

        The vertex passed should be a room id
        The key passed should be a string of n,s,e,w
        The value is going to be a room id as well

        This will allow us to index a room and apply a room id to a direction of the current room
        '''