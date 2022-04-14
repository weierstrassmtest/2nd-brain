def Reorder_Columns(input_frame, ordered_col_list, action_code, ref_col):
  # ACTION CODES
  # 0 = Move to beginning of DF
  # 1 = Move to end of DF
  reordered_frame = dataframe.copy(deep=True)
  all_columns = reordered_frame.columns
  other_columns = []
  for item in all_columns:
    if item not in ordered_col_list:
      other_columns.append(item)
  # Create List of all columns in original dataframe
  for column in reordered_frame.columns:
    all_columns = all_columns.append(column)
  
  return reordered_frame

# Re-order Columns
# cols = df_ss2.columns.tolist()
# cols = cols[-1:] + cols[:-1]
# df_ss2 = df_ss2[cols]
