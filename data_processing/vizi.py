import pandas as pd
from plotly.offline import init_notebook_mode, plot, iplot
from plotly.graph_objs import *
import plotly.graph_objs as go
import plotly.express as px
init_notebook_mode(connected=True)

def plot_box(y,title_ = None,x_axis = None,y_axis = None):
    data = [go.Box(y=y)]                       
    layout = go.Layout(
        title= title_,
        xaxis=dict(
            title = x_axis,
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title= y_axis,
            titlefont=dict(
                size=16,
                color='rgb(107, 107, 107)'
            ),
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
          )
        )
    
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def plot_bar(df,title_ = None,x_axis = None,y_axis = None): # df should take dataframe with first column as "Type" and second column as "Frequency"
    
    x = df.iloc[:,0]
    y = df.iloc[:,1]
    
    data=[go.Bar(
    x = x,
    y = y,
    text = y,
    textposition='auto')]  
    
    layout = go.Layout(
    title= title_,
    xaxis=dict(
        title = x_axis,
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title= y_axis,
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
      )
    )

    fig = go.Figure(data=data, layout=layout)
    #iplot(fig, filename='style-bar')
    fig.show()
    
def plot_bar_v(df,title_ = None,x_axis = None,y_axis = None,height= 1000): # df should take dataframe with first column as "Type" and second column as "Frequency"
    
    data=[go.Bar(
    x = df.iloc[:,1],
    y = df.iloc[:,0],orientation='h')]    
    
    layout = go.Layout(
    title= title_,
    xaxis=dict(
        title = x_axis,
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title= y_axis,
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
      )
    )
    
    fig = go.Figure(data=data, layout=layout)
    # Configure other layout properties
    fig.update_layout(
    height=height,
    width=900)
    iplot(fig)
    
def plot_histgram(x, title_ = None, x_axis = None, y_axis = None):

    data = [go.Histogram(x = x)]
    
    layout = go.Layout(
    title= title_,
    xaxis=dict(
        title = x_axis,
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title= y_axis,
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
      )
    )
    
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)
    
    
    
    
def plot_bubble(df, title_ = None, xaxis_ = None, yaxis_ = None):
    fig = px.scatter(df, x="indiv_transaction_amt", y = 'donation_count',
                     size="indiv_transaction_amt", color="cand_pty_affiliation",
                     hover_name="cand_name", log_x=True, size_max=60)
    
    fig.update_layout(
        title= title_,
        xaxis_title = xaxis_,
        yaxis_title = yaxis_,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    fig.show()
    
def check_missing(df,title_ = None,x_axis = None,y_axis = None, do_plot = False):
    missing_percent = round(df.isnull().sum() * 100 /df.shape[0],2)
    missing_percent = pd.DataFrame(missing_percent).reset_index()
    missing_percent.columns = ['features','percent']
    missing_percent = missing_percent.sort_values(by = 'percent').reset_index(drop= True)
    if do_plot:
        plot_bar(missing_percent,title_, x_axis, y_axis)
    else:
        return missing_percent