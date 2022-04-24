# Can be spark df OR pandas df

def Reorder_Columns(input_spark_frame, ordered_col_list):
    all_columns = input_spark_frame.columns
    other_columns = []
    for item in all_columns:
        if item not in ordered_col_list:
          other_columns.append(item)
        else:
            pass
    ordered_col_list.extend(other_columns)
    reordered_frame = input_spark_frame.select(ordered_col_list)
    return reordered_frame
