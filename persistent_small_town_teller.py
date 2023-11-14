import pickle


class PersistenceUtils:

    def write_pickle(data, file_path):
        # Writes data to a file using pickle
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
            print(f"Data written to {file_path} using pickle")

    def load_pickle(file_path):
        # Loads data from file using pickle
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            print(f"Data loaded from {file_path} using pickle")
            return data


class Bank:

    def __init__(self):
        # Initialize a bank object with empty list for customers and accounts
        self.accounts = []
        self.customers = []

    def save_data(self, file_path):
        # Save bank data to file using pickle
        # create dictionary containing data to be saved
        # 'Customers': list of data from bank instance
        # 'Accounts': list of account data from bank instance
        data_to_save = {'customers': self.customers, 'accounts': self.accounts}
        PersistenceUtils.write_pickle(data_to_save, file_path)

    def load_data(self, file_path):
        # Loads bank data from file using pickle
        loaded_data = PersistenceUtils.load_pickle(file_path)
        # Update 'customers' or 'accounts' attributes of bank instance with loaded customer data
        # If 'customers' or 'accounts' key is not there in loaded data, fallback to the empty list
        self.customers = loaded_data.get('customers', [])
        self.accounts = loaded_data.get('accounts', [])
