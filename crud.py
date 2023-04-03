import json

class GetMixin:
    def get_data(self):
        with open('data.json') as file:
            return json.load(file)
    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id += 1

        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id
    

class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        try:
            cars = {
                'id':super().get_id(),
                'marka':input('Введите марку машины: '),
                'model':input('Введите модель: '),
                'year':int(input('Введите год: ')),
                'volume':round(float(input('Введите объем двигателя: ')),1),
                'color':str(input('Введите цвет: ')),
                'probeg':int(input('Введите пробег: ')),
                'price':round(float(input('Введите цену: ')),2),
                'kuzov': str(input('Варианты кузова sedan, universal, kupe, hatchback, miniven, vnedorozhnik, pikap: ')),
                }
        except ValueError:
            print('Введите корректные данные!')
            self.create()
        else:
            data.append(cars)
            with open('data.json','w') as my_file:
                json.dump(data, my_file)
                print('Успешно создан!')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список машин')
        data = super().get_data()
        print(data)

class RetrieveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.retrieve()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Такого товара нет')
            else:
                print(one_product[0])

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Такого товара нет')

            product = data.index(one_product[0])

            choice = int(input('Что вы хотите изменить? 1-marka, 2-model, 3-year, 4-volume, 5-color, 6-probeg, 7-price: '))
            
            if choice == 1:
                try:
                    data[product]['marka'] = input('Введите новую марку: ')
                    print('Изменено!')
                except ValueError:
                    print('Марка неопознана')

            elif choice == 2:
                try:
                    data[product]['model'] = input('Введите новую модель: ')
                    print('Изменено!')
                except ValueError:
                    print('Модель неопознана')

            elif choice == 3:
                try:
                    data[product]['year'] = int(input('Введите год: '))
                    print('Изменено!')
                except ValueError:
                    print('Год неопознан')

            elif choice == 4:
                try:
                    data[product]['volume'] = round(float(input('Введите новый объем: ')),1)
                    print('Изменено!')
                except ValueError:
                    print('Объем неопознан')

            elif choice == 5:
                try:
                    data[product]['color'] = input('Введите цвет: ')
                    print('Изменено!')
                except ValueError:
                    print('Цвет неопознан')

            elif choice == 6:
                try:
                    data[product]['probeg'] = int(input('Введите пробег: '))
                    print('Изменено!')
                except ValueError:
                    print('Пробег неопознан')

            elif choice == 7:
                try:
                    data[product]['price'] = round(float(input('Введите новую цену: ')),2)
                    print('Изменено!')
                except ValueError:
                    print('Цена неопознана')

            else:
                print('Такого поля нет')
                self.update()
            with open('data.json', 'w') as file:
                json.dump(data, file)
            
class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Ввели некорректные данные')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product:
            print('Такого товара нет')
        product = data.index(one_product[0])
        data.pop(product)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        print('Удалено!')

class Cars(CreateMixin,ListingMixin,RetrieveMixin,UpdateMixin,DeleteMixin):
    def __init__(self,marka='',model='',year=0,kuzov='',volume=0,color='',probeg=0,price=0):
        self.marka = marka
        self.model = model
        self.year = year
        self.kuzov = kuzov
        self.volume = volume
        self.color = color
        self.probeg = probeg
        self.price = price

product = Cars()
# product.create()
# product.update()
# product.listing()
# product.retrieve()
# product.delete()
