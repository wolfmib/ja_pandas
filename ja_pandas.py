import pandas as pd




class ja_pandas:
    def __init__(self):
        self.name = "ja_pandas"
        self.description = "C'est utili pour moi-meme development purpose"
    
    def set_df(self,input_df):
        self.df = input_df.copy()
    
    def rename_col(self,input_df,norm_de_col,changed_name):
        pass




if __name__ == "__main__":

    print("Test the agent")
    # Changer le norm ###########################
    name_data_list = ["Johnny","Jean","Jason","Douge"]
    age_data_list = [32,25,27,45]
    # Creer la DataFrame
    test_df = pd.DataFrame({'norm_de_familiy':name_data_list,'age':age_data_list})
    print(test_df)
    
    # Change le norm de col
    test_df.rename(columns={'age': 'col_age_changed'},inplace=True)
    print(test_df)


    # test avec agent
    print("---------------------------------------------------------")

    #######################################################################






