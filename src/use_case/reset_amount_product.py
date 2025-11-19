from src.main.http_types.http_response.http_response import HttpResponse
from src.model.database.mongodb.repositories.interface.product_repository_interface import IProductRepository

class ResetAmountProduct:

    def __init__(self, repository: IProductRepository):
        
        self.__repository = repository
    

    def handle(self) -> HttpResponse:
    
        #capturar todos os produtos
        products = self.__get_all_products_from_db()

        #get code and item list
        code_list, item_list = self.__get_code_and_items_length(products)

        #Atualizar as quantidades para 0
        self.__update_amount(code_list, item_list)

        formatted_response = self.__format_response(code_list)

        return formatted_response        

    
    def __get_all_products_from_db(self) -> list:

        products = self.__repository.get_all_products()

        return products
    
    def __get_code_and_items_length(self, products: list) -> tuple:

        code_list = []
        item_list = []

        for product in products:

            del product["_id"]
        
            code = list(product.keys())[0]

            code_list.append(code)

            item_list.append(len(product[code]))        

        return (code_list, item_list)
    
    
    def __update_amount(self, codes: list, items: list) -> None:

        for i in range(len(codes)):
            for j in range(items[i]):
                self.__repository.update_product_by_code_to_zero(codes[i], str(j))
            
    def __format_response(self, codes: list) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation":"update",
                    "count": len(codes)
                }
            },status_code=200
        )