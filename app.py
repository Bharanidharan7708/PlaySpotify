from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pass the Spotify playlist URL to template
    spotify_playlist_url = "https://open.spotify.com/embed/playlist/5LxpyPEIBB0LEKwlHqSeVn?utm_source=generator"
    return render_template('index.html', spotify_playlist_url=spotify_playlist_url)

if __name__ == '__main__':
    app.run(debug=True)
