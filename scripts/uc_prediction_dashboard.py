import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import statsmodels.api as sm
import numpy as np
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# To change scientific numbers to float
np.set_printoptions(formatter={'float_kind':'{:f}'.format})

# Read the data
df = pd.read_csv('cleaned_data.csv')
df.head()

# Logistic regression model
X = df[['Age ', 'Sex', 'Current Smoker', 'IBD-U', '5-ASA', 'Azathioprine or 6-MP', 
        'Adalimumab', 'vedolizumab', 'current steroid use', 'Tofacitinib', 'Ustekinumab', 
        'New Previous surgery', 'New previous biologic used']]
y = df['UC']
X = sm.add_constant(X)

# Fit the logistic regression model
model = sm.Logit(y, X)
result = model.fit()

# Extract coefficients, p-values, and odds ratios
coefficients = result.params
p_values = result.pvalues
odds_ratios = coefficients.apply(lambda x: round(np.exp(x), 3))

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Logistic Regression Model Dashboard"),
    
    # Display model summary as text
    html.Div([
        html.H3("Model Summary"),
        html.Pre(result.summary().as_text())
    ]),
    
    # Interactive plot for coefficients and odds ratios
    html.Div([
        html.H3("Coefficients & Odds Ratios"),
        dcc.Graph(
            id="coef-odds-ratios-plot"
        )
    ]),
    
    # Interactive plot for p-values
    html.Div([
        html.H3("P-values"),
        dcc.Graph(
            id="p-value-plot"
        )
    ])
])

# Callback to update the plots
@app.callback(
    [Output("coef-odds-ratios-plot", "figure"),
     Output("p-value-plot", "figure")],
    Input('coef-odds-ratios-plot', 'id')  # Trigger updates when the page loads
)
def update_plots(_):
    # Coefficients and odds ratios plot
    coef_figure = go.Figure()
    coef_figure.add_trace(go.Bar(
        x=coefficients.index,
        y=coefficients.values,
        name='Coefficients'
    ))
    coef_figure.add_trace(go.Bar(
        x=odds_ratios.index,
        y=odds_ratios.values,
        name='Odds Ratios',
        marker=dict(color='rgba(246, 78, 139, 0.6)')
    ))
    coef_figure.update_layout(
        title="Model Coefficients vs. Odds Ratios",
        xaxis_title="Variables",
        yaxis_title="Values",
        barmode="group"
    )

    # P-values plot
    p_value_figure = go.Figure()
    p_value_figure.add_trace(go.Bar(
        x=p_values.index,
        y=p_values.values,
        name='P-values',
        marker=dict(color='rgba(55, 128, 191, 0.6)')
    ))
    p_value_figure.update_layout(
        title="P-values for Each Predictor",
        xaxis_title="Variables",
        yaxis_title="P-value",
        showlegend=False
    )

    return coef_figure, p_value_figure

if __name__ == '__main__':
    app.run(debug=True)
