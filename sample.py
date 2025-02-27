import hopsworks
import pandas as pd

def create_feature_group(name:str,primarykey:str):
    api_key = "wfTwb1hSTRESvdV1.FP4GjRqsGb2mGEcKUq5zZTfSPPAuicaUL8QZsWvr7ZpjhqA86CPa4H38MvhS439H"
    project_name = "shankarg"
    project = hopsworks.login(api_key_value=api_key,project=project_name)
    _fs=project.get_feature_store()
    fg = _fs.get_or_create_feature_group(
        name=name, 
        version=1, 
        description="Details of the Truck", 
        event_time = "event_time",
        primary_key=[primarykey], 
        online_enabled=False)
    return fg
    
trucks_df = pd.read_csv("/Users/shankar/Downloads/Data/Training_data/trucks_table.csv")
trucks_df["event_time"] = pd.to_datetime("2023-08-23")
trucks_df=trucks_df.sort_values(['event_time','truck_id'])
truck_fg = create_feature_group("trucks_df","truck_id")
truck_fg.insert(trucks_df)