def Reorder_Column(dataframe, col_to_move, ref_col):
  reordered_frame = dataframe.copy(deep=True)
  all_columns = []
  # Create List of all columns in original dataframe
  for column in reordered_frame.columns:
    all_columns = all_columns.append(column)
  
  return reordered_frame
