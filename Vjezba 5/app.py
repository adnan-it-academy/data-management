from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def books():
    html = ""
    df = pd.read_csv('books.csv')

    for index, row in df.iterrows():
         html += f"<img src='/static/covers/Ponos_i_predrasude.jpg'alt='{row["title"]} cover'><div class=book-text-container><h3>{row["title"]}</h3><p>{row["author"]}</p><p>{row["published"]}</p><p>{row["genre"]}</p></div>"
    
    return html