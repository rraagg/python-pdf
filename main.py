from pypdf import PdfReader
import os.path
import argparse

month_array = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

year_array = ["2023", "2022", "2021", "2020", "2019", "2018"]

def build_file_names(months, years):
    file_names = []
    for month in months:
        for year in years:
            file_names.append(f"{month}-{year}.pdf")
    return file_names

def check_for_word(word, page_text):
    lines = [line.rstrip() for line in page_text.split("\n")]
    for line in lines:
        if word in line:
            print(line)

def main():
    parser = argparse.ArgumentParser(description='Search for word')
    parser.add_argument('--word', default="FORET",
                    help='word to search for')

    args = parser.parse_args()
    pdfs = build_file_names(month_array, year_array)

    for pdf in pdfs:
        try:
            file = f"./pdfs/{pdf}"
            if os.path.isfile(file):
                reader = PdfReader(file)
                # number_of_pages = len(reader.pages)
                for page in reader.pages:
                    text = page.extract_text()
                    check_for_word(args.word, text)
            else:
                raise Exception(f"file not found: {file}")
        except Exception as e:
            print(e)
    

if __name__ == '__main__':
    main()