# Read text from a file, and count the occurence of words in that text
#count words

def read_file(filename):
    open_file = open("C:/Users/USER/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt", "r")
    read_file = open_file.read() 
    #print(read_file)
    new = read_file.split()
    #print(new)
       
    count ={}
    for i in new:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return count
print(read_file("./story.txt"))