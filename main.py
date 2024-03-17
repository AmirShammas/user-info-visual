import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
users = df["User"].to_list()
user_code = input("Please enter the user's code: ")

if user_code in users:
    selected_data = df[df['User'] == user_code]
    grouped_data_month = selected_data.groupby('Month').agg(
        {'Count': 'sum', 'Total Price': 'sum'})
    grouped_data_product = selected_data.groupby(
        'Product').agg({'Count': 'sum'})

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

    ax1.bar(grouped_data_month.index, grouped_data_month['Count'], width=0.1)
    ax1.set_xlabel('Month')
    plt.xticks(range(1, 13))
    ax1.set_ylabel('Count')
    ax1.set_title('Count(sum)/Month for selected user')

    ax2.plot(grouped_data_month.index,
             grouped_data_month['Total Price'], marker='o', color='red')
    ax2.set_xlabel('Month')
    plt.xticks(range(1, 13))
    ax2.set_ylabel('Total Price')
    ax2.set_title('Total Price(sum)/Month for selected user')

    ax3.bar(grouped_data_product.index,
             grouped_data_product['Count'], color='Green', width=0.1)
    ax3.set_xlabel('Product')
    ax3.set_ylabel('Count')
    ax3.set_title('Count/Product for selected user')

    plt.tight_layout()

    plt.show()
else:
    print("The user's code is not correct !!")
