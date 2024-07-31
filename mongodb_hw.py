from pymongo.mongo_client import MongoClient
from config import USER_NAME, PASSWORD
from pymongo.server_api import ServerApi

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.nsbj61q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['new_db']

fantasy_books_coll = db['fantasy_books']
school_books_coll = db['school_books']

fantasy_books_coll.insert_one({
    'title': 'Game of Thrones',
    'price': 700,
    'graduation_year': 1996,
    'pages': 864

})

school_books = [

    {'title': 'History', 'class': 2014, 'pages': 228},

    {'title': 'Math', 'class': 2020, 'pages': 230},

    {'title': 'Biologie', 'class': 2016, 'pages': 170},

    {'title': 'Physik', 'class': 2022, 'pages': 218},

    {'title': 'Geography', 'class': 2017, 'pages': 146},

    {'title': 'Computer Science', 'class': 2019, 'pages': 300}

]

school_books_coll.insert_many(school_books)

# query = {
#
#     'title': {'$regex': 'History*'}
#
# }
#
# result = school_books_coll.find_one(query)
# print(result)


# fantasy_books_coll.drop()
# school_books_coll.drop()

