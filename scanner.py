
def getchar(words,pos):
        

        if pos<0 or pos>=len(words): return None

        
        

        
        if words[pos]>='0' and words[pos]<='1':
                return 'HOUR1'
        
        elif words[pos]=='2':        
                return 'HOUR2'

        elif words[pos]>='0' and words[pos]<='3':
                return 'HOUR3'

        elif words[pos]>='0' and words[pos]<='5':
                return 'MIN1'

        elif words[pos]>='0' and words[pos]<='9':
                return 'MIN2'

        elif words[pos]==':' or words[pos]=='.':
                return 'SEP'

        else:
                return 'OTHER'
        

        
        

def scan(text,transition_table,accept_states):
        """ Scans `text` while transitions exist in 'transition_table'.
        After that, if in a state belonging to `accept_states`,
        returns the corresponding token, else ERROR_TOKEN.
        """
        
        # initial state
        pos = 0
        state = 'q0'
        
        while True:
                
                c = getchar(text,pos)   # get next char
                
                if state in transition_table and c in transition_table[state]:
                
                        state = transition_table[state][c]      # set new state
                        pos += 1        # advance to next char
                        
                else:   # no transition found

                        # check if current state is accepting
                        if state in accept_states:
                                return accept_states[state],pos

                        # current state is not accepting
                        return 'ERROR_TOKEN',pos
                        
        
# the transition table, as a dictionary
td = { 
       'q0' : {'HOUR1' : 'q1', 'HOUR2' : 'q2', 'HOUR3' : 'q3', 'MIN1' : 'q3', 'MIN2' : 'q3','OTHER':'q7'},
       'q1' : {'HOUR1': 'q3', 'HOUR2' : 'q3', 'HOUR3' : 'q3' , 'MIN1' : 'q3','MIN2' : 'q3','SEP' : 'q4'},
       'q2' : {'HOUR1': 'q3', 'HOUR2' : 'q3', 'HOUR3' : 'q3' ,'SEP' : 'q4'},
       'q3' : {'SEP' : 'q4'},     
       'q4' : {'HOUR1': 'q5', 'HOUR2' : 'q5', 'HOUR3' : 'q5', 'MIN1' : 'q5'},
       'q5' : {'HOUR1': 'q6', 'HOUR2' : 'q6', 'HOUR3' : 'q6', 'MIN1' : 'q6', 'MIN2' : 'q6'}
     }



# the dictionary of accepting states and their
# corresponding token
ad = { 'q6':'TIME_TOKEN',
       'q7':'ERROR'}
     


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:     # that is, while len(text)>0
        
        # get next token and position after last char recognized
        token,position = scan(text,td,ad)
        
        if token=='ERROR_TOKEN':
                
                print('unrecognized input at pos',position+1,'of',text)
                print("token:",token)
                break
        
        print("token:",token,"string:",text[:position])
        
        # remaining text for next scan
        text = text[position:]
