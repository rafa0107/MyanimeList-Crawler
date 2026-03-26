import scrapy

class AnimeSpider(scrapy.Spider):
    name = "animes"
    start_urls = ['https://myanimelist.net/topanime.php']


    def parse(self, response):
        #Logica do parse
        for anime in response.css("tr.ranking-list"):
            
            dados_iniciais = {
                "Rank" : anime.css("td.rank span::text").get(),
                "Title" : anime.css("h3.anime_ranking_h3 a::text").get(),
                "Information": [i.strip() for i in anime.css("div.information::text").getall() if i.strip()],
                "Score" : anime.css(".score-label::text").get(),
            }
           
            link_interno = anime.css("h3.anime_ranking_h3 a::attr(href)").get()
           
            yield scrapy.Request(
                url = link_interno,
                callback = self.parse_detalhes,
                meta ={'item_parcial': dados_iniciais}
            )
                
        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



    def parse_detalhes(self,response):
        #Para recuperar os dados da pagina anterior
        item = response.meta['item_parcial']
        #Buscando a sinopse e ajustando seu formato
        texto_sinopse = response.css("p[itemprop='description']::text").getall()
        item['Sinopse'] = " ".join(texto_sinopse).strip()
        yield item