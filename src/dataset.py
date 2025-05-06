import pandas as pd

data = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Salary": [50000, 60000, 70000, 80000],
    "Email": ["john@example.com", "jane@example.com", "jim@example.com", "jill@example.com"],
    "Phone": ["1234567890", "0987654321", "1122334455", "6677889900"],
}

df = pd.DataFrame(data)

print(df)

df.head(2)

df.tail(2)

df.describe()

df.info()

df.replace("New York", "NY", inplace=True)

df.replace(["New York", "Los Angeles"], ["NY", "LA"], inplace=True)

df.replace({"New York": "NY", "Los Angeles": "LA"}, inplace=True)

