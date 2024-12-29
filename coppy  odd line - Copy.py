def copy_odd_lines(source_file,destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as dest:
        for i, line in enumerate (source):
            if i % 2 != 0:
                dest.write(line)

copy_odd_lines('list2.txt','odd.txt')


