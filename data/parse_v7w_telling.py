import string
import json
import pandas as pd

def process_dict(d, output):
    if isinstance(d, dict):
        if "multiple_choices" in d and "answer" in d and "question" in d:
            # Check if "multiple_choices" values and "answer" are integers (after stripping punctuation)
            mc = [s.translate(str.maketrans('', '', string.punctuation)) for s in d["multiple_choices"]]
            ans = d["answer"].translate(str.maketrans('', '', string.punctuation))
            question = d["question"]
            if all(x.isdigit() for x in mc) and ans.isdigit() and question.startswith("How many"):
                # Add "multiple_choices" and "answer" to the output list
                for choice in mc:
                    output.append({
                        "image_id": d["image_id"],
                        "question": d["question"],
                        "answer": int(choice),
                        "label": False
                    })
                output.append({
                    "image_id": d["image_id"],
                    "question": d["question"],
                    "answer": int(ans),
                    "label": True
                })
        
        # Recursively process each item in the dictionary
        for v in d.values():
            process_dict(v, output)
    elif isinstance(d, list):
        # Recursively process each item in the list
        for v in d:
            process_dict(v, output)
    return output

def main():
    with open("data/v7w_telling/dataset_v7w_telling.json", "r") as f:
        telling_dataset = json.load(f)

    dataset = process_dict(telling_dataset, [])

    df = pd.DataFrame(dataset)
    df = df[df["answer"] <= 20 ]
    df = df.groupby(by=["answer"]).head(200)
    df = df.reset_index(drop=True)
    df['prompts'] = df['question'].combine(df['answer'], lambda x, y: f"{x} {y}")
    df.to_csv("data/v7w_telling/v7w_telling.csv", index=False)
    df['prompts'].to_csv("data/v7w_telling/v7w_telling_prompts.csv", index=False, header=False)

if __name__ == "__main__":
    main()