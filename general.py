import os

# Each website crawled will create a new project (Folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project "+ directory)
        os.makedirs(directory)


# Create the queue and the crawled files
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        make_file(queue,base_url)
    if not os.path.isfile(crawled):
        make_file(crawled,'')

# Create a new file
def make_file(path,data):
    f= open(path,'w')
    f.write(data)
    f.close()

# Add data to an exisitng file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass

# To read a file and convert to a set item
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))

    return results

# To convert a set to a file
def set_to_links(links,file):
    delete_file_contents(file)
    for line in sorted(links):
        append_to_file(file,line)
