
import functions as fn
import website as ws

base_url = "www.blaskelius.se"
sitemap_url = "https://www.blaskelius.se/wp-sitemap-posts-post-1.xml"

hemsida = ws.Website(base_url=base_url, sitemap_url=sitemap_url)


similarity_list = hemsida.get_most_similar_pagesV2()
print(similarity_list)
