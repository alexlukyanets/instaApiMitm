def response (flow):
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
        #content = flow.request.content

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


        #print(flow)
        text = flow.response.text
        text = str(text)
        #print(text)
        write_txt_response_friendships(text)
    
    if data == 'https://i.instagram.com/api/v1/friendships/21399586401/followers/':
        text = flow.response.text
        text = str(text)
        write_txt_response_followers(text)



def write_txt_response_friendships(data):
    f = open("friendships.json", "a")
    f.write(data)
    f.close()

def write_txt_response_followers(data):
    f = open("followers.json", "a")
    f.write(data)
    f.close()