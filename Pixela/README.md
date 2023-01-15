# Modules

Dependencies\n
requests module

Class
Pixela(username, api_token)

Methods
"""User Methods"""
create_user()                     : Register a new user
update_user(new_api_token)        : Update API Token for an existing user
delete_user()                     : Deleter a user

"""Graph Methods"""
create_graph(graph_name, graphid) : Create a new graph
delete_graph(graphid)             : Deletes a graph

"""Pixel Methods"""
register_pixel(graphid, date)     : Register a pixel on specified date on a given graph
delete_pixel(graphid, date)       : Delets a pixel on specified date on a given graph
