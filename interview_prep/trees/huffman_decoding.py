

"""class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    string = ""
    prev = root
    ret = doDecodeHuff(root, s, string, prev)
    print(ret)

#A for loop could potentially use less memory here, less args to pass in
#1001011
def doDecodeHuff(root, s, string, prev):
    if s == "" and root.right and root.left:
        return string
    if root.right and root.left:
        if s[0:1] == "1":
            #print("going right")
            return doDecodeHuff(root.right, s[1:], string, prev)
        if s[0:1] == "0":
            #print("going left")
            return doDecodeHuff(root.left, s[1:], string, prev)
    else:
        string += root.data
        #print("Updating string to: " + str(string))
        #print("s = " + str(s[1:len(s)]))
        return doDecodeHuff(prev, s, string, prev)
    


    

