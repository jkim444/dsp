import re
import csv
import pprint as pp
from collections import defaultdict

facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

def readCsv_dict(filename):
	file = open(filename, 'r')

	profile = {}

	for line in file.readlines():
		regex_lastTemp = re.search(r'[A-Z][a-z]*\,', line)
		regex_degree = re.findall(r'PhD|Ph\.D\.|Ph\.D|MA|MD|Sc\.D\.|ScD|MD|MPH|BSEd|B\.S\.Ed\.|MS|M\.S\.|JD|0', line)
		regex_degree = ' ' + ' '.join(regex_degree)
		if regex_degree == ' 0':
			regex_degree = regex_degree.strip()
		regex_title = re.search(r'[^,]*Professor[^,]*', line)
		regex_email = re.search(r'[^,]*[@].*\.edu', line)

		if regex_lastTemp:
			regex_lastName = re.sub(',', '', regex_lastTemp.group())
			if regex_lastName == "Bilker":
				regex_degree = regex_degree.strip()
			if regex_lastName in profile:
				profile[regex_lastName].append([regex_degree, regex_title.group(), regex_email.group()])
			else:
				profile[regex_lastName] = [[regex_degree, regex_title.group(), regex_email.group()]]

	return profile

def readCsv_tuple(filename):
	file = open(filename, 'r')

	profile = {}

	for line in file.readlines():
		regex_nameTemp = re.search(r'^[A-Z][\(\)\-\w\.\s]*\,', line)
		regex_degree = re.findall(r'PhD|Ph\.D\.|Ph\.D|MA|MD|Sc\.D\.|ScD|MD|MPH|BSEd|B\.S\.Ed\.|MS|M\.S\.|JD|0', line)
		regex_degree = ' ' + ' '.join(regex_degree)
		if regex_degree == ' 0':
			regex_degree = regex_degree.strip()
		regex_title = re.search(r'[^,]*Professor[^,]*', line)
		regex_email = re.search(r'[^,]*[@].*\.edu', line)

		if regex_nameTemp:
			regex_name = re.sub(',', '', regex_nameTemp.group())
			if regex_name == "Warren B. Bilker":
				regex_degree = regex_degree.strip()
			regex_nameTuple = tuple(regex_name.split(' '))
			profile[regex_nameTuple] = [regex_degree, regex_title.group(), regex_email.group()]
	
	return profile

def main():
	profiles = readCsv_dict('faculty.csv')

	answer = {'Li': [[' Ph.D.', 'Assistant Professor of Biostatistics',
						'liy3@email.chop.edu'],
					[' Ph.D.',
						'Associate Professor of Biostatistics',
						'mingyao@mail.med.upenn.edu'],
					[' Ph.D', 'Professor of Biostatistics',
						'hongzhe@upenn.edu']],
				'Localio': [[' JD MA MPH MS PhD',
								'Associate Professor of Biostatistics',
								'rlocalio@upenn.edu']]}
	
	answer2 = {('Benjamin', 'C.', 'French'): [' PhD', 
												'Associate Professor of Biostatistics',
												'bcfrench@mail.med.upenn.edu'],
				('Dawei', 'Xie'): [' PhD', 'Assistant Professor of Biostatistics',
									'dxie@upenn.edu'],
				('Russell', 'Takeshi', 'Shinohara'): ['0',
														'Assistant Professor of Biostatistics',
														'rshi@mail.med.upenn.edu'],
				('Warren', 'B.', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics',
												'warren@upenn.edu']
				}

	n = 0
	#pp.pprint(profiles)
	for key, vals in profiles.items():
		assert all('{key},{val}'.format(key=key, val=','.join(val)) in facultycsv for val in vals)
		n += len(vals)
	assert n == facultycsv.count('\n')
	print(1)

if __name__ == "__main__":
	main()