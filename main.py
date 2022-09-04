import pandas as pd
class DataProcess:
    def __area(self, area_name):
        area_code = {
            'karapakam': 0,
            'adyar': 1,
            'chrompet': 2,
            'velachery': 3,
            'kk_nagar': 4,
            'anna_nagar': 5,
            't_nagar': 6}
        return area_code[area_name]

    def __mzzone(self, zone_name):

        zone_code = {
            'a': 0,
            'c': 1,
            'i': 2,
            'rh': 3,
            'rl': 4,
            'rm': 5}
        return zone_code[zone_name]

    def __sale_cond(self, sale_name):
        sale_code = {
            'abnormal': [0, 0, 0, 0],
            'adjland': [1, 0, 0, 0],
            'family': [0, 1, 0, 0],
            'normalsale': [0, 0, 1, 0],
            'partial': [0, 0, 0, 1]
        }
        return sale_code[sale_name]

    def __parking(self, park):
        park_code = {
            'yes': 1,
            'no': 0
        }
        return park_code[park]

    def __build_type(self, build):
        build_code = {
            "commercial": [0, 0],
            "house": [1, 0],
            "other": [0, 1]
        }
        return build_code[build]

    def __utility(self, util):
        util_code = {
            "allpub": [0, 0],
            "elo": [1, 0],
            "nosewr": [0, 1]
        }
        return util_code[util]

    def __street(self, street):
        street_code = {
            "gravel": [0, 0],
            "noaccess": [1, 0],
            "paved": [0, 1]}
        return street_code[street]

    def process_input(self, data):
        # call every fun
        # get processed output from every fun and store in pro_data
        # send the pro_data for model

        pro_data = list()
        for i in range(len(data)):
            if i == 0:
                # area
                variable = self.__area(data[i])
                pro_data.append(variable)
            elif i == 1:
                # int_sqft
                pro_data.append(data[i])
            elif i == 2:
                # n_bedroom
                pro_data.append(data[i])
            elif i == 3:
                # n_bathroom
                pro_data.append(data[i])
            elif i == 4:
                # n_room
                pro_data.append(data[i])
            elif i == 5:
                # mzzone
                variable = self.__mzzone(data[i])
                pro_data.append(variable)
            elif i == 6:
                # date_build
                _date_build = pd.DatetimeIndex([data[i]]).year
            elif i == 7:
                # date_sale
                date_sale = pd.DatetimeIndex([data[i]]).year
                variable = date_sale - _date_build
                for i in variable:
                    val = int(i)
                pro_data.append(val)
            elif i == 8:
                # sale_cond
                variable = self.__sale_cond(data[i])
                for i in variable:
                    pro_data.append(i)
            elif i == 9:
                # parking
                variable = self.__parking(data[i])
                pro_data.append(variable)
            elif i == 10:
                # build_type
                variable = self.__build_type(data[i])
                for i in variable:
                    pro_data.append(i)
            elif i == 11:
                # utility
                variable = self.__utility(data[i])
                for i in variable:
                    pro_data.append(i)
            elif i == 12:
                # street
                variable = self.__street(data[i])
                for i in variable:
                    pro_data.append(i)
        return pro_data
