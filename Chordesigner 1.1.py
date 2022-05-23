print("Chordesigner 1.1--create simple chords")
timelist=[]
class Notes():
    def __init__(self):
        self.notes=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    def get_note(self, n, shift=0):
        return self.notes[(1200+n+shift)%12]
    
    def get_num(self, name):
        try:
            return self.notes.index(name.upper())
        except:
            return None
            
class ChordDesigner():
    def __init__(self):
        self.notes=Notes()
        self.chords={'major':[0,4,7], 'minor':[0,3,7], 'major7':[0,4,7,11], 'minor7':[0,3,7,10], 'dominant7':[0,4,7,10], 'major9':[0,4,7,11,14], 'minor9':[0,3,7,10,14], 'dominant9':[0,4,7,10,14], 'diminished':[0,3,6], 'diminished7':[0,3,6,9], 'perfect5th':[0,7], 'aug':[0,4,8]}
        
    def get_chords(self, root, shifts):
        result=''
        for n in shifts:
            result+=self.notes.get_note(root, n)+' '
        return result
    
    def get_num(self, name):
        return self.notes.get_num(name)
    
    def run(self):
        while True:
            name=input('type root note(or type "exit" to quit)\n')
            if name=='exit':
                break
            root=self.get_num(name)
            if root==None:
                print('error')
            else:
                chord=input('type your chord({})\n'.format(str(list(self.chords.keys()))[1:-1]))
                if chord.lower() not in self.chords:
                    print('error')
                else:
                    timelist.append(self.get_chords(root, self.chords[chord.lower()]))
                    print(self.get_chords(root, self.chords[chord.lower()]))
                    print('chordlist:',timelist)
cdes=ChordDesigner()
cdes.run()
