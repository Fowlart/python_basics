import json as j

raw_json = """
[{"date": "2024-03-01", "Date_Pulled": "2024-03-20", "SKU_Nbr": "1000015757", "SKU_Class": "025-004-BUILDER'S HARDWARE", "SKU_Name": "COMMAND CLEAR CLIP W/WTHR STRIP 16PK", "Short_Month": "FP 202402", "SKU_Subclass": "025-004-026-PICTURE HANGING", "Week_Of": "Fiscal Week 5 of 2024", "suof_week_number": null, "SKU_Dept": "25-HARDWARE", "DC_Avg_Retail_Amount": null, "DC_Forecasted_Units": null, "In_Stock_Percentage": 0.9989995, "Out_of_Stock": 2, "number_of_stocking_stores": 1999, "consecutive_out_of_stock_days": 7}, {"date": "2024-03-01", "Date_Pulled": "2024-03-20", "SKU_Nbr": "1000015757", "SKU_Class": "025-004-BUILDER'S HARDWARE", "SKU_Name": "COMMAND CLEAR CLIP W/WTHR STRIP 16PK", "Short_Month": "FP 202402", "SKU_Subclass": "025-004-026-PICTURE HANGING", "Week_Of": "Fiscal Week 5 of 2024", "suof_week_number": null, "SKU_Dept": "25-HARDWARE", "DC_Avg_Retail_Amount": null, "DC_Forecasted_Units": null, "In_Stock_Percentage": null, "Out_of_Stock": null, "number_of_stocking_stores": null, "consecutive_out_of_stock_days": null}]
"""

decoder = j.JSONDecoder()
print(type(decoder))
decoded_json = decoder.decode(s=raw_json)
json_str = j.dumps(decoded_json, indent=4)
print(json_str)
