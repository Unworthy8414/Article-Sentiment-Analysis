import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

with open("articles_data.json") as f:
    articles = json.load(f)

news = pd.DataFrame(articles)

news["date"] = pd.to_datetime(news["date"])
news["date_str"] = news["date"].dt.strftime('%Y-%m-%d')

date_mapping = {date_str: i for i, date_str in enumerate(news["date_str"].unique())}

news["date_float"] = news["date_str"].map(date_mapping)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(news["date_float"], news["polarity"], news["subjectivity"], c=news["polarity"], cmap="RdYlGn")
ax.set_xlabel("Date")
ax.set_ylabel("Polarity")
ax.set_zlabel("Subjectivity")

x_tick_labels = list(date_mapping.keys())[::2]
x_tick_positions = np.arange(0, len(date_mapping), 2)

ax.set_xticks(x_tick_positions)
ax.set_xticklabels(x_tick_labels, rotation=90)

plt.title("Sentiment Analysis of News Articles")
plt.show()