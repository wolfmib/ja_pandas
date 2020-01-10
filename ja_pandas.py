import pandas as pd
import ja_language as ja_lan 




class ja_pandas:
    def __init__(self):
        self.name = "ja_pandas"
        self.description = "C'est utili pour moi-meme development purpose"
    
    def set_df(self,input_df):
        self.df = input_df.copy()
    
    def _obtenir_df(self):
        return self.df

    def rename_col(self,origin_col_norm,after_col_norm,option_df=_obtenir_df()):

        # __cnanged_dict Format:
            # {origin_name : after_name}
        __changed_dict = {origin_col_norm:after_col_norm}
        option_df.rename(columns=__changed_dict,inplace=True)
        return option_df.copy
        


if __name__ == "__main__":

    try:
        ja_lan_df = pd.read_pickle('ja_lan_env.pkl')
        apply_lan = ja_lan_df['ja_lan'][0]
        print("[INFO]: Your apply language is {%s}"%apply_lan)
    except:
        print("[INFO]: No ja_lan_env.pkl found !")
        print("Set language as default 'English' ")

    ja_lan = ja_lan.language_translator()
    ja_lan.set_language_code(apply_lan)


    print(ja_lan.print("Test the class:  ja_pandas"))
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
    ja_pd = ja_pandas()
    test_df = pd.DataFrame({'norm_de_familiy':name_data_list,'age':age_data_list})
    print(test_df)
    print("-----------\n\n")
    test_df = ja_pd.rename_col('age','after_age',test_df)
    print(test_df)
    print("-----------\n\n")


    #######################################################################






