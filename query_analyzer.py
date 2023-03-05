#-----------------------------Import-----------------------------------------

import psycopg2
import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import messagebox

#-----------------------------Backend ----------------------------------------
def execute_query():

    #--------------------- Get user inputs-----------------------------------
    host = host_entry.get()
    database = database_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    query = query_text.get('1.0', 'end-1c')

    #-----------------Connect to the PostgreSQL database----------------------
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    except:
    #-------------------------------Error Exception----------------------------
        messagebox.showerror("Error", "Failed to connect to database")
        return

    #---------------------Define the dynamic SQL query---------------------
    query = "explain analyze " + query

    #---------------------Query Execution-----------------------------------
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except:
        messagebox.showerror("Error", "Failed to execute the query try again!!")
        conn.close()
        return

    # ---------------------Parse the output to create nodes and edges---------------------
    nodes = []
    edges = []
    node_info = {}
    for row in result:
        node = row[0].split()[0]
        nodes.append(node)
        if "->" in row[0]:
            edge = row[0].replace("->", "").strip()
            edges.append(edge)
        else:
            node_info[node] = row[0]

    # ---------------------Create a directed graph using NetworkX---------------------
    G = nx.DiGraph()

    # ---------------------Add nodes to the graph--------------------------------------
    for node in nodes:
        G.add_node(node)

    # ---------------------Add edges to the graph---------------------------------------
    for u, v in zip(edges, edges[1:]):
        G.add_edge(u, v)

    #---------------------Define node positions for the layout---------------------------
    pos = nx.spring_layout(G, iterations=50)

    # ---------------------Draw the graph using Matplotlib--------------------------------
    plt.clf()
    nx.draw_planar(G, with_labels=True)

    #---------------------Add node hover text----------------------------------------------
    nx.draw_networkx_edge_labels(G, pos, edge_labels={})
    nx.draw_networkx_labels(G, pos, labels=node_info, font_size=8, font_color='w', bbox=dict(facecolor='black', edgecolor='none', alpha=0.7))

    #--------------------------------Show the graph------------------------------
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

    # ---------------------Close the database connection---------------------
    conn.close()
# ---------------------Creation of Graphical User Interface---------------------
root = tk.Tk()
root.title("QueryAnalyzer Graph")
root.resizable(False, False)
window_width=400
window_height=400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# ---------------------Host input---------------------
host_label = tk.Label(root, text="Host:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()

# ---------------------Database input---------------------
database_label = tk.Label(root, text="Database:")
database_label.pack()
database_entry = tk.Entry(root)
database_entry.pack()

# ---------------------User input---------------------
user_label = tk.Label(root, text="User:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()

# ---------------------Password input---------------------
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# ---------------------Query input---------------------
query_label = tk.Label(root, text="Query:")
query_label.pack()
query_text = tk.Text(root, height=8)
query_text.pack()

# ---------------------Query button---------------------
query_button = tk.Button(root, text="Analyze Query",background="dark orange",command=execute_query)
query_button.place(x=152,y=335)

# ---------------------Run GUI---------------------
root.mainloop()
