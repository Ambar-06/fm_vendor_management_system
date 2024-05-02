from common.boilerplate.db.base_repository import BaseRepository
from vendor.models.vendor import Vendor


class VendorRepository(BaseRepository):
    
    def __init__(self):
        self.model = Vendor