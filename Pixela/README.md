# Modules

Dependencies
<br />requests module<br />
<br />Class
<br />Pixela(username, api_token)<br />
<br />Methods
<br />"""User Methods"""
<br />create_user()                     : Register a new user
<br />update_user(new_api_token)        : Update API Token for an existing user
<br />delete_user()                     : Deleter a user
<br /><br />"""Graph Methods"""
<br />create_graph(graph_name, graphid) : Create a new graph
<br />delete_graph(graphid)             : Deletes a graph
<br /><br />"""Pixel Methods"""
<br />register_pixel(graphid, date)     : Register a pixel on specified date on a given graph
<br />delete_pixel(graphid, date)       : Delets a pixel on specified date on a given graph
