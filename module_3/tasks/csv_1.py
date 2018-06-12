import csv
import collections as col

crimes_csv = '/home/e-golov/Downloads/Crimes.csv'

if __name__ == '__main__':
    lst = list()
    with open('%s' % crimes_csv, 'r') as f:
        dr = csv.DictReader(f)
        for row in dr:
            if '2015' in row['Date']:
                lst.append(row['Primary Type'])
        print(col.Counter(lst).most_common(1))



