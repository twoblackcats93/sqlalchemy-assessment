"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.
mo
"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?  An object.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage? An association table is a table whose fields serve
# as "the glue" that connects to other tables.  It is like the "pass through"
# or "go between" that a table must go through in order to access another table's
# information.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id == 'ram').first()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 =  Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like ('Cor%')).all()
# I also tried this query 
# Model.query.filter(Model.name.like ('%Cor%')).all()
# and got the same results but think that what I submitted
# is more accurate as there could be a brand that had two names
# and the second name starts with Cor which will not be the 
# right result.

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(db.or_(Brand.discontinued != None, Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()
# alternative 
# Model.query.filter(db.not_(Model.brand_id == 'for')).all()
# I found this more complex



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    
    # query both Brand and Model classes, get a list of tuples
    brand_model_info = db.session.query(Brand, Model).all()

    # loop through tuples and get the brand name, HQ, model for a given year
    for brand, model in brand_model_info:
        if model.year == year:
            print "In the year %d, %s, based in %s produced the model %s." \
            % (year, brand.name, brand.headquarters, model.name) 


# def get_brands_summary():
#     """Prints out each brand name (once) and all of that brand's models,
#     including their year, using only ONE database query."""
    
#     # create empty dictionary
#     brands_summary = {}
    
#     # create query that produces tuples
#     brand_model_year = db.session.query(Brand.name, Model.name, Model.year).all()
    
#     # # loop through tuples and set dict key and values
#     # for items in brand_model_year:
#     #     dict_key = items[0]
#     #     dict_value = (items[1], items[2])

#     #     if dict_key not in brands_summary:
#     #         brands_summary[dict_key] = []
#     #     else:
#     #         brands_summary[dict_key].append(dict_value)      
    
#     # return brands_summary

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_name = Brand.query.filter(Brand.name == mystr).all()
    return brand_name


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    
    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
    return models
 
