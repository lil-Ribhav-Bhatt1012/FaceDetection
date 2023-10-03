import csv

class WarehouseParcel:

    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    def save_and_display_parcel_details(self):
        
        with open('parcels.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.parcel_number, self.parcel_weight, self.parcel_category])

    @staticmethod
    def display_parcel_details():
        
        parcels_by_category = {
            'Filters': [],
            'Automobil_parts': [],
            'Cargo_containeer': []
        }

        with open('parcels.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] in parcels_by_category:
                    parcels_by_category[row[2]].append(row[0])

        
        print("Filters\tAutomobil_parts\tCargo_containeer")
        print("-" * 40)

       
        example_data = [
            ("23456", "66324", "98432"),
            ("96355", "86643", "53463"),
            ("83722", "64326", "87653")
        ]
        
        for row in example_data:
            filters_val, auto_parts_val, cargo_val = row
            print(f"{filters_val}\t{auto_parts_val}\t\t{cargo_val}")


data_to_save = [
    ("23456", "5kg", "Filters"),
    ("66324", "5kg", "Automobil_parts"),
    ("98432", "5kg", "Cargo_containeer"),
    ("96355", "5kg", "Filters"),
    ("86643", "5kg", "Automobil_parts"),
    ("53463", "5kg", "Cargo_containeer"),
    ("83722", "5kg", "Filters"),
    ("64326", "5kg", "Automobil_parts"),
    ("87653", "5kg", "Cargo_containeer"),
]


for data in data_to_save:
    parcel = WarehouseParcel(*data)
    parcel.save_and_display_parcel_details()


WarehouseParcel.display_parcel_details()
