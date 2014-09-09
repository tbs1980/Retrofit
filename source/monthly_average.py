# a program to  prin the mothly averages

import numpy as np
from xlrd import open_workbook
import datetime
import sys

date_start_epoch=datetime.datetime(1899,12,30)


def compute_averages(file_name,cdate,c1,c2,c3):

	# variables
	#####################################
	#file_name="TSB001.xlsx" 
	sheet_index=0
	column_date_index=cdate
	column_temp_1_index=c1
	column_temp_2_index=c2
	column_temp_3_index=c3
	avg_file_name=file_name+".averages.txt"
	#####################################

	print ""
	print "file name :",file_name
	print "date column :",column_date_index
	print "temperature column 1 :",column_temp_1_index
	print "temperature column 2 :",column_temp_2_index
	print "temperature column 3 :",column_temp_2_index
	print "output file :",avg_file_name
	print ""

	# open the workbook
	print "opening the file ",file_name
	print ""
	book=open_workbook(file_name)
	print "Done. Now computing the averages..."
	print ""



	# open the sheet
	sht=book.sheet_by_index(sheet_index)

	# open the column
	c_date=sht.col_values(column_date_index)
	c_t_1=sht.col_values(column_temp_1_index)
	c_t_2=sht.col_values(column_temp_2_index)
	c_t_3=sht.col_values(column_temp_3_index)

	month_check=0

	month_list=[]
	mean_t_list_1=[]
	mean_t_list_2=[]
	mean_t_list_3=[]

	tot_t_1=[]
	tot_t_2=[]
	tot_t_3=[]

	for i in range(len(c_date)):
		try:
			current_date = date_start_epoch + datetime.timedelta(days=int(c_date[i]))

			# am I a new month this case will be satisfied in the first iteration
			if current_date.month !=  month_check :

				# if not the first time I should append the values
				if month_check != 0 :
					month_list.append(month_check)
					mean_t_list_1.append(np.mean(tot_t_1))
					mean_t_list_2.append(np.mean(tot_t_2))
					mean_t_list_3.append(np.mean(tot_t_3))
					tot_t_1=[]
					tot_t_2=[]
					tot_t_3=[]

				if c_t_1[i] != 0 :
					tot_t_1.append( float(c_t_1[i]) )

				if c_t_2[i] != 0 :
					tot_t_2.append( float(c_t_2[i]) )

				if c_t_3[i] != 0 :
					tot_t_3.append( float(c_t_3[i]) )

				month_check = current_date.month

			else:
				if c_t_1[i] != 0 :
					tot_t_1.append( float(c_t_1[i]) )

				if c_t_2[i] != 0 :
					tot_t_2.append( float(c_t_2[i]) )

				if c_t_3[i] != 0 :
					tot_t_3.append( float(c_t_3[i]) )

		except(ValueError):
			print "Skipping the value ",i,c_date[i]

	# append the mean of the last month
	month_list.append(month_check)
	mean_t_list_1.append(np.mean(tot_t_1))
	mean_t_list_2.append(np.mean(tot_t_2))
	mean_t_list_3.append(np.mean(tot_t_3))

	print ""
	print "month","temp-1","temp-2","temp-3"
	for i in range(len(month_list)):
		print month_list[i],mean_t_list_1[i],mean_t_list_2[i],mean_t_list_3[i]

	
	np.savetxt(avg_file_name,np.asarray([month_list,mean_t_list_1,mean_t_list_2,mean_t_list_3]).T,fmt='%5.3f',delimiter=",")




if __name__ == '__main__':
	if len(sys.argv) == 6:
		#dsfds
		file_name=str(sys.argv[1])
		cdate=int(sys.argv[2])
		c1=int(sys.argv[3])
		c2=int(sys.argv[4])
		c3=int(sys.argv[5])

		if c1<0 or c2<0 or c3<0 :
			print "column numbers should be >= 0! try again..."
		else:
			compute_averages(file_name,cdate,c1,c2,c3)
	else:
		print "usage: python ",sys.argv[0], "<file_name>", "<date>" , "<temp-1>","<temp-2>","<temp-3>"
		print "example: python",sys.argv[0], "TSB001.xlsx 0 1 7 11"
