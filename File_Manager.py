
class FileManager:

    def __init__(self, processos, processo):
        self.processos = processos
        self.p_number = processo




    def all_andamentos(self):
        """get all andamentos in processos and writes a file"""
        with open("todos_andamentos.txt", mode="wt", encoding= "utf-8") as file:
            num = 0
            print(num)
            for processo in self.p_number:

                file.write(f"{processo}:")
                file.write('\n')
                file.write('\n')

                for andamento in self.processos[num]:
                    file.write(andamento)
                    file.write('\n')

                file.write('\n')
                num += 1



    def write_info(self):
        # esta escrevendo o numero do processo errado!!!
        with open('andamentos.txt', mode='wt', encoding='utf-8') as myfile:
            num = 0
            print(num)
            for processo in self.p_number:

                myfile.write(f"{processo}:")
                myfile.write('\n')
                myfile.write('\n')

                for andamento in self.processos[num]:
                    myfile.write(andamento)
                    myfile.write('\n')

                myfile.write('\n')
                num += 1

    def read_file(self):
        with open('andamentos.txt') as f:
            lines = f.read()
            return lines
