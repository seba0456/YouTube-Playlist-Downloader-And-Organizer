from datetime import datetime
today = datetime.today().strftime("%H-%M_%Y-%m-%d")

# Function to generate HTML code for the list of similar songs
def generate_html_duplicate_list(songs, playlist_name, playlist_url):
    song_amount=len(songs)
    html_content = "<div class='border-box'><h1>Similar videos</h1><br><h2><a href='"+str(playlist_url)+"'>"+str(playlist_name)+"</a></h2><br><p>Found: <b>" + str(song_amount) + "</b> similar videos in this playlist.<br><i>Date: "+str(today)+"</i></p><br><ol>"
    for song1, song2 in songs:
        html_content += f"<li><a href='{song1.url}' target='_blank'>{song1.title}</a> is similar to: <a href='{song2.url}' target='_blank'>{song2.title}</a> by: {song2.similarity if song2.similarity else ''}</li><br>"
    html_content += "</ol></div>"
    return html_content

def generate_html_list(songs, playlist_name, playlist_url):
    # Sort songs alphabetically by title
    songs_sorted = sorted(songs, key=lambda song: song.title.lower())
    
    song_amount = len(songs_sorted)
    html_content = (
        "<div class='border-box'>"
        "<h1>Playlist backup</h1><br>"
        "<h2><a href='"+str(playlist_url)+"'>"+str(playlist_name)+"</a></h2><br>"
        "<p>Found: <b>" + str(song_amount) + "</b> videos in this playlist.<br>"
        "<i>Date: "+str(today)+"</i></p><br>"
        "<ol>"
    )
    
    for song in songs_sorted:
        html_content += f"<li><a href='{song.url}' target='_blank'>{song.title}</a></li><br>"
    
    html_content += "</ol></div>"
    
    return html_content


def read_html_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

def extract_head_and_body(html_content):
    head_start = html_content.find('<head>') + len('<head>')
    head_end = html_content.find('</head>')
    body_start = html_content.find('<body>') + len('<body>')
    body_end = html_content.find('</body>')

    head = html_content[head_start:head_end].strip()
    body = html_content[body_start:body_end].strip()
    
    return head, body
def load_js_code_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        js_content = file.read()
    return js_content