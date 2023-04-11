from aia.preprocessing.utils import Preprocess_Text

df = Preprocess_Text("C:\\Users\\GRIZELLE\\GitHub Projects\\aia\\Dataset\\cereal.csv")
df.preprocess()
df.view()