import os
import tkinter as tk
from tkinter import ttk
import pandas as pd

class MembersTable:
	def __init__(self, master, s1, s2, s3):
		self.master = master
		self.master.title("Members Table")
		self.master.geometry("600x400")
		
		self.treeview = ttk.Treeview(master)
		self.treeview.pack(fill=tk.BOTH, expand=True)
		columns = ['골', '점수']
		self.treeview["columns"] = columns
		for column in columns:
			self.treeview.column(column, anchor=tk.CENTER, width=100)
			self.treeview.heading(column, text=column, anchor=tk.CENTER)
			
		df = pd.DataFrame([[s1.countGetter, s1.countGetter], [s2.countGetter, s2.countGetter*2],[s3.countGetter, s3.countGetter*3]])
		
		for i, row in df.iterrows():
			values = list(row.values)
			self.treeview.insert("", tk.END, text=i+1, values=values)
		self.treeview.insert("", tk.END, text="total", values=[sum(df.iloc[:,0]), sum(df.iloc[:,1])])

class Basketball:
	def __init__(self):
		self.__count = 0
		
	@property
	def countGetter(self):
		return self.__count
		
	@countGetter.setter
	def countSetter(self, count):
		self.__count = count
		
def main():
	score1 = Basketball()
	score2 = Basketball()
	score3 = Basketball()
	while 1:
		n = input('1점, 2점, 3점중 하나를 입력하세요. 0점을 입력하면 종료됩니다.\n')
		if not n.isdigit():
			os.system('cls')
			print('범위 밖을 넘었습니다.')
			continue
		n = int(n)
		if n < 0 or n > 3:
			os.system('cls')
			print('범위 밖을 넘었습니다.')
			continue
		if n == 1:
			score1.countSetter+=1
		elif n == 2:
			score2.countSetter+=1
		elif n == 3:
			score3.countSetter+=1
		elif n == 0:
			break
	root = tk.Tk()
	MembersTable(root, score1, score2, score3)
	root.mainloop()
	
main()