import pandas as pd
import json
from collections import defaultdict

def generate_intents_from_tweets(csv_path, output_path="data/intents.json"):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["text", "inbound"])

    df['inbound'] = df['inbound'].astype(bool)

    intent_data = defaultdict(lambda: {"patterns": [], "responses": []})

    for _, row in df.iterrows():
        if row['inbound']:
            intent_tag = "twitter_support"  
            intent_data[intent_tag]["patterns"].append(row["text"].strip())
        else:
            resp = row.get("text", "").strip()
            if resp:
                intent_data["twitter_support"]["responses"].append(resp)

    if not intent_data["twitter_support"]["responses"]:
        intent_data["twitter_support"]["responses"] = [
            "Thank you for your message. We're reviewing it and will get back to you shortly."
        ]

    final_intents = {
        "intents": [
            {"tag": tag, "patterns": data["patterns"], "responses": data["responses"]}
            for tag, data in intent_data.items()
        ]
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_intents, f, indent=2)

    print(f"✅ Created intents.json with {len(final_intents['intents'])} intent(s)")



generate_intents_from_tweets("data/chatbot_data.csv")