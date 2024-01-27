import spacy

def extract_key_information(news_article):
    # Load the spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the news article text
    doc = nlp(news_article)

    # Extract key information (e.g., named entities)
    key_info = []

    for ent in doc.ents:
        key_info.append({
            "text": ent.text,
            "label": ent.label_
        })

    return key_info

if __name__ == "__main__":
    # Example news article
    news_article = "Your news article text goes here."

    # Extract key information
    key_information = extract_key_information(news_article)

    # Print the extracted information
    print("Key Information:")
    for info in key_information:
        print(f"Text: {info['text']}, Label: {info['label']}")