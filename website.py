from bs4 import BeautifulSoup
import requests 
import functions as fn

class Website():
   
    def __init__(self,sitemap_url,base_url):
        self.sitemap_list = self.get_sitemap(url = sitemap_url)
        self.pagelist = self.iterate_through_sitemap() 
        
        
    def get_sitemap(self,url):
       """"takes a .xml sitemap and returns a list of individual pages. Example: https://www.hemnet.se/sitemap.xml
        this only makes sense for some sitemaps where they link to individual articles... """
       
       result  = requests.get(url).text
       soup = BeautifulSoup(result,"xml") #var html paser innan 

       sitemap_list_uncleaned = soup.find_all("loc")
       sitemap_list = [site_soup.text for site_soup in sitemap_list_uncleaned]

       return sitemap_list 
    
    def iterate_through_sitemap(self):
        pagelist = [IndividualPage(individual_url) for individual_url in self.sitemap_list] 
        return pagelist 
    

    def get_most_similar_pages(self):
        jaccard_index_list= []

        for page in self.pagelist:
            for other_page in self.pagelist:
                jac_ind = fn.jaccard_index(page.content,other_page.content)
                jaccard_index_list.append([jac_ind,page,other_page])

        return jaccard_index_list
    
    def get_most_similar_pagesV2(self):
        jaccard_index_list= []

        for item in zip(self.pagelist,self.pagelist):  # Okay, zip didn't do what I thought it did... 
            
                jac_ind = fn.jaccard_index(item[0].content,item[1].content)
                jaccard_index_list.append([jac_ind,item])

        return jaccard_index_list
    





class IndividualPage():

    def __init__(self,url):
        self.url = url
        self.soup = self.get_soup()
        self.content = self.get_content()
        self.links = self.get_links()
   
    def get_soup(self):
        """makes a request to url, returns html

        Returns:
            _soub Object?
        """
        result  = requests.get(self.url).text
        soup = BeautifulSoup(result,"html.parser")
        return soup

    def get_links(self): # we need to make sure that these are internal links... 
       links = [link.get('href') for link in self.soup.find_all('a')]
       return links 
    
    def get_content(self):
        content = self.soup.text
        return content 


