'''# Milestone 1 - Represent and Analyse One Listening Item
 
# a) Input listener name, title, creator, media type, duration (seconds), rating out of 5
listener = input("Enter listener name: ")
title = input("Enter title: ")
creator = input("Enter creator: ")
media_type = input("Enter media type (Song/Podcast): ")
duration_text = input("Enter duration (seconds): ")
rating_text = input("Enter rating out of 5: ")
 
# b) Convert duration and rating to numbers and show their data types
duration = int(duration_text)    # text -> whole number
rating = float(rating_text)      # text -> decimal number
 
print("\n--- Python Data Types ---")
print("Listener  :", type(listener))
print("Duration  :", type(duration))
print("Rating    :", type(rating))
 
# c) Convert duration to minutes and remaining seconds using // and %
minutes = duration // 60
seconds = duration % 60
 
# d) 3-character media code using string slicing
media_code = media_type[:3].upper()
 
# d) Display neatly
print("\n--- Listening Item ---")
print(f"Listener   : {listener}")
print(f"Title      : {title}")
print(f"Creator    : {creator}")
print(f"Media Type : {media_type}")
print(f"Media Code : {media_code}")
print(f"Duration   : {duration} seconds = {minutes} min {seconds} sec")
print(f"Rating     : {rating} / 5")'''


'''# Milestone 2 - Build a Multi-Item Listening Queue
# (Extends Milestone 1 using collections, decisions and loops)
 
items = []          # list of dictionaries (one dictionary per song/podcast)
creators = set()    # set of unique creators
 
print("Enter listening items. Type DONE as the title to stop.\n")
 
# a) Repeatedly accept records until DONE
while True:
    title = input("Title (or DONE): ").strip()
    if title.upper() == "DONE":
        break
    creator = input("Creator: ").strip()
    media_type = input("Type (SONG/PODCAST): ").strip().upper()
 
    try:
        duration = int(input("Duration (seconds): "))
        rating = float(input("Rating (1-5): "))
    except ValueError:
        print("Rejected: duration and rating must be numbers.\n")
        continue
 
    # c) Reject bad duration or rating and continue with the next record
    if duration <= 0 or rating < 1 or rating > 5:
        print("Rejected: duration must be > 0 and rating must be between 1 and 5.\n")
        continue
 
    # b) Store the record as a dictionary in the list, creator in the set
    items.append({"title": title, "creator": creator, "type": media_type,
                  "duration": duration, "rating": rating})
    creators.add(creator)
    print("Added!\n")
 
# d) Classify each item and count categories
counts = {"Quick": 0, "Standard": 0, "Long-form": 0}
total_time = 0
for item in items:
    total_time += item["duration"]
    if item["duration"] <= 300:
        category = "Quick"
    elif item["duration"] <= 1800:
        category = "Standard"
    else:
        category = "Long-form"
    item["category"] = category
    counts[category] += 1
 
# e) Display results
print("\n--- Queue Summary ---")
for item in items:
    print(f"{item['title']} | {item['type']} | {item['duration']} s | "
          f"{item['rating']} | {item['category']}")
 
if items:
    best = items[0]
    for item in items:
        if item["rating"] > best["rating"]:
            best = item
    print("\nTotal listening time :", total_time, "seconds")
    print("Category counts      :", counts)
    print("Highest-rated item   :", best["title"], "(", best["rating"], ")")
    print("Unique creators      :", len(creators), "->", sorted(creators))
else:
    print("No valid items were entered.")'''


'''# Milestone 3 - Model a Playlist Using Object-Oriented Composition
# (Same data as Milestone 2, now organised with two collaborating classes)
 
class MediaItem:
    app_name = "Digital Playlist and Listening Analytics System"   # class variable
 
    def __init__(self, title, creator, media_type, duration_sec, rating):
        self.title = title
        self.creator = creator
        self.media_type = media_type
        self.duration_sec = duration_sec
        self.rating = rating
 
    def __str__(self):          # readable summary of one item
        mins, secs = divmod(self.duration_sec, 60)
        return (f"{self.title} by {self.creator} [{self.media_type}] - "
                f"{mins}m {secs}s - Rating: {self.rating}/5")
 
 
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.items = []         # the Playlist HAS MediaItem objects (composition)
 
    def add_item(self, item):
        self.items.append(item)
 
    def total_duration(self):
        total = 0
        for item in self.items:
            total += item.duration_sec
        return total
 
    def top_rated(self):
        best = self.items[0]
        for item in self.items:
            if item.rating > best.rating:
                best = item
        return best
 
    def display_playlist(self):
        print("Playlist:", self.playlist_name)
        for number, item in enumerate(self.items, start=1):
            print(f"  {number}. {item}")
 
    def __len__(self):          # lets us write len(playlist)
        return len(self.items)
 
 
# e) Add at least three MediaItem objects to one Playlist
print("Application:", MediaItem.app_name, "\n")
 
my_playlist = Playlist("My Evening Mix")
my_playlist.add_item(MediaItem("Blinding Lights", "The Weeknd", "SONG", 200, 4.8))
my_playlist.add_item(MediaItem("Data Skeptic", "Kyle Polich", "PODCAST", 1875, 4.5))
my_playlist.add_item(MediaItem("Shape of You", "Ed Sheeran", "SONG", 240, 4.0))
 
my_playlist.display_playlist()
print("\nPlaylist size  :", len(my_playlist))
print("Total duration :", my_playlist.total_duration(), "seconds")
print("Top rated item :", my_playlist.top_rated())
 
# Explanation of object composition (3-4 lines):
# The Playlist class contains MediaItem objects inside its items list, so a
# Playlist "has" many MediaItems (like a bag has many books). The Playlist does
# not copy the item details; it keeps the objects and asks them for their data.
# Each class has one clear job, which keeps the code neat and reusable.'''

# media_utils.py - user-defined module (Milestone 4)
 
def seconds_to_hms(seconds):
    """Convert seconds into H:MM:SS text."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}:{minutes:02d}:{secs:02d}"
 
 
def filter_by_rating(items, min_rating=4.0):
    """Return only items whose rating is >= min_rating."""
    result = []
    for item in items:
        if item["rating"] >= min_rating:
            result.append(item)
    return result
 
 
def summarize_by_type(items):
    """Return {'SONG': {'count': 2, 'seconds': 440}, ...}"""
    summary = {}
    for item in items:
        kind = item["type"]
        if kind not in summary:
            summary[kind] = {"count": 0, "seconds": 0}
        summary[kind]["count"] += 1
        summary[kind]["seconds"] += item["duration"]
    return summary
# main.py - Milestone 4: Modularize Playlist Analytics with Functions
import time
from media_utils import seconds_to_hms, filter_by_rating, summarize_by_type
 
# Sample collection (same style of records as Milestone 2)
items = [
    {"title": "Blinding Lights", "creator": "The Weeknd", "type": "SONG", "duration": 200, "rating": 4.8},
    {"title": "Data Skeptic", "creator": "Kyle Polich", "type": "PODCAST", "duration": 1875, "rating": 4.5},
    {"title": "Shape of You", "creator": "Ed Sheeran", "type": "SONG", "duration": 240, "rating": 4.0},
    {"title": "Deep Dive", "creator": "Lex F", "type": "PODCAST", "duration": 3600, "rating": 3.5},
]
 
 
# b) Functions that receive the media-item collection and return results
def show_summary(items):
    summary = summarize_by_type(items)
    for kind, info in summary.items():
        print(f"  {kind}: {info['count']} item(s), total {seconds_to_hms(info['seconds'])}")
 
 
def show_top_rated(items):
    for item in filter_by_rating(items, min_rating=4.0):
        print(f"  {item['title']} ({item['rating']})")
 
 
# c) Map menu choices to functions in a dictionary
menu = {"1": show_summary, "2": show_top_rated}
 
print("1 = Summary by type")
print("2 = Items rated 4.0 or more")
choice = input("Enter your choice (1/2): ")
 
start = time.time()
if choice in menu:
    menu[choice](items)             # call the selected function through the dictionary
else:
    print("Invalid choice")
 
# d) Lambda expression: sort by rating, highest to lowest
sorted_items = sorted(items, key=lambda item: item["rating"], reverse=True)
print("\nSorted by rating (highest first):")
for item in sorted_items:
    print(f"  {item['rating']}  {item['title']}")
 
# e) Show summary-generation time using the time module
end = time.time()
print(f"\nSummary generated in {end - start:.6f} seconds")
