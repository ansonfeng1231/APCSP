# partner with Ivan Li
# set up parent class for the computer
class Computer:
    def __init__(self, name, cpu, ram, hard_drive, gpu):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.hard_drive = hard_drive
        self.gpu = gpu

# set up child class for the computer specs
    def specs(self):
        return '{} has {}, {}, {}, {}.'.format(self.name, self.cpu, self.ram, self.hard_drive, self.gpu)


class Pc(Computer):
    def __init__(self, name, cpu, ram, hard_drive, gpu):
        Computer.__init__(self, name, cpu, ram, hard_drive, gpu)


# define all of the macs
mac1 = Pc('MacBook Air', 'Apple M1 chip with 8‑core CPU', '8GB unified memory', '256GB SSD storage',
          '7‑core GPU, and 16‑core Neural Engine')
mac2 = Pc('MacBook Air', 'Apple M1 chip with 8‑core CPU', '8GB unified memory', '512GB SSD storage',
          '8‑core GPU, and 16‑core Neural Engine')
mac3 = Pc('MacBook Pro 13"', 'Apple M1 chip', '8GB unified memory', '256GB SSD storage',
          '8-core GPU, and 16-core Neural Engine')
mac4 = Pc('MacBook Pro 13"', 'Apple M1 chip', '8GB unified memory', '512GB SSD storage',
          '8-core GPU, and 16-core Neural Engine')
mac5 = Pc('MacBook Pro 13"', '2.0GHz quad-core 10th-generation Intel Core i5 processor', '16GB memory',
          '512GB SSD storage', 'and Intel Iris Plus Graphics')
mac6 = Pc('MacBook Pro 13"', '2.0GHz quad-core 10th-generation Intel Core i5 processor', '16GB memory',
          '1TB SSD storage', 'and Intel Iris Plus Graphics')
mac7 = Pc('MacBook Pro 16"', '2.6GHz 6-core 9th-generation Intel Core i7 processor', '16GB of 2666MHz DDR4 memory',
          '512GB of SSD storage', 'and AMD Radeon Pro 5300M with 4GB of GDDR6 memory')
mac8 = Pc('MacBook Pro 16"', '2.3GHz 8-core 9th-generation Intel Core i9 processor', '16GB of 2666MHz DDR4 memory',
          '1TB of SSD storage', 'and AMD Radeon Pro 5500M with 4GB of GDDR6 memory')
mac9 = Pc('iMac 21.5"', '2.3GHz dual-core 7th-generation Intel Core i5 processor',
          '8GB 2133MHz memory, configurable to 16GB', '256GB SSD storage', 'and Intel Iris Plus Graphics 640')
mac10 = Pc('iMac 21.5"', '3.6GHz quad-core 8th-generation Intel Core i3 processor',
           '8GB 2400MHz DDR4 memory, configurable up to 32GB', '256GB SSD storage',
           'Radeon Pro 555X with 2GB of GDDR5 memory')
mac11 = Pc('iMac 21.5"', '3.0GHz 6-core 8th-generation Intel Core i5 processor',
           '8GB 2666MHz DDR4 memory, configurable up to 32GB', '256GB SSD storage',
           'Radeon Pro 560X with 4GB of GDDR5 memory')
mac12 = Pc('iMac 27"', '3.1GHz 6-core 10th-generation Intel Core i5 processor',
           '8GB 2666MHz DDR4 memory, configurable up to 128GB', '256GB SSD storage',
           'Radeon Pro 5300 with 4GB of GDDR6 memory')
mac13 = Pc('iMac 27"', '3.3GHz 6-core 10th-generation Intel Core i5 processor',
           '8GB 2666MHz DDR4 memory, configurable up to 128GB', '512GB SSD storage',
           'Radeon Pro 5300 with 4GB of GDDR6 memory')
mac14 = Pc('iMac 27"', '3.8GHz 8-core 10th-generation Intel Core i7 processor',
           '8GB 2666MHz DDR4 memory, configurable up to 128GB', '512GB SSD storage',
           'Radeon Pro 5500 XT with 8GB of GDDR6 memory')
mac15 = Pc('iMac Pro', '3.0GHz 10-core Intel Xeon W processor',
           '32GB 2666MHz ECC memory, configurable up to 256GB', '1TB SSD storage',
           'Radeon Pro Vega 56 with 8GB HBM2 memory')
mac16 = Pc('Mac Pro', '2.5GHz 28-core Intel Xeon W', '32GB, configurable up to 1.5 TB of DDR4 ECC memory', '8TB SSD',
           'One or two Radeon Pro Vega II Duo MPX Modules with 64GB of HBM2 memory each')
mac17 = Pc('Mac mini', 'Apple M1 chip with 8‑core CPU', '8GB unified memory',
           '256GB SSD storage', '7‑core GPU, and 16‑core Neural Engine')
mac18 = Pc('Mac mini', 'Apple M1 chip with 8‑core CPU', '8GB unified memory',
           '512GB SSD storage', '8‑core GPU, and 16‑core Neural Engine')

# print all of the specs
print(Pc.specs(mac1))
print(Pc.specs(mac2))
print(Pc.specs(mac3))
print(Pc.specs(mac4))
print(Pc.specs(mac5))
print(Pc.specs(mac6))
print(Pc.specs(mac7))
print(Pc.specs(mac8))
print(Pc.specs(mac9))
print(Pc.specs(mac10))
print(Pc.specs(mac11))
print(Pc.specs(mac12))
print(Pc.specs(mac13))
print(Pc.specs(mac14))
print(Pc.specs(mac15))
print(Pc.specs(mac16))
print(Pc.specs(mac17))
print(Pc.specs(mac18))
