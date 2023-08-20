"""
new example to explain the use of query and path params
"""
from fastapi import FastAPI

app = FastAPI()

animals_data = {
    "cat": [
        "Cats can jump up to 6 times their height.",
        "They have a total of 18 toes.",
        "There are over 500 million pet cats",
    ],
    "dog": [
        "Their sense of smell is at least 40x better than ours",
        "Some have such good noses they can sniff out medical problems",
        " Dogs can sniff at the same time as breathing",
    ],
    "cow": [
        "Cows have a strong sense of smell.",
        "They can perceive smells at a distance of up to ten kilometres.",
        "Compared to the hearing of humans, the hearing ability of cows is better in the deep and high frequency ranges.",
        "Cows are moving constantly during grazing and can cover 13 km per day.",
    ],
    "goat": [
        "Goats are social animals",
        "Cleanliness is important to them",
        "They're emotionally intelligent",
        "They're quick learners.",
    ],
}


@app.get("/search/{data}")
def google_search(data: str):
    if data in animals_data:
        return animals_data[data]
    else:
        return {"info not found about perticular data"}
