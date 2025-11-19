from src.model.database.firebase.repositories.interface.product_repository_interface import IProductRepository
from src.main.http_types.http_response.http_response import HttpResponse
from src.errors.types.http_error_server import HttpErrorServer
from .interface.reset_stock_product_use_case_interface import IResetStockProductUseCase

class ResetStockProductUseCase(IResetStockProductUseCase):

    def __init__(self, repository: IProductRepository) -> None:
        
        self.__repository = repository
    
    
    def handle(self) -> HttpResponse:

        try:
            
            products = self.__get_all_products()

            code_list = self.__get_code_list(products)

            self.__update_stock(code_list)

            formatted_response = self.__format_response(code_list)

            return formatted_response

        except Exception as exception:
            
            print(f"Error Server: {str(exception)}")

            raise HttpErrorServer("Error Server")
        
    
    def __get_all_products(self) -> dict:

        return self.__repository.get_all_products()

    
    def __get_code_list(self, products: dict) -> list:

        code_list = []

        for code in products:

            code_list.append(code)
        
        return code_list
    

    def __update_stock(self, codes: list) -> None:

        for code in codes:
            
            self.__repository.update_product_by_code_to_zero(code)
    

    def __format_response(self, codes: list) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation":"update",
                    "count": len(codes)
                }
            }, status_code=200
        )