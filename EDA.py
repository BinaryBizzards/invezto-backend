import plotly
import plotly.express as px
from plotly import graph_objects as go
import pandas as pd
import db

def fetch_and_prepare_data(name):
    
    database = db.init_connection()
    collection = database.get_collection(name)
    df = pd.DataFrame(list(collection.find({}))).astype({"_id": str})
    df_edited = df.drop(columns = ["_id"])

    if df_edited is not None:
        return df_edited
    else:
        return None

def opening_closing_trends_graph(name) :
    df = fetch_and_prepare_data(name)
    monthwise = df.groupby(df["Date"].dt.strftime('%B'))[["Open", "Close"]].mean()
    new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                            'September', 'October', 'November', 'December']
    monthwise_ordered = monthwise.reindex(new_order, axis = 0)
    fig = go.Figure()
    fig.add_trace(go.Bar(x = monthwise_ordered.index, 
                        y = monthwise_ordered["Open"], 
                        name = "Stock open price", 
                        marker_color = "crimson"))
    fig.add_trace(go.Bar(x = monthwise_ordered.index, 
                        y = monthwise_ordered["Close"], 
                        name = "Stock close price", 
                        marker_color = "lightsalmon"))
    fig.update_layout(barmode = "group", 
                    xaxis_title = "Month", 
                    yaxis_title="Stock Price", 
                    xaxis_tickangle = -45, 
                    title = "Monthwise comparison b/w stock opening & closing price", 
                    font_size = 15,autosize=True,
                    width=1200,
                    height=600)
    return plotly.io.to_json(fig)
    