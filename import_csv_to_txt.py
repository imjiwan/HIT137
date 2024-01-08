import pandas as pd
import re

csv_files = [
    'C:/Users/Acer/Desktop/Master/Software Now (HIT137)/Group11_assignment 2/CSV1.csv',
    'C:/Users/Acer/Desktop/Master/Software Now (HIT137)/Group11_assignment 2/CSV2.csv',
    'C:/Users/Acer/Desktop/Master/Software Now (HIT137)/Group11_assignment 2/CSV3.csv',
    'C:/Users/Acer/Desktop/Master/Software Now (HIT137)/Group11_assignment 2/CSV4.csv'
]

all_content = []
for file in csv_files:
    try:
        df = pd.read_csv(file)
        content = df.to_string(index=False, header=False)
        content = re.sub(r'\d+', '', content)
        content = '\n'.join(line.strip() for line in content.splitlines() if line.strip())
        all_content.append(content)
    except pd.errors.EmptyDataError:
        print(f"Warning: Empty file found - {file}")

if all_content:
    combined_content = "\n".join(all_content)
    output_file = 'D:/Individual/text1.txt'
    with open(output_file, 'w') as f:
        f.write(combined_content)
    print(f'Combined content saved to {output_file}')
else:
    print('No valid data found in the CSV files.')
