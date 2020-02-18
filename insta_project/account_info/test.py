import csv

def write_csv_request(data):
    with open('request.csv', 'a', newline='') as file:# with is content manager
        writer = csv.writer(file)
        writer.writerow(data)

def write_csv_response(data):
    with open('response.csv', 'a', newline='') as file:# with is content manager
        writer = csv.writer(file)
        writer.writerow(data)

def write_txt_response(data):
    f = open("response.txt", "a")
    f.write(data)
    f.close()

def write_txt_requets(data):
    f = open("requets.txt", "a")
    f.write(data)
    f.close()


def response(flow):
    content = flow.response.content
    cookies = flow.response.cookies
    decode = flow.response.decode
    encode = flow.response.encode
    data = flow.response.get_content

    get_text = flow.response.get_text
    headers = flow.response.headers
    http_version = flow.response.http_version
    raw_content = flow.response.raw_content

    text = flow.response.text
    timestamp_end = flow.response.timestamp_end
    timestamp_start = flow.response.timestamp_start

    
    #print('content ' + str(content))
    #print('cookies ' +  str(cookies))
    #print('decode ' + str(decode))
    #print('encode ' + str(encode))
    #print('data ' + str(data ))
    #print('get_text ' + str(get_text))
    #print('headers ' + str(headers))
    #print('http_version ' + str(http_version))
    #print('raw_content ' + str(raw_content))
    #print('text ' + str(text))
    #print('timestamp_start ' + str(timestamp_start))
    #print('timestamp_end ' + str(timestamp_end))

    #text = str(text)
    #write_txt_response(text)
    
def request (flow):
    pretty_url = flow.request.pretty_url
    data = str(pretty_url)
    if data == 'https://i.instagram.com/api/v1/friendships/21399586401/following/?includes_hashtags=1':
           
        host = flow.request.host
        host_header = flow.request.host_header
        method = flow.request.method
        multipart_form = flow.request.multipart_form
        path = flow.request.path
        path_components = flow.request.path_components
        pretty_host = flow.request.pretty_host
        pretty_url = flow.request.pretty_url
        query = flow.request.query
        content = flow.request.content

        url = flow.request.url
        urlencoded_form = flow.request.urlencoded_form

        print('host ' + str(host))
        print('host_header ' +  str(host_header))
        print('method ' + str(method))
        print('multipart_form ' +  str(multipart_form))
        print('path ' + str(path))
        print('path_components ' +  str(path_components))
        print('pretty_host ' + str(pretty_host))
        print('pretty_url ' +  str(pretty_url))
        print('query ' + str(query))
        print('url ' +  str(url))
        print('urlencoded_form ' + str(urlencoded_form))
        #print('content ' + str(content))
        #print('get_content ' + str(get_content))
        #print('text ' + str(text))


        print(flow)
        text = flow.response.text
        text = str(text)
        print(text)
        write_txt_response(text)