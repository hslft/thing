from pathlib import Path
import csv
file_path = Path.cwd()/"csv_reports"/"Profit_Loss.csv"
summary = Path.cwd()/"summary_report.txt"
def profit_loss_function(): 
    increase = 0
    lack = 0
    PL = []
    with file_path.open(mode="r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for profits in reader:
            PL.append(profits)
            count = len(PL)
            while increase + 1 < count:
                prev_figure = PL[increase][4]
                figure = PL[increase + 1][4]
                PREV_FIGURE = float(prev_figure)
                FIGURE = float(figure)
                with summary.open(mode="a",encoding="UTF-8",newline="") as file:
                    if PREV_FIGURE - FIGURE <  0:
                        statement = f"\n[PROFIT DEFICIT] DAY: {PL[increase + 1][0]}, AMOUNT: SGD{(lack):.2f}"
                        file.write(statement)
                        file.close()
                        increase += 1
                        if lack == 0:
                            with summary.open(mode="a",encoding = "UTF-8",newline="") as file:
                                statement_2 = f"\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                                file.write(statement_2)
                                file.close()
    file.close()
print(profit_loss_function())
            

