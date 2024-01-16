from pydantic import BaseModel

class DataEntryBase(BaseModel):
    pass

class DataEntryCreate(BaseModel):
    pass

class DataEntry(BaseModel):
    pass


class DataStationBase(BaseModel):
    pass

class DataStationCreate(BaseModel):
    pass

class DataStation(BaseModel):
    pass



class DataGroupingBase(BaseModel):
    pass

class DataGroupingCreate(BaseModel):
    pass

class DataGrouping(BaseModel):
    pass
