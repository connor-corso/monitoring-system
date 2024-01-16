from sqlalchemy.orm import Session

from . import models, schemas


#####################################################################
## data entry methods
def create_data_entry(db: Session):
    pass

def get_data_entries(db: Session):
    pass

def get_data_entry(db: Session):
    pass

#####################################################################
## data grouping methods
def create_data_grouping(db: Session):
    pass

def get_data_groupings(db: Session):
    pass

def edit_data_grouping(db: Session):
    pass

def add_data_station_to_grouping(db: Session):
    pass

def remove_data_station_from_grouping(db: Session):
    pass

#####################################################################
## data station methods

def create_data_station(db: Session):
    pass

def get_data_stations(db: Session):
    pass

def edit_data_station(db: Session):
    pass

# I'm not too sure on these methods yet. If I don't use them then by default a data entry will be bound to a blank station
# With these methods it would allow me to have the data entries not be bound to a station and I could keep them in a limbo state. This is probably hard to track
def register_data_entry_to_station(db: Session):
    pass

def remove_data_entry_from_station(db: Session):
    pass
