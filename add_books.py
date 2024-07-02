#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book
from dotenv import load_dotenv
import os

load_dotenv('.env')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1209, 15, "A novel set in the Jazz Age that tells the story of the mysterious millionaire Jay Gatsby and his obsession with Daisy Buchanan.", "Fiction"),
    ("To Kill a Mockingbird", "Harper Lee", 879, 10, "A story of racial injustice and childhood innocence set in the American South during the 1930s.", "Fiction"),
    ("1984", "George Orwell", 989, 12, "A dystopian novel exploring the dangers of totalitarianism and extreme political ideology.", "Fiction"),
    ("Pride and Prejudice", "Jane Austen", 769, 20, "A classic romance novel that also critiques the British landed gentry at the end of the 18th century.", "Fiction"),
    ("The Catcher in the Rye", "J.D. Salinger", 1099, 18, "A story about teenage rebellion and alienation, narrated by the iconic Holden Caulfield.", "Fiction"),
    ("The Road", "Cormac McCarthy", 1319, 10, "A post-apocalyptic novel that follows a father and son's journey through a desolate America.", "Fiction"),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson", 1429, 8, "A gripping mystery involving a journalist and a hacker who investigate a disappearance.", "Mystery"),
    ("Gone Girl", "Gillian Flynn", 1209, 14, "A thriller about a woman's disappearance and the dark secrets that come to light.", "Mystery"),
    ("The Da Vinci Code", "Dan Brown", 1099, 16, "A mystery thriller that delves into secret societies and hidden messages in famous artworks.", "Mystery"),
    ("Big Little Lies", "Liane Moriarty", 1209, 12, "A story of three women whose seemingly perfect lives unravel to the point of murder.", "Mystery"),
    ("In the Woods", "Tana French", 989, 10, "A psychological mystery involving a detective haunted by a traumatic childhood event.", "Mystery"),
    ("The Silent Patient", "Alex Michaelides", 1649, 9, "A psychological thriller about a woman who stops speaking after being accused of murdering her husband.", "Mystery"),
    ("Dune", "Frank Herbert", 1759, 13, "A science fiction epic set on the desert planet Arrakis, focusing on politics, religion, and ecology.", "Sci-Fi"),
    ("Neuromancer", "William Gibson", 1319, 11, "A cyberpunk novel that explores artificial intelligence, virtual reality, and corporate espionage.", "Sci-Fi"),
    ("Ender's Game", "Orson Scott Card", 879, 20, "A young boy is trained to be a military leader in a future war against an alien race.", "Sci-Fi"),
    ("The Left Hand of Darkness", "Ursula K. Le Guin", 1099, 15, "A science fiction novel exploring themes of gender and sexuality on a distant planet.", "Sci-Fi"),
    ("Snow Crash", "Neal Stephenson", 1539, 7, "A fast-paced cyberpunk novel involving a computer virus that affects the real world.", "Sci-Fi"),
    ("Foundation", "Isaac Asimov", 1209, 18, "A science fiction series about the fall and rise of a Galactic Empire, focusing on the use of psychohistory to predict the future.", "Sci-Fi"),
    ("The Hobbit", "J.R.R. Tolkien", 989, 25, "The prelude to 'The Lord of the Rings,' this novel follows Bilbo Baggins on an epic quest.", "Fantasy"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1099, 30, "The first book in the Harry Potter series, introducing the young wizard and his adventures at Hogwarts.", "Fantasy"),
    ("A Game of Thrones", "George R.R. Martin", 1429, 20, "The first book in the 'A Song of Ice and Fire' series, filled with political intrigue, warfare, and dragons.", "Fantasy"),
    ("The Name of the Wind", "Patrick Rothfuss", 1649, 15, "A fantasy novel about the life and adventures of a gifted young man named Kvothe.", "Fantasy"),
    ("Mistborn: The Final Empire", "Brandon Sanderson", 1319, 18, "A fantasy novel set in a world where ash falls from the sky and mist dominates the night, focusing on a rebellion against the Lord Ruler.", "Fantasy"),
    ("The Way of Kings", "Brandon Sanderson", 1869, 12, "The first book in 'The Stormlight Archive' series, featuring a richly detailed world and complex characters.", "Fantasy"),
    ("Pride and Prejudice", "Jane Austen", 769, 25, "A classic romance novel that also critiques the British landed gentry at the end of the 18th century.", "Romance"),
    ("Outlander", "Diana Gabaldon", 1209, 20, "A time-travel romance that follows Claire Randall as she is transported from 1945 to 1743 Scotland.", "Romance"),
    ("Me Before You", "Jojo Moyes", 1099, 15, "A heart-wrenching romance about a young woman who becomes a caregiver for a man paralyzed in an accident.", "Romance"),
    ("The Notebook", "Nicholas Sparks", 879, 18, "A romantic drama about a couple who fall in love in the early 20th century, and their enduring love story.", "Romance"),
    ("The Hating Game", "Sally Thorne", 989, 12, "A romantic comedy about two coworkers who start as rivals but find themselves falling in love.", "Romance"),
    ("Twilight", "Stephenie Meyer", 1099, 22, "A young adult romance involving a teenage girl and a vampire, sparking a worldwide phenomenon.", "Romance"),
    ("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 1649, 20, "A comprehensive history of the human species, from the Stone Age to the modern era.", "Non-Fiction"),
    ("Educated", "Tara Westover", 1319, 15, "A memoir about a woman who grows up in a strict and abusive household in rural Idaho but eventually escapes to learn about the wider world through education.", "Non-Fiction"),
    ("Becoming", "Michelle Obama", 1869, 10, "The former First Lady of the United States recounts her life story, from her childhood to her years in the White House.", "Non-Fiction"),
    ("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", 1539, 12, "The story of Henrietta Lacks and the immortal cell line (HeLa) taken without her knowledge, which became one of the most important tools in medicine.", "Non-Fiction"),
    ("The Wright Brothers", "David McCullough", 1649, 8, "A biography of the Wright brothers, who are credited with inventing and building the world's first successful airplane.", "Non-Fiction"),
    ("Thinking, Fast and Slow", "Daniel Kahneman", 1319, 18, "A renowned psychologist explains the two systems that drive the way we think, offering insights into how we make decisions.", "Non-Fiction")
]

for title, author, price, quantity, description, genre in books:
    new_book = Book(title=title, author=author, price=price, quantity=quantity, description=description)
    session.add(new_book)

session.commit()
