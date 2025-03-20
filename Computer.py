class Component:

    def __init__(self, motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port):
        self.motherboard_model = motherboard_model # модель материнской платы
        self.power_unit_model = power_unit_model # модель блока питания
        self.power_unit_port = power_unit_port # порт блока питания
        self.motherboard_soccet = motherboard_soccet # разъем материнской платы
        self.motherboard_voltage_port =  motherboard_voltage_port # порт напряжения материнской платы

    def get_info(self):
        print("Ваш компьютер имеет:"
               f"\n Модель материнской платы: {self.motherboard_model}"
               f"\n Модель блока питания: {self.power_unit_model}"
               f"\n Порт блока питания: {self.power_unit_port}"
               f"\n Разъем материнской платы: {self.motherboard_soccet}"
               f"\n Порт напряжения материнской платы: {self.motherboard_voltage_port}")
        
    def check_compatibility(self):
        if self.power_unit_port == self.motherboard_voltage_port:
            print(f"Проверка совместимости пройдена успешно, порты совместимы")
        else:
            print(f"Проверка совместимости провалена, порты не совместимы")

    def __del__(self):
        pass

class Processor(Component):
    
    def __init__(self, motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port, core_count, power_consumption, processor_model, soccet):
        super().__init__(motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port)
        self.core_count = core_count # количество ядер
        self.power_consumption = power_consumption # потребление энергии
        self.processor_model = processor_model # модель процессора
        self.soccet = soccet # сокет

    def get_info(self):
        super().get_info()
        print(f"Мой процессор имеет:"
              f"\n Количество ядер: {self.core_count}"
              f"\n Потребление энергии: {self.power_consumption}"
              f"\n Модель процессора: {self.processor_model}"
              f"\n Сокет: {self.soccet}")
        
    def check_system_compfbility(self):
        super().check_compatibility()
        if self.motherboard_soccet == self.soccet:
            print (f"Проверка совместимости пройдена успешно, сокеты совместимы")
        else:
            print (f"Проверка совместимости провалена, сокеты не совместимы")


computer1 = Processor(1, 2, 3, 4, 3, 6, 7, 8, 5)
computer1.check_system_compfbility()