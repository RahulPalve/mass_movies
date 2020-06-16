import requests
import json
def process(no):
    original_link='https://filmyzilla.digital/download/'+str(no)+'/server_4'
	#https://filmyzilla.digital/download/4522/server_4
    head_ol=requests.head(original_link, allow_redirects= True)
    r_link=head_ol.url
    link=r_link.split('/')
    movie=link[5].split('2')
    movie=movie[0].strip('_')
    movie=movie.replace('_','+')

    #Oimdb key : 154d259c
    #http://www.omdbapi.com/?t=Avengers+Infint&y=2019 API
   
    ml='http://www.omdbapi.com/?t='+movie+'&apikey=154d259c'
    db=requests.get(ml)
    dic=json.loads(db.text)

    return (dic["imdbID"], dic["Title"], dic["Poster"], dic["Plot"], original_link)