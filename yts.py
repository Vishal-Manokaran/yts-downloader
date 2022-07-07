import os
import json
from tabulate import tabulate
from urllib.parse import quote
from urllib.request import Request,urlopen

import constants

def api_req(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request).read().decode()
    return response

def display_movie(movie):
    table = [["Title", movie['title_long']],
            ["Duration", f"{movie['runtime']//60}hrs {movie['runtime']%60}mins"],
            ["Language", constants.ISO639_2[movie['language']]],
            ["MPA Rating", movie['mpa_rating']],
            ["IMDb", f"https://www.imdb.com/title/{movie['imdb_code']}/?ref_=fn_al_tt_1"]]
    print(tabulate(table, missingval="-"))

def display_torrents(torrents):
    table = [["Option","Size","Quality","Type","Seeds","Peers"]]
    options = []
    for index,torrent in enumerate(torrents):
        options.append(chr(65+index))
        table.append([chr(65+index), torrent['size'], torrent['quality'], torrent['type'], torrent['seeds'], torrent['peers']])
    print(tabulate(table, headers=("firstrow"), missingval="-"))
    return options

def find_yify_torrent():
    hash = None
    new = True
    while hash == None:
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        movie_name = input("ENTER THE MOVIE NAME: ") if new else movie_name
        encoded_string=quote(movie_name)
        total_index = 0 if new else total_index + (page*response['data']['limit'])
        page = 0 if new else page+1
        if not new and total_index >= response["data"]["movie_count"]:
            new = True if input("No more search result left. Search for a new movie?(y/n) ").upper() == "Y" else False
            if not new:
                print("terminating")
                return None
        url=f"https://yts.am/api/v2/list_movies.json?query_term={encoded_string}&page={page}"
        response = api_req(url)
        response = json.loads(response)
        try:
            if response["status"] != "ok":
                raise Exception("Unable to connect to YIFY")
            elif response["data"]["movie_count"] == 0:
                raise Exception(f"No movie found in the name: {movie_name}")
            
            for index,movie in enumerate(response["data"]["movies"]):
                total_index+=1
                os.system('cls' if os.name == 'nt' else "printf '\033c'")
                print(f"found {response['data']['movie_count']} movie(s)\n")
                print(f"#{index+1}")
                display_movie(movie=movie)

                if input("\nIs this the movie?(y/n) ").upper() == "Y":
                    while True:
                        os.system('cls' if os.name == 'nt' else "printf '\033c'")
                        print(f"{movie['title_long']}\nTorrents:")
                        options = display_torrents(torrents=movie['torrents'])
                        print
                        c = input(f"\nEnter an alphabet from Options{options} to download corresponding torrent ")
                        if c.upper() in options:
                            hash = movie["torrents"][ord(c.upper())-65]["hash"]
                            return hash
                            # break
                    # break
                    
            if index + 1 == min(response["data"]["limit"],response["data"]["movie_count"]) and total_index <= response["data"]["movie_count"]:
                new = False if input("Do you want to continue to next page?(y/n) ").upper() == "Y" else True
                if new and input("Do you want to stop?(y/n) ").upper() == "Y":
                    print("terminating")
                    return None
            # else:
            #     hash = response["data"]["movies"][0]["torrents"][0]["hash"]
        except KeyError as ke:
            if ke.args[0] == 'movies':
                _ = input("Page Number exceeded.")
            else:
                _ = input(ke)
            return None
        except Exception as e:
            _ = input(e)
            return None
    # session = requests.Session()
    # retry = Retry(connect=3, backoff_factor=0.5)
    # adapter = HTTPAdapter(max_retries=retry)
    # session.mount('http://', adapter)
    # session.mount('https://', adapter)

    # session.get(url)

    # hash = "CAEBDB751F2B541C9A420A15FB5C107494544285"
    


if __name__ == "__main__":
    print(find_yify_torrent())