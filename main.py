from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing
from src.model_duild import model_build
# Define Orchestron Model : Enter Point
#Orchestrator Layer : Enter point
def main():  # Function Defination
  #step 1 : Data Ingestion
  df = data_ingestion()
  #step 2 : Data PreProseccing and Cleaning
  X_train, X_test, y_train, y_test = data_preprocessing(df)
  #step 3 : Model Building
  score = model_build(X_train, X_test, y_train, y_test)
  print(f'R2 score : {score}')

main()  # Function Calling