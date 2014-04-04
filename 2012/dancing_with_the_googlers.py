import os
import sys


fn = sys.argv[1]

#print (fn)

fd = open(fn, 'r')

lines = fd.readlines()

fd.close()

T = int(lines[0])

#T = 4

def getScores_2(ti, S, p):
	scores = []
	s_scores = []
	for score in ti:
		if score % 3 == 0:
			x = int(score / 3)
			if x >= 1:
				s_scores.append((x - 1, x, x + 1))
			else:
				s_scores.append((-1, -1, -1))
			scores.append((x, x, x))
			continue
		if (score + 1) % 3 == 0:
			if (score - 2) >= 0:
				x = int((score - 2) / 3)
				s_scores.append((x, x, x + 2))
			else:
				s_scores.append((-1, -1, -1))
			
			x = int((score + 1) / 3)
			if x >= 1:
				scores.append((x, x, x - 1))
			else:
				scores.append((-1, -1, -1))
			continue
		if (score - 1) % 3 == 0:
			x = int((score + 2) / 3)
			if x >= 2:
				s_scores.append((x, x, x - 2))
			else:
				s_scores.append((-1, -1, -1))
			if (score - 1) >= 0:
				x = int((score - 1) / 3)
				scores.append((x, x, x + 1))
			else:
				scores.append((-1, -1, -1))
				
	#print("1\t", scores, "\t", s_scores);
	
	f_scores = []
	
	cnt = []
	if S != 0:
		for i in range(0, len(scores)):
			if max(scores[i]) < p:
				if max(s_scores[i]) >= p:
					cnt.append(i)
					S -= 1
					if S == 0:
						break

	#print("2\t", cnt, "\t", S);
	
	for i in range(0, len(scores)):
		if i in cnt:
			f_scores.append(s_scores[i])
			#print("3\t", f_scores);
		else:
			if S != 0:
				if max(s_scores[i]) == -1 or max(s_scores[i]) < p:
					f_scores.append(scores[i])
					#print("4\t", f_scores);
				else:
					f_scores.append(s_scores[i])
					S -= 1
					#print("5\t", f_scores, "\t", S);
			else:
				if max(scores[i]) == -1:
					f_scores.append(s_scores[i])
					#print("6\t", f_scores);
				else:
					f_scores.append(scores[i])
					#print("7\t", f_scores);
				
	return f_scores


def getScores(ti, S):
	scores = []
	for score in ti:
		
		if score % 3 == 0:
			x = int(score / 3)
			if S != 0:
				if x >= 1:
					scores.append((x - 1, x, x + 1))
					S -= 1
					#print("1", "\t", scores, S)
			else:
				scores.append((x, x, x))
				#print("2", "\t", scores, S)
		if (score + 1) % 3 == 0:
			if S != 0:
				if (score - 2) >= 0:
					x = int((score - 2) / 3)
					scores.append((x, x, x + 2))
					S -= 1
					#print("3", "\t", scores, S)
			else:
				x = int((score + 1) / 3)
				if x >= 1:
					scores.append((x, x, x - 1))
					#print("4", "\t", scores, S)
		if (score - 1) % 3 == 0:
			if S != 0:
				x = int((score + 2) / 3)
				if x >= 2:
					scores.append(x, x, x - 2)
					S -= 1
					#print("5", "\t", scores, S)
			else:
				if (score - 1) >= 0:
					x = int((score - 1) / 3)
					scores.append((x, x, x + 1))
					#print("6", "\t", scores, S)
	
	return scores
					
def getMaxStudents(scores, p):
	count = 0
	for score in scores:
		
		if max(score) >= p:
			count += 1
			#print(score, p, max(score), count)
	return count
for i in range(1, T + 1):
	case = lines[i].rstrip('\n').split(' ')
	
	N = int(case[0])
	S = int(case[1])
	p = int(case[2])
	ti = [int(x) for x in case[3:]]
	
	#print (N, S, p, ti)
	
	scores = getScores_2(ti, S, p)
	#print(scores)
	cnt = getMaxStudents(scores, p)
	#print(cnt)
	output = "Case #" + str(i) + ": "
	print(output + str(cnt))
