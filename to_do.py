import os

print('Use "h" or help for more details')
while True:
	cmds = input("> ").lower()
	
	if cmds == "h" or cmds == "help":
		print('Use "a" to add a new to do')
		print('Use "e" to edit a to do ')
		print('Use "r" to remove your to do')
		print('Use "s" to see your to do')
		print('Use "q" to quit')
	
	elif cmds == "a":
		add = input("Your to do: ")
		
		with open("tasks.txt", "a") as var2:
				var2.write(f"\n{add}")
				print("Task added")
		
		
	elif cmds == "r":
	   with open("tasks.txt", "r") as f:
	   	tasks = f.readlines()
	   
	   size = os.path.getsize("tasks.txt")	
	   
	   if size > 0:
	   		while "\n" in tasks:
	   			tasks.remove("\n")
	   			
	   		print(tasks)
	   		try:
	   			index = int(input("Index to remove: ")) -1
	   			
	   			tasks.pop(index)
	   			
	   			with open("tasks.txt", "w") as f2:
	   				f2.write('\n'.join(tasks))
	   				print("Removed succefully")
	   		except:
	   			print("Some error occurred")
	   	
	   else:
	   	print("Add a to do first")
		
	
	
	elif cmds == "s":
		size = os.path.getsize("tasks.txt")
		
		if size > 0:
			with open("tasks.txt", "r") as see:
				print(see.read())
			
		else:
			print("Add a to do first")
	
	
	elif cmds == "e":
		with open("tasks.txt", "r") as edit:
			able = edit.readlines()
			
			size = os.path.getsize("tasks.txt")
			
			if size > 0:
				while "\n" in able:
					able.remove("\n")
					
				print(able)
				
				try:
					inp = int(input("Index to edit: "))-1
					words = input("The new task: ")
					able.pop(inp)
					
					able.insert(inp, words)
					
					with open("tasks.txt", "w") as final:
						final.write('\n'.join(able))
						print("Succefully edited")
				except:
					print("Some error occurred")
					
				
			
			
			else:
			      print("Add a to do first")
	
	
	elif cmds == "q":
		print("You exited")
		break
		
	else:
		print('Not sure what to type?. Use "h" or help')		
