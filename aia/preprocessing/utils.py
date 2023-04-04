# can use python packages, this is just to learn OOP (inheritance, encapsulation, polymorphism, abstraction)

import pandas as pd
import numpy as np
from abc import ABC, abstractclassmethod

class Preprocess_Data(ABC): # acc to different file types
    def __init__(self, data_path) -> None:
        """
        Load the DataFrame using pandas
        """ 
        try:
            self.data_frame = pd.read_csv(data_path)
        except (OSError, FileNotFoundError, TypeError):
            print("File path does not exist")
            exit(-1)

    def drop_columns(self):
        pass

    def drop_rows(self):
        pass

    def dummy_vars(self):
        pass

    def missing_data(self):
        pass

    def clean(self):
        pass

    # Class must do the following
    # 1. Load data in Pandas
    # 2. Drop columns that are not useful
    # 3. Drop rows with missing values
    # 4. Create dummy variables
    # 5. Take care of missing data
    # -- lower, remove spaces, remove numbers in text
    # 6. Convert the data frame to NumPy
    # 7. Divide the data set into training data and test data