import pandas as pd

def calculate_and_save_frequencies(input_file, output_file):
    # 读取数据集
    df = pd.read_csv(input_file)

    # 初始化一个字典来存储每个属性的频率统计
    frequency_dict = {}

    # 遍历每个属性列
    for column in df.columns:
        # 统计每个值的频率
        frequency_dict[column] = df[column].value_counts().to_dict()

    # 创建一个 DataFrame 来存储频率统计结果
    frequency_df = pd.DataFrame(columns=['Attribute', 'Value', 'Count'])

    # 填充 DataFrame
    rows = []
    for column, freq in frequency_dict.items():
        for value, count in freq.items():
            rows.append({'Attribute': column, 'Value': value, 'Count': count})

    frequency_df = pd.concat([frequency_df, pd.DataFrame(rows)], ignore_index=True)

    # 将频率统计结果保存到 CSV 文件
    frequency_df.to_csv(output_file, index=False)

    print(f"Frequency statistics have been saved to '{output_file}'")

# 处理第一个文件
calculate_and_save_frequencies(
    'c:\\Users\\phdwf\\Documents\\risks--mdp\\datasets\\db_Adult.csv',
    'c:\\Users\\phdwf\\Documents\\risks--mdp\\datasets\\attribute_frequencies_adult.csv'
)

# 处理第二个文件
calculate_and_save_frequencies(
    'c:\\Users\\phdwf\\Documents\\risks--mdp\\datasets\\db_ACSEmployement.csv',
    'c:\\Users\\phdwf\\Documents\\risks--mdp\\datasets\\attribute_frequencies_acsemployement.csv'
)