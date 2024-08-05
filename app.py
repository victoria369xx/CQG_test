import sys

def main():
    #check correct programm usage
    if len(sys.argv) <= 2 or len(sys.argv) > 3:
        print("Programm usage is python app.py config_path sample_path")
        sys.exit(1)

    #create list of dict from config file where key is default char and value is replacement char 
    with open(sys.argv[1], 'r') as file:
        config = []
        for line in file:
            temp = {line[0]:line[2]}
            config.append(temp)

    #read sample file to list 
    with open (sys.argv[2], 'r') as file:
        sample = []
        for line in file:
            line = line.rstrip()
            sample.append(line)
  
  #iterate through sample line by line, char by char and replace chars where needed. return replaced list of dict with number of substitutions and replaced strings
    list_replaced = []
    for line in sample:
        counter = 0
        for char in line:
            for dict in config:
                for key, value in dict.items():
                    if (char == key):
                        replaced_line = line.replace(char, value)
                        counter += 1 
                    else:
                        counter += 0
        list_replaced.append({'counter': counter, 'string': replaced_line})
    #sort replaced list by number of substitutions in desc order       
    sorted_data = sorted(list_replaced, key = lambda x: (x['counter']), reverse=True)

    #print sorted data to console 
    for dict in sorted_data:
        print(dict['string'])
main()