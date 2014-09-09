# a program to  prin the mothly averages

import numpy as np
from xlrd import open_workbook
import datetime
import sys

date_start_epoch=datetime.datetime(1899,12,30) #starting epoch of the date in excel

def get_threasholds(month,room):
  winter = [10,11,12,1,2,3,4]
  summer = [5,6,7,8,9]
  thr_max = 22.
  thr_min = 26.

  if month in winter:
    if room == "bedroom":
      thr_max = 19.
      thr_min = 17.
    elif room == "livingroom":
      thr_max = 23.
      thr_min = 22.
    else:
      RuntimeError("Unknown room")
  elif month in summer:
    if room == "bedroom":
      thr_max = 23.
      thr_min = -100.
    elif room == "livingroom":
      thr_max = 25.
      thr_min = -100.
    else:
      RuntimeError("Unknown room")
  else:
    RuntimeError("Unknown month")

  return thr_max,thr_min


def compute_averages(file_name,cdate,c1,room):
  """
  Compute the monthly average, min, max of columns c1 given the date column
  cdate.

  @param file_name name of the input file
  @param cdata column corresponding to the date
  @param c1 column number corresponding to the 1st data
  """


  # variables
  #####################################
  #file_name="TSB001.xlsx"
  sheet_index=0
  column_date_index=cdate
  column_temp_1_index=c1
  avg_file_name = file_name+".stats_"+str(c1)+"_"+room+".txt"
  #####################################

  print ""
  print "file name :",file_name
  print "date column :",column_date_index
  print "temperature column :",column_temp_1_index
  print "room :",room
  print "output file :",avg_file_name
  print ""

  #return

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
  c_t=sht.col_values(column_temp_1_index)

  month_check=0

  month_list=[]
  mean_t_list=[]
  min_t_list = []
  max_t_list = []
  thr_min_list = []
  thr_max_list = []
  greater_than_max = []
  less_than_min = []

  tot_t=[]

  for i in range(len(c_date)):
    try:
      #find the current month
      current_date = date_start_epoch + datetime.timedelta(days=int(c_date[i]))

      # am I a new month this case will be satisfied in the first iteration
      if current_date.month !=  month_check :
        # if not the first time I should append the values
        if month_check != 0 :
          #print "month ",month_check
          month_list.append(month_check)
          if len(tot_t) >0 :
            mean_t_list.append(np.mean(tot_t))
            min_t_list.append(np.min(tot_t))
            max_t_list.append(np.max(tot_t))
            thr_max,thr_min=get_threasholds(month_check,room)
            tot_t_npy  = np.asarray(tot_t)
            thr_min_list.append(thr_min)
            thr_max_list.append(thr_max)
            greater_than_max.append(100.*len(np.where(tot_t_npy>thr_max)[0])/float(len(tot_t)))
            less_than_min.append(100*len(np.where(tot_t_npy<thr_min)[0])/float(len(tot_t)))
          else :
            mean_t_list.append(-1e90)
            min_t_list.append(-1e90)
            max_t_list.append(-1e90)
            thr_max,thr_min=get_threasholds(month_check,room)
            thr_max_list.append(thr_max)
            thr_min_list.append(thr_min)
            greater_than_max.append(-1e90)
            less_than_min.append(-1e90)

          tot_t=[]

        #if value is not FALSE add it to the list
        if c_t[i] != 0 :
          tot_t.append( float(c_t[i]) )

        month_check = current_date.month
      else: # if i am not a new month, keep appending the list
        if c_t[i] != 0 :
          tot_t.append( float(c_t[i]) )


    except(ValueError):
      print "Skipping the value ",i,c_date[i]
      #pass

  # append the mean of the last month
  month_list.append(month_check)
  if len(tot_t) >0 :
    mean_t_list.append(np.mean(tot_t))
    min_t_list.append(np.min(tot_t))
    max_t_list.append(np.max(tot_t))
    thr_max,thr_min=get_threasholds(month_check,room)
    tot_t_npy  = np.asarray(tot_t)
    thr_min_list.append(thr_min)
    thr_max_list.append(thr_max)
    greater_than_max.append(100.*len(np.where(tot_t_npy>thr_max)[0])/float(len(tot_t)))
    less_than_min.append(100*len(np.where(tot_t_npy<thr_min)[0])/float(len(tot_t)))
  else :
    mean_t_list.append(-1e90)
    min_t_list.append(-1e90)
    max_t_list.append(-1e90)
    thr_max,thr_min=get_threasholds(month_check,room)
    thr_max_list.append(thr_max)
    thr_min_list.append(thr_min)
    greater_than_max.append(-1e90)
    less_than_min.append(-1e90)

  # print the averages
  print ""
  print "month","mean","min","max","thr-min","thr-max","less-than-min%","greater-than-max%"
  for i in range(len(month_list)):
    print month_list[i],mean_t_list[i],min_t_list[i],max_t_list[i],thr_min_list[i],thr_max_list[i],less_than_min[i],greater_than_max[i]

  # write the averaes to a file
  np.savetxt(avg_file_name,np.asarray([month_list,mean_t_list,min_t_list,max_t_list,thr_min_list,thr_max_list,less_than_min,greater_than_max]).T,fmt='%5.3f',delimiter=",")


if __name__ == '__main__':
  if len(sys.argv) == 5:
    file_name=str(sys.argv[1])
    cdate=int(sys.argv[2])
    c1=int(sys.argv[3])
    room  = str(sys.argv[4])

    rooms = ["bedroom","livingroom"]

    if c1>0  and (room in rooms):
      #print "computing"
      compute_averages(file_name,cdate,c1,room)
    else:
      print "input problematic"
      print "note that"
      print "column of temperature should be > 0!"
      print "room should be in : ",rooms
  else:
    print "usage: python ",sys.argv[0], "<file_name>", "<date>" , "<temp>" ,"<bedroom/livingroom>"
    print "example: python",sys.argv[0], "TSB001.xlsx 0 1 bedroom"
