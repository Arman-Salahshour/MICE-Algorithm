from sklearn.ensemble import RandomForestRegressor

def mice(data_frame,miss_cols,list,step):
    #Save DataFrame at every step in log
    log=[]
    #A dictionary for saving missing values
    missing_values={key:data_frame.loc[data_frame[f'{key}']==-1] for key in miss_cols}
    print(missing_values)
    df=data_frame.copy(deep=True)
    log.append(data_frame.copy(deep=True))

    #Puting avg of each column that has missing values at the place of the missing values
    for col in miss_cols:
        avg=df[df[col]!=-1][col].mean()
        df[col]=df[col].apply(lambda x: avg if x==-1 else x)


    #In every step we predict missing values till wefind the best answer   
    for _ in range(step):

        for col in miss_cols:
            log.append(df.copy(deep=True))

            for i in missing_values[col].index:
                df[col].loc[i]=-1
            
                tempList=list[:]
                tempList.remove(col)
                
                x=df[df[col]!=-1].loc[:,tempList]
                y=df[df[col]!=-1].loc[:, col].apply(lambda item: int(item))
                x_test=df[df[col]==-1].loc[:,tempList]
            
                #It uses K Neighbors Regressor for predecting missing values
                # lr=KNeighborsRegressor(n_neighbors=20)

                #It uses Linear Regression
                # lr=LinearRegression()
                lr=RandomForestRegressor()
                
                lr.fit(x,y)
                prediction=lr.predict(x_test)
                print(f'{col} : {prediction}')
                df[col].loc[i]=prediction[0]

    return df




