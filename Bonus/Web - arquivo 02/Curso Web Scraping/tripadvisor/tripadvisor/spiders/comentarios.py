# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html#REVIEWS']

    def parse(self, response):
        #Os Comentarios abaixo são para mostrar como era o código antes da mudança
        #Os códigos comentados são aqueles desenvolvidos ao longo do curso
        #Os códigos comentados não são mais válidos
        #Os códigos comentados são para mera comparação e transparência
        item = TripadvisorItem()
        # quadros_de_comentarios = response.xpath("//div[@class='location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw']")
        quadros_de_comentarios = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for quadro in quadros_de_comentarios:
            # item["autor_comentario"] = quadro.xpath(".//div[@class='social-member-event-MemberEventOnObjectBlock__event_type--3njyv']/span/a/text()").get()
            item["autor_comentario"] = quadro.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()").get()
            # item["autor_endereco"] = quadro.xpath(".//span[@class='default social-member-common-MemberHometown__hometown--3kM9S small']/text()").get()
            item["autor_endereco"] = quadro.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            # item["comentario_titulo"] = quadro.xpath(".//div[@class='location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z']/a//span/text()").get()
            item["comentario_titulo"] = quadro.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            # item["comentario_corpo"] = quadro.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item["comentario_corpo"] = quadro.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            # item["comentario_data"] = quadro.xpath(".//span[@class='location-review-review-list-parts-EventDate__event_date--1epHa']/text()").get()
            item["comentario_data"] = quadro.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item
        
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
