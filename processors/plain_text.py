#!python3

#from win32com.client.dynamic import AttributeError

def split_strip(comma_separated_txt="", delimiter=","):
	#print(">>>>",command_line_arg.wmi_object_properties)
	return [x.strip() for x in comma_separated_txt.split(delimiter)]


def plain_text3(wmi_objects,command_line_arg,host):
	if type(wmi_objects) is not list:
		wmi_objects = [wmi_objects]
	properties = command_line_arg.wmi_object_properties
	if properties:
		properties = split_strip(command_line_arg.wmi_object_properties)
	else:
		#print(">>>",type(wmi_objects[0]))
		#if type(wmi_objects) is list: 			properties =  wmi_objects
		properties =  wmi_objects[0].properties.keys()
		command_line_arg.wmi_object_properties = ",".join(properties)
	

	result=[]	
	
	for obj in wmi_objects:
		tmp = []
		for p in properties:
			#print(">>>",p)
			tmp.append(getattr(obj, p))
		result.append(tmp)
#		except(AttributeError):
#				result.append([obj.Property, getattr(obj, obj.Property)])
	return result
