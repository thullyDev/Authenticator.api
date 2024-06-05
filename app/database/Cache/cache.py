from typing import Any, Dict, List, Optional, Union
from app.resources.config import REDIS_URL
from redis import Redis
import ast
import json

redis = Redis().from_url(REDIS_URL)
_24hour_expiry = 86400 

class Cache:
    _instance = None  
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance
        

    def get(self, name: str) -> Optional[str]: 
        rdata: Any = redis.get(name)
        
        if not rdata: return None
        
        return rdata.decode()
        
    def hget(self, name: str, *, is_list: bool =False) -> Union[Dict, List, None]:
        rdata: Any = redis.get(name)

        if not rdata: return None

        rdata =  rdata.decode()

        if is_list:
            return ast.literal_eval(rdata)

        return json.loads(rdata) 

    def set(self, name: str, value: str, expiry=_24hour_expiry) -> None:
        if expiry: 
            redis.set(name, value, expiry)
            return 

        redis.set(name, value)
        
    def hset(self, name: str, data, expiry=_24hour_expiry) -> None:
        value = json.dumps(data)
        self.set(name=name, value=value, expiry=expiry)

    def mset(self, data) -> None: redis.mset(data)
        
    def delete(self, name: str) -> None: redis.delete(name)