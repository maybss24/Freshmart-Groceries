from dataclasses import dataclass
from datetime import datetime

@dataclass
class Employee:
    fullname: str
    birthdate: datetime
    address: str
    contact_number: str
    emergency_number: str
    
    def to_dict(self):
        return {
            'fullname': self.fullname,
            'birthdate': self.birthdate.strftime('%Y-%m-%d'),
            'address': self.address,
            'contact_number': self.contact_number,
            'emergency_number': self.emergency_number
        }
