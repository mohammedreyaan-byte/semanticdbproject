METRICS = {
    "total_books" : {
        "field" : "book_id",
        "aggregation" : "COUNT",
        "description" : "Total number of books"
    },

    "max_ratings":{
        "field" : "ratings",
        "aggregation" : "MAX",
        "description" : "Highest Rated books"
    },

    "books_with_description" : {
        "field" : "description",
        "aggregation" : "COUNT",
        "description" : "Total number of books with description"
    }



}