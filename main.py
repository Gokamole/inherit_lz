from Computer import Component
from Computer import Processor

def main():
    motherboard_model = input(f"Введите модель вашей материнской платы ")
    power_unit_model = input(f"Введите модель вашего блока питания ")
    power_unit_port = input(f"Введите порт вашего блока питания ")
    motherboard_soccet = input(f"Введите сокет вашей материнской платы ")
    motherboard_voltage_port = input(f"Введите порт напряжения вашей материнской платы ")
    core_count = input(f"Введите количество ядер ")
    power_consumption = input(f"Введите потребление энергии ")
    processor_model = input(f"Введите модель вашего процессора ")
    soccet = input(f"Введите сокет вашего процессора ")

    computer1 = Component(motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port)
    computer1 = Processor(motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port, core_count, power_consumption, processor_model, soccet)

    computer1.check_system_compability()
    computer1.get_info()
    
if __name__ == "__main__":
    main()