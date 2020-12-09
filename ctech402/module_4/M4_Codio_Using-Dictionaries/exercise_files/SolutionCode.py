weekly_planner = { 'Monday': 'hair appointment' , 'Tuesday': 'pick up groceries', 'Wednesday': 'baseball practice', 'Thursday': 'wash car', 'Saturday': 'dinner with friends'}


moved_appointments = []
if 'Monday' in weekly_planner:
	moved_appointments.append(weekly_planner['Monday'])
	del weekly_planner['Monday']

if 'Friday' in weekly_planner:
	moved_appointments.append(weekly_planner['Friday'])
	del weekly_planner['Friday']
	

weekly_planner['Tuesday'] += ',' + ' ,'.join(moved_appointments)
  
  
print(weekly_planner)


#want monday and friday off, move to another day of the week
