def overheads_functions(forex):
    """
    - This function will find the highest overhead category and its value.
    - This function will return the value in SGD after it is converted using the real-time exchange rate from the API call.
    """
    from pathlib import Path
    import re, csv

    file_home = Path.cwd()/"project_group"
    file_path = file_home/"csv_reports"/"Overheads.csv"
    
    fp_summary = file_home/"summary_report.txt"
    highestvalue = 0.00
    Category = ""
    with file_path.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        #to skip the header.
        next(reader)
        for data in reader:
            if float(data[1]) > highestvalue:
                highestvalue = float(data[1])
                Category = data[0].upper()
                
                with fp_summary.open(mode = "w", encoding = "UTF-8", newline = "") as file:
                    Output = f"\n[HIGHEST OVERHEAD] {Category} : SGD{highestvalue:.2f}"
                    file.write(Output)
                    file.close()
    file.close()
