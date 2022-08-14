import datetime
import pymongo

def init_connection():
    
    conn_str = 'mongodb+srv://invezto_74687:PUfDDD6lwmUoG5bp@cluster0.srlwykp.mongodb.net/?retryWrites=true&w=majority'
    
    client = pymongo.MongoClient(conn_str)
    print('Database Connected')
    database = client.Stock_Price
    return database


def set_data(name, dataframe):
    db = init_connection()
    new_name = name + str(datetime.datetime.now());
    db.create_collection(new_name)
    my_collection = db.get_collection(new_name)
    my_collection.insert_many(dataframe.to_dict('records'))
    return