for n in ["Dhawan","Kohli"]: 
    total[n] = 0 
    for match in score.keys(): 
        if n in score[match].keys(): 
           total[n] = total[n] + score[match][n]

