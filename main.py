from src.data_ingestion import data_ingestion
# Define Orchestron Model : Enter Point
def main() :  #Function Defination
  # step 1 : Data Ingestion
  df = data_ingestion()
  df.head()


main() #Function Calling