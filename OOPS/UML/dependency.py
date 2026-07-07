class Printer:
    def print_data(self, text):
        print(text)


class Report:
    def generate(self, printer):
        printer.print_data("Report Generated")

printer = Printer()
report = Report()

report.generate(printer)