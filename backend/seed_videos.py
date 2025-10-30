import requests
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.sqlalchemy_models import Video
import os

# Manually extracted data from Frontend/src/data/mockData.ts
all_movies_data = [
    {
        "id": 1,
        "title": "Nebula Rising",
        "thumbnail": "https://images.pexels.com/photos/2873486/pexels-photo-2873486.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2873486/pexels-photo-2873486.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A thrilling space adventure that follows a crew of explorers as they venture into uncharted territories of the cosmos, discovering ancient civilizations and facing impossible odds.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 18m",
        "genre": ["Sci-Fi", "Adventure", "Thriller"]
    },
    {
        "id": 2,
        "title": "Shadow Protocol",
        "thumbnail": "https://images.pexels.com/photos/4553618/pexels-photo-4553618.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/4553618/pexels-photo-4553618.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An elite agent must uncover a global conspiracy that threatens the very fabric of international security. Time is running out, and trust is a luxury no one can afford.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 5m",
        "genre": ["Action", "Thriller", "Mystery"]
    },
    {
        "id": 3,
        "title": "Eternal Sunset",
        "thumbnail": "https://images.pexels.com/photos/1666073/pexels-photo-1666073.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1666073/pexels-photo-1666073.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A poignant love story that transcends time and space, following two souls destined to find each other across multiple lifetimes.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 58m",
        "genre": ["Romance", "Drama", "Fantasy"]
    },
    {
        "id": 4,
        "title": "Urban Legends",
        "thumbnail": "https://images.pexels.com/photos/3137078/pexels-photo-3137078.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3137078/pexels-photo-3137078.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "When ancient myths start manifesting in a modern metropolis, a group of unlikely heroes must band together to save their city from supernatural forces.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 12m",
        "genre": ["Fantasy", "Action", "Adventure"]
    },
    {
        "id": 5,
        "title": "The Last Algorithm",
        "thumbnail": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "In a world controlled by artificial intelligence, one programmer discovers a hidden code that could either free humanity or doom it forever.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 22m",
        "genre": ["Sci-Fi", "Thriller", "Drama"]
    },
    {
        "id": 6,
        "title": "Velocity",
        "thumbnail": "https://images.pexels.com/photos/210887/pexels-photo-210887.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/210887/pexels-photo-210887.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "High-octane racing meets international espionage in this adrenaline-pumping thriller.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 8m",
        "genre": ["Action", "Thriller"]
    },
    {
        "id": 7,
        "title": "Iron Phoenix",
        "thumbnail": "https://images.pexels.com/photos/3380743/pexels-photo-3380743.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3380743/pexels-photo-3380743.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A retired special forces operative is forced back into action to rescue hostages from a heavily fortified compound.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Action", "Adventure"]
    },
    {
        "id": 8,
        "title": "Storm Chasers",
        "thumbnail": "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Elite pilots navigate through deadly weather conditions to complete an impossible mission.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "2h 15m",
        "genre": ["Action", "Adventure", "Thriller"]
    },
    {
        "id": 9,
        "title": "Reckoning",
        "thumbnail": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A vigilante seeks justice for his family in a city ruled by corruption and crime.",
        "year": 2023,
        "rating": "R",
        "duration": "2h 3m",
        "genre": ["Action", "Crime", "Thriller"]
    },
    {
        "id": 10,
        "title": "Tactical Force",
        "thumbnail": "https://images.pexels.com/photos/1701208/pexels-photo-1701208.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1701208/pexels-photo-1701208.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An elite military unit must infiltrate enemy territory to prevent a global catastrophe.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 58m",
        "genre": ["Action", "War", "Thriller"]
    },
    {
        "id": 11,
        "title": "Laugh Track",
        "thumbnail": "https://images.pexels.com/photos/1115816/pexels-photo-1115816.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1115816/pexels-photo-1115816.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A struggling comedian gets an unexpected chance at stardom when a viral video changes everything.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 42m",
        "genre": ["Comedy", "Drama"]
    },
    {
        "id": 12,
        "title": "Office Chaos",
        "thumbnail": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "When an office prank goes too far, coworkers must work together to fix the hilarious mess they've created.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "1h 38m",
        "genre": ["Comedy"]
    },
    {
        "id": 13,
        "title": "Family Reunion",
        "thumbnail": "https://images.pexels.com/photos/1128318/pexels-photo-1128318.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1128318/pexels-photo-1128318.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A dysfunctional family comes together for the holidays, leading to comedic disasters and heartwarming moments.",
        "year": 2023,
        "rating": "PG",
        "duration": "1h 55m",
        "genre": ["Comedy", "Family"]
    },
    {
        "id": 14,
        "title": "The Mix-Up",
        "thumbnail": "https://images.pexels.com/photos/1157557/pexels-photo-1157557.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1157557/pexels-photo-1157557.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Mistaken identities lead to a series of hilarious misadventures in this romantic comedy.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 48m",
        "genre": ["Comedy", "Romance"]
    },
    {
        "id": 15,
        "title": "Road Trip Madness",
        "thumbnail": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Best friends embark on a cross-country road trip that tests their friendship and sanity.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Comedy", "Adventure"]
    },
    {
        "id": 16,
        "title": "Broken Dreams",
        "thumbnail": "https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A powerful story of redemption and resilience as one man rebuilds his life after losing everything.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 28m",
        "genre": ["Drama"]
    },
    {
        "id": 17,
        "title": "The Portrait",
        "thumbnail": "https://images.pexels.com/photos/1212407/pexels-photo-1212407.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1212407/pexels-photo-1212407.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An artist struggles with fame and identity while creating her masterpiece.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "2h 5m",
        "genre": ["Drama", "Biography"]
    },
    {
        "id": 18,
        "title": "Silent Echoes",
        "thumbnail": "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A haunting exploration of memory and loss as a woman confronts her past.",
        "year": 2023,
        "rating": "R",
        "duration": "2h 12m",
        "genre": ["Drama", "Mystery"]
    },
    {
        "id": 19,
        "title": "The Teacher",
        "thumbnail": "https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An inspiring teacher transforms the lives of students in an underprivileged community.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 1m",
        "genre": ["Drama", "Biography"]
    },
    {
        "id": 20,
        "title": "Crossroads",
        "thumbnail": "https://images.pexels.com/photos/1309766/pexels-photo-1309766.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1309766/pexels-photo-1309766.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Three strangers' lives intersect in unexpected ways, changing their destinies forever.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 18m",
        "genre": ["Drama"]
    },
    {
        "id": 21,
        "title": "The Awakening",
        "thumbnail": "https://images.pexels.com/photos/2693529/pexels-photo-2693529.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2693529/pexels-photo-2693529.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An ancient evil awakens in a small town, and only a group of teenagers can stop it.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 48m",
        "genre": ["Horror", "Thriller"]
    },
    {
        "id": 22,
        "title": "Dark Waters",
        "thumbnail": "https://images.pexels.com/photos/1029624/pexels-photo-1029624.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1029624/pexels-photo-1029624.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Something sinister lurks beneath the surface of a peaceful lakeside resort.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 55m",
        "genre": ["Horror", "Mystery"]
    },
    {
        "id": 23,
        "title": "The Haunting of Elm Street",
        "thumbnail": "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A family moves into their dream home, only to discover they're not alone.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 42m",
        "genre": ["Horror"]
    },
    {
        "id": 24,
        "title": "Whispers",
        "thumbnail": "https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A psychiatrist treating a disturbed patient begins experiencing terrifying visions.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Horror", "Thriller", "Mystery"]
    },
    {
        "id": 25,
        "title": "The Ritual",
        "thumbnail": "https://images.pexels.com/photos/2693212/pexels-photo-2693212.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2693212/pexels-photo-2693212.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A group of friends on a hiking trip stumble upon a terrifying ancient ceremony.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 58m",
        "genre": ["Horror", "Thriller"]
    }
]

import requests
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.sqlalchemy_models import Video
import os

# Manually extracted data from Frontend/src/data/mockData.ts
all_movies_data = [
    {
        "id": 1,
        "title": "Nebula Rising",
        "thumbnail": "https://images.pexels.com/photos/2873486/pexels-photo-2873486.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2873486/pexels-photo-2873486.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A thrilling space adventure that follows a crew of explorers as they venture into uncharted territories of the cosmos, discovering ancient civilizations and facing impossible odds.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 18m",
        "genre": ["Sci-Fi", "Adventure", "Thriller"]
    },
    {
        "id": 2,
        "title": "Shadow Protocol",
        "thumbnail": "https://images.pexels.com/photos/4553618/pexels-photo-4553618.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/4553618/pexels-photo-4553618.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An elite agent must uncover a global conspiracy that threatens the very fabric of international security. Time is running out, and trust is a luxury no one can afford.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 5m",
        "genre": ["Action", "Thriller", "Mystery"]
    },
    {
        "id": 3,
        "title": "Eternal Sunset",
        "thumbnail": "https://images.pexels.com/photos/1666073/pexels-photo-1666073.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1666073/pexels-photo-1666073.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A poignant love story that transcends time and space, following two souls destined to find each other across multiple lifetimes.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 58m",
        "genre": ["Romance", "Drama", "Fantasy"]
    },
    {
        "id": 4,
        "title": "Urban Legends",
        "thumbnail": "https://images.pexels.com/photos/3137078/pexels-photo-3137078.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3137078/pexels-photo-3137078.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "When ancient myths start manifesting in a modern metropolis, a group of unlikely heroes must band together to save their city from supernatural forces.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 12m",
        "genre": ["Fantasy", "Action", "Adventure"]
    },
    {
        "id": 5,
        "title": "The Last Algorithm",
        "thumbnail": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "In a world controlled by artificial intelligence, one programmer discovers a hidden code that could either free humanity or doom it forever.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 22m",
        "genre": ["Sci-Fi", "Thriller", "Drama"]
    },
    {
        "id": 6,
        "title": "Velocity",
        "thumbnail": "https://images.pexels.com/photos/210887/pexels-photo-210887.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/210887/pexels-photo-210887.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "High-octane racing meets international espionage in this adrenaline-pumping thriller.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 8m",
        "genre": ["Action", "Thriller"]
    },
    {
        "id": 7,
        "title": "Iron Phoenix",
        "thumbnail": "https://images.pexels.com/photos/3380743/pexels-photo-3380743.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3380743/pexels-photo-3380743.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A retired special forces operative is forced back into action to rescue hostages from a heavily fortified compound.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Action", "Adventure"]
    },
    {
        "id": 8,
        "title": "Storm Chasers",
        "thumbnail": "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Elite pilots navigate through deadly weather conditions to complete an impossible mission.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "2h 15m",
        "genre": ["Action", "Adventure", "Thriller"]
    },
    {
        "id": 9,
        "title": "Reckoning",
        "thumbnail": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A vigilante seeks justice for his family in a city ruled by corruption and crime.",
        "year": 2023,
        "rating": "R",
        "duration": "2h 3m",
        "genre": ["Action", "Crime", "Thriller"]
    },
    {
        "id": 10,
        "title": "Tactical Force",
        "thumbnail": "https://images.pexels.com/photos/1701208/pexels-photo-1701208.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1701208/pexels-photo-1701208.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An elite military unit must infiltrate enemy territory to prevent a global catastrophe.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 58m",
        "genre": ["Action", "War", "Thriller"]
    },
    {
        "id": 11,
        "title": "Laugh Track",
        "thumbnail": "https://images.pexels.com/photos/1115816/pexels-photo-1115816.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1115816/pexels-photo-1115816.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A struggling comedian gets an unexpected chance at stardom when a viral video changes everything.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 42m",
        "genre": ["Comedy", "Drama"]
    },
    {
        "id": 12,
        "title": "Office Chaos",
        "thumbnail": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "When an office prank goes too far, coworkers must work together to fix the hilarious mess they've created.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "1h 38m",
        "genre": ["Comedy"]
    },
    {
        "id": 13,
        "title": "Family Reunion",
        "thumbnail": "https://images.pexels.com/photos/1128318/pexels-photo-1128318.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1128318/pexels-photo-1128318.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A dysfunctional family comes together for the holidays, leading to comedic disasters and heartwarming moments.",
        "year": 2023,
        "rating": "PG",
        "duration": "1h 55m",
        "genre": ["Comedy", "Family"]
    },
    {
        "id": 14,
        "title": "The Mix-Up",
        "thumbnail": "https://images.pexels.com/photos/1157557/pexels-photo-1157557.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1157557/pexels-photo-1157557.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Mistaken identities lead to a series of hilarious misadventures in this romantic comedy.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "1h 48m",
        "genre": ["Comedy", "Romance"]
    },
    {
        "id": 15,
        "title": "Road Trip Madness",
        "thumbnail": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1659438/pexels-photo-1659438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Best friends embark on a cross-country road trip that tests their friendship and sanity.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Comedy", "Adventure"]
    },
    {
        "id": 16,
        "title": "Broken Dreams",
        "thumbnail": "https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A powerful story of redemption and resilience as one man rebuilds his life after losing everything.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 28m",
        "genre": ["Drama"]
    },
    {
        "id": 17,
        "title": "The Portrait",
        "thumbnail": "https://images.pexels.com/photos/1212407/pexels-photo-1212407.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1212407/pexels-photo-1212407.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An artist struggles with fame and identity while creating her masterpiece.",
        "year": 2023,
        "rating": "PG-13",
        "duration": "2h 5m",
        "genre": ["Drama", "Biography"]
    },
    {
        "id": 18,
        "title": "Silent Echoes",
        "thumbnail": "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A haunting exploration of memory and loss as a woman confronts her past.",
        "year": 2023,
        "rating": "R",
        "duration": "2h 12m",
        "genre": ["Drama", "Mystery"]
    },
    {
        "id": 19,
        "title": "The Teacher",
        "thumbnail": "https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An inspiring teacher transforms the lives of students in an underprivileged community.",
        "year": 2024,
        "rating": "PG-13",
        "duration": "2h 1m",
        "genre": ["Drama", "Biography"]
    },
    {
        "id": 20,
        "title": "Crossroads",
        "thumbnail": "https://images.pexels.com/photos/1309766/pexels-photo-1309766.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1309766/pexels-photo-1309766.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Three strangers' lives intersect in unexpected ways, changing their destinies forever.",
        "year": 2024,
        "rating": "R",
        "duration": "2h 18m",
        "genre": ["Drama"]
    },
    {
        "id": 21,
        "title": "The Awakening",
        "thumbnail": "https://images.pexels.com/photos/2693529/pexels-photo-2693529.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2693529/pexels-photo-2693529.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "An ancient evil awakens in a small town, and only a group of teenagers can stop it.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 48m",
        "genre": ["Horror", "Thriller"]
    },
    {
        "id": 22,
        "title": "Dark Waters",
        "thumbnail": "https://images.pexels.com/photos/1029624/pexels-photo-1029624.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1029624/pexels-photo-1029624.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "Something sinister lurks beneath the surface of a peaceful lakeside resort.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 55m",
        "genre": ["Horror", "Mystery"]
    },
    {
        "id": 23,
        "title": "The Haunting of Elm Street",
        "thumbnail": "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A family moves into their dream home, only to discover they're not alone.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 42m",
        "genre": ["Horror"]
    },
    {
        "id": 24,
        "title": "Whispers",
        "thumbnail": "https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A psychiatrist treating a disturbed patient begins experiencing terrifying visions.",
        "year": 2023,
        "rating": "R",
        "duration": "1h 52m",
        "genre": ["Horror", "Thriller", "Mystery"]
    },
    {
        "id": 25,
        "title": "The Ritual",
        "thumbnail": "https://images.pexels.com/photos/2693212/pexels-photo-2693212.jpeg?auto=compress&cs=tinysrgb&w=800",
        "backdrop": "https://images.pexels.com/photos/2693212/pexels-photo-2693212.jpeg?auto=compress&cs=tinysrgb&w=1920",
        "description": "A group of friends on a hiking trip stumble upon a terrifying ancient ceremony.",
        "year": 2024,
        "rating": "R",
        "duration": "1h 58m",
        "genre": ["Horror", "Thriller"]
    }
]

BASE_URL = "http://127.0.0.1:8008/api/v1/videos"

def seed_videos():
    db: Session = next(get_db())
    try:
        # Clear existing videos
        db.query(Video).delete()
        db.commit()
        print("Cleared existing video data.")

        for movie_data in all_movies_data:
            # Extract just the filename from the full path
            video_urls = [
                "http://localhost:8008/static/video2.mp4",
                "http://localhost:8008/static/video3.mp4",
                "http://localhost:8008/static/video4.mp4",
                "http://localhost:8008/static/video5.mp4",
                "http://localhost:8008/static/video6.mp4",
            ]
            
            # Use modulo to cycle through the video_urls based on movie_data['id']
            # For IDs 1-6, use the first 6 videos (index 0-5)
            # For IDs 7-13, use the same videos again (index 0-5)
            # The modulo operator handles the cycling
            video_url_for_db = video_urls[(movie_data['id'] - 1) % len(video_urls)]

            payload = {
                "title": movie_data["title"],
                "description": movie_data["description"],
                "year": movie_data["year"],
                "rating": movie_data["rating"],
                "duration": movie_data["duration"],
                "category": ", ".join(movie_data["genre"]),
                "video_url": video_url_for_db,
                "thumbnail_url": movie_data["thumbnail"],
                "backdrop_url": movie_data["backdrop"]
            }
            
            try:
                response = requests.post(BASE_URL, json=payload)
                response.raise_for_status() # Raise an exception for HTTP errors
                print(f"Successfully added video: {movie_data["title"]}")
            except requests.exceptions.HTTPError as err:
                print(f"Error adding video {movie_data["title"]}: {err}")
                print(f"Response: {response.json()}")
            except requests.exceptions.ConnectionError as err:
                print(f"Connection error: {err}. Is the backend running?")
                break # Stop if there's a connection error
    finally:
        db.close()

if __name__ == "__main__":
    seed_videos()


