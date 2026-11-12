#Step 2 : Data Preprocessing and Cleaning
def data_preprocessing(df):
  '''
  Step 1 : Feature engineering and Selection

  step 2 : Split the dataset  into independent and dependent columns i.e X and y

  step 3 : Use trian and test split i.e. Split the dataset into Seen and Unseen
  (Seen Data : train data and Unseen data : test data)

  step 4 : Use Scaling Technique /Normalization Technique
  (StndardScaler / MinMaxScaler/ RobustScaler)

  step 5 : Return Seen and Unseen data
  '''
  #Step 1 :Feture Engineering : Create a new feature based on existing feature
  df['Water_Binder_Ratio'] = df['Water  (component 4)(kg in a m^3 mixture)']/(df['Cement (component 1)(kg in a m^3 mixture)'] +
                                                                              df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)']
                                                                              +df['Fly Ash (component 3)(kg in a m^3 mixture)'])

  # Step 2 : Split the dataset into X and y
  target_col = ('Concrete compressive strength(MPa, megapascals) ')
  X = df.drop(columns= [target_col])  # Independent columns
  y = df[target_col]                  # Target Column

  #Step 3 : split the dataset into Seen and Unseen (Train and Test Data)
  from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
  X_train.shape, X_test.shape, y_train.shape, y_test.shape

  '''
  * Scaling for training data: fit_transform()
  * Scaling for test data: transform()
  '''

  sc = MinMaxScaler()
  X_train = sc.fit_transform(X_train)  # Seen Data
  X_test = sc.transform(X_test)        #Unseen Data

# Step 5 : return seen and unseen data
  return X_train, X_test, y_train, y_test
