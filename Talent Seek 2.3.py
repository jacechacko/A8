#import statements for libraries.  Packages installed already.
import json
import requests
from requests import post, get
import base64
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser


#Client authentication provided in the Developer dashboard of Spotify
Client_ID = "Enter Client ID from Spotify.Developer.com"
Client_secret = "Enter Client Secret from Spotify.Developer.com"


#Establish first function, which holds authentication information.
def request_token():

# concatenate the ID and Secret, per documentation
    ID_Secret = Client_ID + ":" + Client_secret

#URL provided by API for token
    url = "https://accounts.spotify.com/api/token"
#calls the base64 library function to encode the string to bytes, per spotify documentation
    ID_Secret_tobytes = ID_Secret.encode("utf-8")
#base64 encodes the ID_Secret_tobytes variable and also converts that value to string
    ID_Secret_base64 = str(base64.b64encode(ID_Secret_tobytes), "utf-8")

#requests library headers
    headers = {
#spotify documentation specifies these two values.  The base64 encoded variable earlier is passed here
        "Authorization": "Basic " + ID_Secret_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

#spotify documentation specifies this variable name, with this key and value.
    body_parameters = {

        "grant_type": "client_credentials"

    }

#utilizes the features in the requests library, being used to post data.  Headers and data defined earlier.
    response = post(url, headers=headers, data=body_parameters)

#converts the json data received into a readable format via json.loads method
    json_convert = json.loads(response.content)

#creates an access token variable, which looks through json_convert to find access_token, per Spotify API documentation
    access_token = json_convert["access_token"]
#fulltoken variable holds the syntax for all future requests, per spotify documentation
    return access_token


#this function will be used to call the token in various functions in order for the api requests to work
def authentication_token(access_token):
    fulltoken = {
        "Authorization": "Bearer " + access_token
    }
    return fulltoken


#get artist info, followers for each artist
def get_artist_info(genre, access_token, minimum_followers, minimum_popularity):
    #token and headers need to be passed per api instructions
    access_token = request_token()
    headers = authentication_token(access_token)

#creating the empty list that will hold our list of artists
    artists_list = []
    #This is the api endpoint for searching for artists
    search_page = "https://api.spotify.com/v1/search"

# spotify only allows for 50 results per page.  This makes the code difficult to use because it only searches
# through those 50, and only displays the artists with under minimum_follower count from those 50
# This means not all the results are searched.  We are instead
# using offset to search through multiple pages of results and then filtering that larger batch.

    #artists returned from the api call
    limit = 50
    #starting page
    offset = 0

    #For as long as API is sending us results, this is active.  That is why it's in while loop.
    while True:
        #query f-string captures the limit and offsets we defined above the while loop
        query = f"?q=genre:{genre}&type=artist&limit={limit}&offset={offset}"
        # concatenate the search with the query, did this separately so we can modify the offset and limit
        # easier if needed to in the future
        searchurl = search_page + query
        # the response from api is received with request library .get, the parameters are searchurl with prev defined headers
        # this will return a json object with all of the response information within it.
        response = requests.get(searchurl, headers=headers)
        # the resposne variable is parsed and converted from json to python dictionary.  The .get looks at the
        # artist key and if the key is empty, the second parameter loads empty dictionary.  Without the second parameter,
        # our code would stop with an error every time it reached the last response.  The .get items does the same thing,
        # items is what we call the value of the key, if empty returns empty list
        artists_response = response.json().get("artists", {}).get("items", [])

        # once the api sends empty list (meaning artist_response is empty) it breaks the while loop.  So when
        # the api is done giving us results, it breaks.  Without this, our program kept searching without stopping
        # because of the while loop.
        if not artists_response:
            break

        #The for loop searches for artist in the api returned dictionary.
        for artist in artists_response:
            #defines artist name as the name portion of artist list.
            artist_name = artist["name"]
            # within followers dictionary, the total key has the value of the followers.  0 is the default instead of empty
            # because we're dealing with integers.

            followers = artist.get("followers", {}).get("total", 0)
            # the if statement filters for artists where number of followers is less than the min_followers, which
            # we defined earlier.  For example, if we set min_followers to 50k, then only artists from a genre
            # with less than 50k followers are displayed in the output.

            if followers <= minimum_followers:
                # call the get_song_info function with access token passed to authenticate.  These variables are
                # found in the get_song_info function
                top_song_name, top_song_popularity, artwork_url, song_url = get_song_info(artist["id"], access_token)
                # the second if statement in this function focuses on the popularity of the track.  Our program
                # is set so the artists with less than min_popularity must also have a top song with a popularity
                # of over a certain number.  This is how we ensure that the artists we are seeing are not only
                # under the radar but also have growth potential, since their top song is so successfull.

                if top_song_popularity > minimum_popularity:
                    # this line says, if the popularity is high enough, add that artist and their song information
                    # to the artist_list list we created above (which was empty).  Each time an artist
                    # with under a certain amoutn of followers who has a track with over a certain amount
                    # of popularity, the artist name, the follower count, top song, popularity of top song, album
                    # art, etc, are all added to (.append) to the master list.
                    artists_list.append({
                        "name": artist_name,
                        "id": artist["id"],
                        "followers": followers,
                        "top_song": top_song_name,
                        "top_song_popularity": top_song_popularity,
                        "album_art": artwork_url,
                        "track_url": song_url
                    })

        # this accumulator allows us to basically go to next page, by searching through the next batch
        # first it searches through first 50 results, then with this logic it searches through next 50
        # until there are no more results.  So searches 1-50, then 51-100, until empty dictionary is found.
        offset += limit
    # When researching how to sort the list, the sorted() function is how to do this, with the
    # follower count as the means to sort.
    artists_list = sorted(artists_list, key=lambda artists_list: artists_list["followers"], reverse=True)
    # return function returns the master artist_list, list of all artist/song information, to the
    # get_artist_info function.  Will be called later in main function.
    return artists_list


#get_song_info function handles the api request for top song of each artist.  This function is called in the
#artist function above to help append the list.
def get_song_info(artist_id, access_token):
    #like for all other functions that handle the requests, we need to pass the token and headers information.
    headers = authentication_token(access_token)

    #spotify API endpoint for the top track of an artist
    top_song_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"

    # again using request library .get method to get the top track, passing the url and headers as parameters
    # gives us json object of top song info
    response = requests.get(top_song_url, headers=headers)

    # spotify will return a json object with the track information, so we use json library to convert
    # to python dictionary and extract the tracks key, empty list returned if not found.
    songs = response.json().get("tracks", [])

    #variable holds the first song in the list
    top_song = songs[0]

    # we also want the artwork for the song, and spotify api provides this as a get request per documentation
    # it pulls the album from the top song we found, and the image associated with it
    artwork = top_song["album"]["images"]
    # create variable that takes that image we just isolated, picks the first of the 3 images, and grabs the url
    # associated with it
    artwork_url = artwork[0]["url"]


    #within the extnral_urls dictionary there is key of spotify which holds the spotify url for that particular track
    song_url = top_song["external_urls"]["spotify"]

    #create a variable that holds the name key of the top song
    topsongname = top_song["name"]
    song_popularity = top_song["popularity"]
    # this return function returns the these top track variables we created.  The return will mae it so that
    # when we call the get_song_info function into the artist_info function, we can pass these variables
    # we created so that the information can be added to the master list, in other words, it can be appended
    # as each new entry is added to the artist_list.
    return topsongname, song_popularity, artwork_url, song_url


#The next portion of the code creates the logic required for our GUI.  It creates a function called
#gui_main that houses the structure and behavior of our gui code.  The main components we wrote were for
#clicking on the hyperlinks (using webbrowser module via open_links() function), as well as the main gui output.  Our structure is a
#main window with the prompts and a search window that opens when search is clicked.
def gui_main():
    #This function uses the webbrowser module.  Our output is a table where two fields hold website urls.  We
    #wanted the user to be able to open these links by clicking on it.  Research showed us that this was
    #possible with the webbrowser module.  Because we wanted output to be a table, we used something called
    #ttk instead of tk, because it had a feature called treeview, which simulates a table.
    def open_links(click):

    #tree.focus will identify which cell in table is highlighted
        cell = tree.focus()
    #the identify_column method in tree will determine the column.  The click.x for where was clicked.
    #documentation says it will be like #1, #2, #3, etc.
        column = tree.identify_column(click.x)
    #the cell variable is called in the .item function, and passes value of cell.
        dataincoll = tree.item(cell, "values")

    #We then use conditional logic to indicate what happens for the links.
        #If i click on 5th column, we see url for album art
        if column == "#5":
            album_art_url = dataincoll[4]
            #using webbrowser module, can open url.
            webbrowser.open(album_art_url)
        #If i click on 6th column, we see url for the external url
        elif column == "#6":
            external_url = dataincoll[5]
            #using webbrowser module, can open url.
            webbrowser.open(external_url)


#This next function houses our main GUI code.  We used ttk instead of tk for the
#search window so that we could use the treeview in order to have a clean table for our
#results.
    def gui_screens():
#again passing the access token to each function for our API calls, per documentation
        access_token = request_token()

        #gets value of the StringVar() we define below, default will be hip-hop genre
        genre = pick_genre.get()
        #Error validation-makes sure that the user inputs a valid integer for the
        #min follower, min pop variables
        try:
        #user gets to decide the min follower threshold, from the entry widget for followers.
            min_followers = int(entry_followers.get())
        #user gets to decide the min pop threshold, from the entry widget for popularity.
            min_popularity = int(entry_popularity.get())
        #except clause, if input isn't a valid integer, the messagebox from tk has a
        #showerror method.  Within that, we prompt user to enter a valid number.
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for followers and popularity.")
            return
        artist_list = get_artist_info(genre, access_token, min_followers, min_popularity)

#This next block sets the body of the search window.  Basically, when the user presses the
#search button, it opens a new window over the main window.
        search_window = tk.Toplevel(main)
        search_window.title("Search Results")
        search_window.geometry("1100x600")
        search_window.config(bg="#DDEEFF")
#sets the column headers for the table in Treeview
        columns = ("Artist", "Top Song", "Popularity", "Followers", "Album Art", "External URL")
        global tree

#set frame inside search window, packs it after
        search_frame = tk.Frame(search_window)
        search_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

#initiates the Treeview table from ttk, within tree variable.  Parameters make sure it
#is inside search frame, and has proper columns and headers.
        tree = ttk.Treeview(search_frame, columns=columns, show="headings")

#Conditional logic: The for loop goes through all the column names in the
#columns variable, sets headers for columns and aligns them for width/centering.
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

#Next we wanted a scroll bar for the results, assuming the results exceed the window size
#ttk has a scrollbar method, placed inside search frame.
        scrollbar1 = ttk.Scrollbar(search_frame, orient="vertical", command=tree.yview)
#connects the vertical scrollbar, with the command
        tree.configure(yscrollcommand=scrollbar1.set)
        scrollbar1.pack(side='right', fill='y')
        tree.pack(side='left', expand=True, fill='both')

#This for loop looks for all the artists who fit the criteria from the master artist list
#it then uses the .insert method from ttk treeview to append the rows to the
#tabular treeview.
        for artist in artist_list:
            tree.insert("", tk.END, values=(
                artist["name"],
                artist["top_song"],
                artist["top_song_popularity"],
                artist["followers"],
                artist["album_art"],
                artist["track_url"]
            ))

#We need to make it so that a left click (button 1) initiates the open_link function
#this will check to see what/where was clicked
        tree.bind("<Button-1>", lambda click: open_links(click))


#This next block of code intiates the main window, using tkinter
#We first initiate the window, set the title and size
    main = tk.Tk()
    main.config(bg="#E4E2E2")
    main.title("TalentSeek 2.3")
    main.geometry("700x450")

    window_width = 700
    window_height = 450
    button_width = 80
    button_height = 40
    padding = 10

    center_x = window_width // 2 - 116 // 2

#This is all the genres user will see in the optionmenu we created
    genre_options = ["pop", "hip-hop", "rock", "country", "metal", "indie", "blues", "alt-rock", "k-pop", "classical",
            "house", "dance", "edm", "electronic", "r-n-b"
                     ]
#default=hip-hop
    pick_genre = tk.StringVar(value="hip-hop")

#Main label, label1, shows title.
    label1 = tk.Label(main, text="TalentSeek 2.3", bg="#E4E2E2", fg="#000", font=("", 50))
#positions label with place method.
    label1.place(x=118, y=18, width=481, height=90)

#prompts user to select genre
    tk.Label(main, text="Select Genre:", bg="#E4E2E2", fg="#000", font=("", 10)).place(x=center_x, y=155, width=116, height=27)

#we are using an optionmenu instead of checkboxes as we stated in update 1 because it provides a cleaner look
#this will show user all the options in the genre selection.
    genre_select = tk.OptionMenu(main, pick_genre, *genre_options)
    genre_select.config(bg="#E4E2E2", fg="#000", font=("", 10))
    genre_select.place(x=center_x, y=184, width=116, height=27)

#The label and entry for followers, shows the word followers in a label, then creates an entry box for user to
#enter the max follower count.  If the user enters a non integer, the program handles it with the try/except from earlier
    tk.Label(main, text="Max Followers:", bg="#E4E2E2", fg="#000", font=("", 10)).place(x=center_x, y=230, width=116, height=20)
    entry_followers = tk.Entry(main)
    entry_followers.place(x=center_x, y=255, width=116, height=27)
#Sets default value to 75k.
    entry_followers.insert(0, "75000")


#The same process for min popularity.  Text label showing the words min popularity, then an entry label for user
#to input min popularity, with error handling again via try/except.
    tk.Label(main, text="Min Popularity:", bg="#E4E2E2", fg="#000", font=("", 10)).place(x=center_x, y=295, width=116, height=20)
    entry_popularity = tk.Entry(main)
    entry_popularity.place(x=center_x, y=320, width=116, height=27)
#Sets default value of the entry to 50.
    entry_popularity.insert(0, "50")

#The search button is created via button method of tk.  Paramater of command calls the run main with genre
#function we made earlier to initiate the search component and also create and modify the search window,
#which is the toplevel window we call when we are doing searches.
    search_button = tk.Button(main, text="Search", command=gui_screens, bg="#E4E2E2", fg="#000", font=("", 10))
    search_button.place(x=padding, y=window_height - button_height - padding,
                        width=button_width, height=button_height)

#Quit button exits app with main.destroy command.
    quit_button = tk.Button(main, text="Quit", command=main.destroy, bg="#E4E2E2", fg="#000", font=("", 10))
    quit_button.place(x=window_width - button_width - padding,
                      y=window_height - button_height - padding,
                      width=button_width, height=button_height)

    main.mainloop()

#calling of main function, gui_main, to call the main function and initiate the program.
if __name__ == "__main__":
    gui_main()
