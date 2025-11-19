from abc import ABC, abstractmethod

class IProductRepository(ABC):

    @abstractmethod
    def get_all_products(self) -> dict:
        pass

    
    @abstractmethod
    def update_product_by_code_to_zero(self, code: str):
        pass