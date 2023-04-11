# can use python packages, this is just to learn OOP (inheritance, encapsulation, polymorphism, abstraction)

import pandas as pd
import numpy as np
import os
from abc import ABC, abstractmethod

class Preprocess_Data(ABC): # acc to different file types
    def __init__(self, data_path: str) -> None:
        """
        Load the DataFrame using pandas
        """ 
        try:
            DIR = os.path.abspath(data_path)
            self.data_frame = pd.read_csv(DIR)
            #print(self.data_frame)
        except (OSError, FileNotFoundError, TypeError):
            print("File path does not exist")
            exit(-1)

    def view(self):
        print(self.data_frame)

    @abstractmethod
    def preprocess(self):
        pass

class Preprocess_Text(Preprocess_Data):
    def __init__(self, data_path: str, *args) -> None:
        super().__init__(data_path)

        self.action = 0

        if args:
            if len(args) > 1:
                self.action = args[0]
                self.value = args[1]
            else:
                self.action = args[0]

    def __drop_columns(self):
        try:
            self.data_frame.drop([self.value], axis=1)
            return self.data_frame
        except Exception as e:
            print(e)
            exit(-1)

    def __drop_empty_cells(self):
        self.data_frame = self.data_frame.dropna()
        return self.data_frame

    def __replace_values(self):
        try:
            if self.action == 3:
                self.data_frame.fillna(self.value)
            elif self.action == 4:
                self.data_frame.replace(to_replace = np.nan, value = self.value)
            return self.data_frame
        except Exception as e:
            print(e)
            exit(-1)

    def __clean(self):
        # Lowercase
        self.data_frame = self.data_frame.apply(lambda x: x.astype(str).str.lower())

        # Remove extra space
        for i in self.data_frame.columns:
            if self.data_frame[i].dtype == 'object':
                self.data_frame[i] = self.data_frame[i].map(str.strip)
            else:
                pass

        # Remove emojis
        self.data_frame.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))  

        return self.data_frame

    def preprocess(self):
        if self.action == 1:
            self.data_frame = self.__drop_columns()
        elif self.action == 2:
            self.data_frame = self.__drop_empty_cells()
        elif self.action == 3 or self.action == 4:
            self.data_frame = self.__replace_values()
        self.data_frame = self.__clean()
        #print(self.data_frame)

        return super().preprocess()

class Preprocess_Image(Preprocess_Data):
    def __init__(self, data_path) -> None:
        super().__init__(data_path)

    def clean(self):
        pass

    def preprocess(self):
        return super().preprocess()